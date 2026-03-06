import sys
from Bio import SeqIO

def convert_sequence(input_file, input_format, output_file, output_format):
    print(f"🔄 Converting {input_file} ({input_format}) to {output_file} ({output_format})...")
    try:
        count = SeqIO.convert(input_file, input_format, output_file, output_format)
        print(f"✅ Successfully converted {count} records.")
        return True
    except Exception as e:
        print(f"❌ Conversion failed: {e}")
        return False

def main():
    if len(sys.argv) < 5:
        print("Usage: python seq_converter.py <input_file> <input_format> <output_file> <output_format>")
        print("Example: python seq_converter.py input.gb genbank output.fasta fasta")
        sys.exit(1)
    
    if not convert_sequence(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]):
        sys.exit(1)

if __name__ == "__main__":
    main()
