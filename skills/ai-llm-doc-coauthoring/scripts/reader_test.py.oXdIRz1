#!/usr/bin/env python3
"""
Automate Stage 3: Reader Testing for a document.
"""
import sys
import subprocess
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Run Reader Testing on a document.")
    parser.add_argument("doc_path", help="Path to the document file")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.doc_path):
        print(f"Error: Document not found at {args.doc_path}")
        sys.exit(1)

    print(f"Starting Reader Testing for: {args.doc_path}")
    
    # Predict questions
    predict_prompt = f"Read the document at {args.doc_path} and predict 5-10 questions a reader might ask. Output only the questions, one per line."
    
    print("1. Predicting reader questions...")
    result = subprocess.run(["gemini", "-p", predict_prompt], capture_output=True, text=True)
    questions = [q.strip() for q in result.stdout.split('\n') if q.strip()]
    
    if not questions:
        print("Failed to generate questions.")
        sys.exit(1)

    print(f"Generated {len(questions)} questions.")

    # Test questions
    print("2. Testing questions with a fresh agent...")
    for i, q in enumerate(questions):
        print(f"\nQuestion {i+1}: {q}")
        test_prompt = f"Based ONLY on the document at {args.doc_path}, answer the following question: {q}. If the answer is not in the doc, say so."
        subprocess.run(["gemini", "-p", test_prompt])

    # Final check
    print("\n3. Running final ambiguity and consistency check...")
    final_prompt = f"Read the document at {args.doc_path} and identify any ambiguities, false assumptions, or internal contradictions. Be critical."
    subprocess.run(["gemini", "-p", final_prompt])

    print("\nReader Testing completed.")

if __name__ == "__main__":
    main()
