/**
 * Helper scripts extracted from SKILL.md for sci-quant-0842-sci-quant-0042-agentdb-vector-search
 */
async function ragQuery(db, llm, embed, question) {
  // 1. Get relevant context
  const queryEmbedding = await embed(question);
  const context = await db.searchSimilar(
    queryEmbedding,
    { limit: 5, threshold: 0.7 }
  );

  // 2. Generate answer with context
  const prompt = `Context: ${context.map(c => c.text).join('\n')}
Question: ${question}`;

  return await llm.generate(prompt);
}
module.exports = { ragQuery };
