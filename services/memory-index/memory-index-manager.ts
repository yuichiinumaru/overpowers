import Database from 'better-sqlite3';
import * as sqliteVec from 'sqlite-vec';
import * as path from 'path';
import * as fs from 'fs';

export interface ChunkMetadata {
  type: 'code' | 'docs' | 'chat';
  startLine?: number;
  endLine?: number;
}

export interface SearchResult {
  id: number;
  file_path: string;
  content: string;
  metadata: any;
  score?: number;
}

export class MemoryIndexManager {
  private db: Database.Database;

  constructor(dbPath: string) {
    // Ensure directory exists
    const dir = path.dirname(dbPath);
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }

    this.db = new Database(dbPath);
    sqliteVec.load(this.db);
    this.initDatabase();
  }

  private initDatabase() {
    this.db.exec(`
      CREATE TABLE IF NOT EXISTS files (
        path TEXT PRIMARY KEY,
        hash TEXT,
        mtime INTEGER
      );
      CREATE TABLE IF NOT EXISTS chunks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_path TEXT,
        content TEXT,
        metadata TEXT,
        FOREIGN KEY(file_path) REFERENCES files(path)
      );
      CREATE VIRTUAL TABLE IF NOT EXISTS chunks_vec USING vec0(
        embedding float[1536]
      );
      CREATE VIRTUAL TABLE IF NOT EXISTS chunks_fts USING fts5(
        content,
        file_path,
        content='chunks',
        content_rowid='id'
      );
      CREATE TABLE IF NOT EXISTS embedding_cache (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content_hash TEXT UNIQUE,
        embedding BLOB
      );
      
      -- Triggers for FTS updates
      CREATE TRIGGER IF NOT EXISTS chunks_ai AFTER INSERT ON chunks BEGIN
        INSERT INTO chunks_fts(rowid, content, file_path) VALUES (new.id, new.content, new.file_path);
      END;
      CREATE TRIGGER IF NOT EXISTS chunks_ad AFTER DELETE ON chunks BEGIN
        INSERT INTO chunks_fts(chunks_fts, rowid, content, file_path) VALUES('delete', old.id, old.content, old.file_path);
      END;
      CREATE TRIGGER IF NOT EXISTS chunks_au AFTER UPDATE ON chunks BEGIN
        INSERT INTO chunks_fts(chunks_fts, rowid, content, file_path) VALUES('delete', old.id, old.content, old.file_path);
        INSERT INTO chunks_fts(rowid, content, file_path) VALUES (new.id, new.content, new.file_path);
      END;
    `);
  }

  public storeFile(filePath: string, content: string, hash: string, mtime: number) {
    const insertFile = this.db.prepare('INSERT OR REPLACE INTO files (path, hash, mtime) VALUES (?, ?, ?)');
    insertFile.run(filePath, hash, mtime);
  }

  public storeChunk(filePath: string, content: string, metadata: ChunkMetadata) {
    const insertChunk = this.db.prepare('INSERT INTO chunks (file_path, content, metadata) VALUES (?, ?, ?)');
    const result = insertChunk.run(filePath, content, JSON.stringify(metadata));
    return result.lastInsertRowid;
  }
  
  public storeEmbedding(chunkId: number | bigint, embedding: Float32Array) {
    const insertVec = this.db.prepare('INSERT INTO chunks_vec (rowid, embedding) VALUES (?, ?)');
    const id = typeof chunkId === 'bigint' ? chunkId : BigInt(chunkId);
    insertVec.run(id, new Uint8Array(embedding.buffer));
  }

  public searchKeyword(query: string, limit: number = 10) {
    const stmt = this.db.prepare(`
      SELECT chunks.id, chunks.file_path, chunks.content, chunks.metadata
      FROM chunks_fts
      JOIN chunks ON chunks.id = chunks_fts.rowid
      WHERE chunks_fts MATCH ?
      ORDER BY rank
      LIMIT ?
    `);
    return stmt.all(query, limit);
  }
  
  public searchVector(embedding: Float32Array, limit: number = 10) {
    const stmt = this.db.prepare(`
      SELECT chunks.id, chunks.file_path, chunks.content, chunks.metadata, chunks_vec.distance
      FROM chunks_vec
      JOIN chunks ON chunks.id = chunks_vec.rowid
      WHERE embedding MATCH ? AND k = ?
      ORDER BY distance
    `);
    return stmt.all(new Uint8Array(embedding.buffer), limit);
  }
  
  public async hybridSearch(query: string, embedding: Float32Array, limit: number = 10): Promise<SearchResult[]> {
    const k = 60; // Constant for RRF
    
    // 1. Get results from Keyword Search
    const keywordResults = this.searchKeyword(query, limit * 2) as SearchResult[];
    
    // 2. Get results from Vector Search
    const vectorResults = this.searchVector(embedding, limit * 2) as SearchResult[];
    
    // 3. Combine using RRF
    const combinedScores = new Map<number, { result: SearchResult, score: number }>();
    
    // Add keyword scores
    keywordResults.forEach((res, index) => {
      const score = 1.0 / (k + index + 1);
      combinedScores.set(res.id, { result: res, score });
    });
    
    // Add/Update vector scores
    vectorResults.forEach((res, index) => {
      const vecScore = 1.0 / (k + index + 1);
      const existing = combinedScores.get(res.id);
      if (existing) {
        existing.score += vecScore;
      } else {
        combinedScores.set(res.id, { result: res, score: vecScore });
      }
    });
    
    // 4. Convert map to array, sort, and limit
    const results = Array.from(combinedScores.values())
      .map(item => ({
        ...item.result,
        score: item.score,
        metadata: typeof item.result.metadata === 'string' ? JSON.parse(item.result.metadata) : item.result.metadata
      }))
      .sort((a, b) => (b.score || 0) - (a.score || 0))
      .slice(0, limit);
      
    return results;
  }
  
  public getFile(filePath: string) {
    const stmt = this.db.prepare('SELECT * FROM files WHERE path = ?');
    return stmt.get(filePath);
  }

  public close() {
    this.db.close();
  }
}
