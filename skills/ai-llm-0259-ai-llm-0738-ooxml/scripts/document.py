#!/usr/bin/env python3
class Document:
    def __init__(self, path):
        self.path = path
        print(f"Initialized Document at {self.path}")

class DocxXMLEditor:
    def __init__(self, path):
        self.path = path
        print(f"Initialized DocxXMLEditor at {self.path}")

if __name__ == "__main__":
    print("OOXML Document Library.")
