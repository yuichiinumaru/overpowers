import json
import secrets
import os

class CanvasBuilder:
    def __init__(self):
        self.canvas = {
            "nodes": [],
            "edges": []
        }
        
    def _generate_id(self):
        return secrets.token_hex(8) # 16 character hex string
        
    def add_text_node(self, x, y, width, height, text, color=None):
        node = {
            "id": self._generate_id(),
            "type": "text",
            "x": x,
            "y": y,
            "width": width,
            "height": height,
            "text": text
        }
        if color:
            node["color"] = color
        self.canvas["nodes"].append(node)
        return node["id"]
        
    def add_file_node(self, x, y, width, height, file_path, subpath=None, color=None):
        node = {
            "id": self._generate_id(),
            "type": "file",
            "x": x,
            "y": y,
            "width": width,
            "height": height,
            "file": file_path
        }
        if subpath:
            node["subpath"] = subpath
        if color:
            node["color"] = color
        self.canvas["nodes"].append(node)
        return node["id"]
        
    def add_edge(self, from_node, to_node, from_side="right", to_side="left", label=None, color=None):
        edge = {
            "id": self._generate_id(),
            "fromNode": from_node,
            "fromSide": from_side,
            "toNode": to_node,
            "toSide": to_side
        }
        if label:
            edge["label"] = label
        if color:
            edge["color"] = color
        self.canvas["edges"].append(edge)
        return edge["id"]
        
    def save(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.canvas, f, indent=2)
        print(f"✅ Canvas saved to {filename}")

def example():
    builder = CanvasBuilder()
    n1 = builder.add_text_node(0, 0, 300, 150, "# Root Node\nMain concept")
    n2 = builder.add_text_node(400, -100, 250, 100, "## Child A\nSupporting detail")
    builder.add_edge(n1, n2, label="supports")
    builder.save("example.canvas")

if __name__ == "__main__":
    example()
