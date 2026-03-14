import sys
from pypdf import PdfReader

def extract_text(pdf_path):
    """
    指定されたパスのPDFからテキストを抽出する
    """
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"
        return text
    except Exception as e:
        return f"Error extracting text: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_text.py <pdf_path>")
        sys.exit(1)
    
    path = sys.argv[1]
    result = extract_text(path)
    print(result)
