#!/usr/bin/env python3
import json
import argparse
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Optional, Tuple, Set

class NodeType(Enum):
    OR = "or"
    AND = "and"
    LEAF = "leaf"

class Difficulty(Enum):
    TRIVIAL = 1
    LOW = 2
    MEDIUM = 3
    HIGH = 4
    EXPERT = 5

class Cost(Enum):
    FREE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    VERY_HIGH = 4

class DetectionRisk(Enum):
    NONE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CERTAIN = 4

@dataclass
class AttackAttributes:
    difficulty: Difficulty = Difficulty.MEDIUM
    cost: Cost = Cost.MEDIUM
    detection_risk: DetectionRisk = DetectionRisk.MEDIUM
    time_hours: float = 8.0
    requires_insider: bool = False
    requires_physical: bool = False

@dataclass
class AttackNode:
    id: str
    name: str
    description: str
    node_type: NodeType
    attributes: AttackAttributes = field(default_factory=AttackAttributes)
    children: List['AttackNode'] = field(default_factory=list)
    mitigations: List[str] = field(default_factory=list)
    cve_refs: List[str] = field(default_factory=list)

    def add_child(self, child: 'AttackNode') -> None:
        self.children.append(child)

    def calculate_path_difficulty(self) -> float:
        if self.node_type == NodeType.LEAF:
            return self.attributes.difficulty.value
        if not self.children:
            return 0
        child_difficulties = [c.calculate_path_difficulty() for c in self.children]
        if self.node_type == NodeType.OR:
            return min(child_difficulties)
        else:  # AND
            return max(child_difficulties)

    def calculate_path_cost(self) -> float:
        if self.node_type == NodeType.LEAF:
            return self.attributes.cost.value
        if not self.children:
            return 0
        child_costs = [c.calculate_path_cost() for c in self.children]
        if self.node_type == NodeType.OR:
            return min(child_costs)
        else:  # AND
            return sum(child_costs)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "type": self.node_type.value,
            "attributes": {
                "difficulty": self.attributes.difficulty.name,
                "cost": self.attributes.cost.name,
                "detection_risk": self.attributes.detection_risk.name,
                "time_hours": self.attributes.time_hours,
            },
            "mitigations": self.mitigations,
            "children": [c.to_dict() for c in self.children]
        }

@dataclass
class AttackTree:
    name: str
    description: str
    root: AttackNode
    version: str = "1.0"

    def find_easiest_path(self) -> List[AttackNode]:
        return self._find_path(self.root, minimize="difficulty")

    def _find_path(self, node: AttackNode, minimize: str) -> List[AttackNode]:
        if node.node_type == NodeType.LEAF:
            return [node]
        if not node.children:
            return [node]
        if node.node_type == NodeType.OR:
            best_path = None
            best_score = float('inf')
            for child in node.children:
                child_path = self._find_path(child, minimize)
                score = self._path_score(child_path, minimize)
                if score < best_score:
                    best_score = score
                    best_path = child_path
            return [node] + (best_path or [])
        else:  # AND
            path = [node]
            for child in node.children:
                path.extend(self._find_path(child, minimize))
            return path

    def _path_score(self, path: List[AttackNode], metric: str) -> float:
        if metric == "difficulty":
            return sum(n.attributes.difficulty.value for n in path if n.node_type == NodeType.LEAF)
        elif metric == "cost":
            return sum(n.attributes.cost.value for n in path if n.node_type == NodeType.LEAF)
        elif metric == "detection":
            return sum(n.attributes.detection_risk.value for n in path if n.node_type == NodeType.LEAF)
        return 0

    def export_json(self) -> str:
        return json.dumps({
            "name": self.name,
            "description": self.description,
            "version": self.version,
            "root": self.root.to_dict()
        }, indent=2)

class MermaidExporter:
    def __init__(self, tree: AttackTree):
        self.tree = tree
        self._lines: List[str] = []
        self._node_count = 0

    def export(self) -> str:
        self._lines = ["flowchart TD"]
        self._export_node(self.tree.root, None)
        return "\n".join(self._lines)

    def _export_node(self, node: AttackNode, parent_id: Optional[str]) -> str:
        node_id = f"N{self._node_count}"
        self._node_count += 1
        if node.node_type == NodeType.OR:
            shape = f"{node_id}(({node.name}))"
        elif node.node_type == NodeType.AND:
            shape = f"{node_id}[{node.name}]"
        else:  # LEAF
            style = self._get_leaf_style(node)
            shape = f"{node_id}[/{node.name}/]"
            self._lines.append(f"    style {node_id} {style}")
        self._lines.append(f"    {shape}")
        if parent_id:
            connector = "-->" if node.node_type != NodeType.AND else "==>"
            self._lines.append(f"    {parent_id} {connector} {node_id}")
        for child in node.children:
            self._export_node(child, node_id)
        return node_id

    def _get_leaf_style(self, node: AttackNode) -> str:
        colors = {
            Difficulty.TRIVIAL: "fill:#ff6b6b",
            Difficulty.LOW: "fill:#ffa06b",
            Difficulty.MEDIUM: "fill:#ffd93d",
            Difficulty.HIGH: "fill:#6bcb77",
            Difficulty.EXPERT: "fill:#4d96ff",
        }
        return colors.get(node.attributes.difficulty, "fill:#gray")

class AttackPathAnalyzer:
    def __init__(self, tree: AttackTree):
        self.tree = tree

    def get_all_paths(self) -> List[List[AttackNode]]:
        paths = []
        self._collect_paths(self.tree.root, [], paths)
        return paths

    def _collect_paths(self, node: AttackNode, current_path: List[AttackNode], all_paths: List[List[AttackNode]]) -> None:
        current_path = current_path + [node]
        if node.node_type == NodeType.LEAF or not node.children:
            all_paths.append(current_path)
            return
        if node.node_type == NodeType.OR:
            for child in node.children:
                self._collect_paths(child, current_path, all_paths)
        else:  # AND
            child_paths = []
            for child in node.children:
                child_sub_paths = []
                self._collect_paths(child, [], child_sub_paths)
                child_paths.append(child_sub_paths)
            combined = self._combine_and_paths(child_paths)
            for combo in combined:
                all_paths.append(current_path + combo)

    def _combine_and_paths(self, child_paths: List[List[List[AttackNode]]]) -> List[List[AttackNode]]:
        if not child_paths: return [[]]
        if len(child_paths) == 1: return [path for paths in child_paths for path in paths]
        result = [[]]
        for paths in child_paths:
            new_result = []
            for existing in result:
                for path in paths:
                    new_result.append(existing + path)
            result = new_result
        return result

def main():
    parser = argparse.ArgumentParser(description="Attack Tree Construction Tool")
    parser.add_argument("action", choices=["analyze", "export-mermaid"], help="Action to perform")
    parser.add_argument("--file", required=True, help="Attack tree JSON file")
    args = parser.parse_args()

    with open(args.file, 'r') as f:
        data = json.load(f)
    
    # Simple reconstruction from JSON (placeholder for full parser)
    # This tool expects a JSON format compatible with AttackTree.export_json()
    print(f"Loaded attack tree: {data.get('name')}")
    
    if args.action == "analyze":
        # Implementation of analysis output
        print("Analysis features coming soon...")
    elif args.action == "export-mermaid":
        # Implementation of mermaid export
        print("Mermaid export features coming soon...")

if __name__ == "__main__":
    main()
