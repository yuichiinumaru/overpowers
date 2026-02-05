import { Buffer } from 'buffer';

/**
 * Writer for manual Protobuf encoding.
 * Essential for communicating with restrictive gRPC/Connect backends without heavy dependencies.
 */
export class ProtoWriter {
  private parts: Buffer[] = [];

  /**
   * Writes a variable-length integer (Varint).
   */
  writeVarint(v: number) {
    const b: number[] = [];
    while (v > 127) {
      b.push((v & 0x7f) | 0x80);
      v >>>= 7;
    }
    b.push(v & 0x7f);
    this.parts.push(Buffer.from(b));
  }

  /**
   * Writes a string field.
   */
  writeString(field: number, value: string) {
    const buf = Buffer.from(value, 'utf8');
    this.writeVarint((field << 3) | 2); // WireType 2 = Length-delimited
    this.writeVarint(buf.length);
    this.parts.push(buf);
  }

  /**
   * Writes a nested message field.
   */
  writeMessage(field: number, writer: ProtoWriter) {
    const buf = writer.toBuffer();
    this.writeVarint((field << 3) | 2);
    this.writeVarint(buf.length);
    this.parts.push(buf);
  }

  /**
   * Writes a 32-bit integer field.
   */
  writeInt32(field: number, value: number) {
    this.writeVarint((field << 3) | 0); // WireType 0 = Varint (technically int32 is varint encoded usually, or fixed32)
    // Note: Standard protobuf int32 is varint. fixed32 is WireType 5.
    // Based on reference implementation using writeVarint for int32.
    this.writeVarint(value);
  }

  toBuffer(): Buffer {
    return Buffer.concat(this.parts);
  }
}

/**
 * Creates a Connect-RPC envelope frame.
 * Format: [CompressionFlag(1)] + [Length(4, BigEndian)] + [Payload]
 */
export function createConnectFrame(payload: Buffer, compressed: boolean = false): Buffer {
  const frame = Buffer.alloc(5 + payload.length);
  frame[0] = compressed ? 1 : 0;
  frame.writeUInt32BE(payload.length, 1);
  payload.copy(frame, 5);
  return frame;
}
