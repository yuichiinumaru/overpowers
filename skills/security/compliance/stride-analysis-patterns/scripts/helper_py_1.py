#!/usr/bin/env python3

from dataclasses import dataclass
from typing import List, Set, Tuple
from enum import Enum

class ElementType(Enum):
    EXTERNAL_ENTITY = "external"
    PROCESS = "process"
    DATA_STORE = "datastore"
    DATA_FLOW = "dataflow"


@dataclass
class DFDElement:
    id: str
    name: str
    type: ElementType
    trust_level: int  # 0 = untrusted, higher = more trusted
    description: str = ""


@dataclass
class DataFlow:
    id: str
    name: str
    source: str
    destination: str
    data_type: str
    protocol: str
    encrypted: bool = False


class DFDAnalyzer:
    """Analyze Data Flow Diagrams for STRIDE threats."""

    def __init__(self):
        self.elements: Dict[str, DFDElement] = {}
        self.flows: List[DataFlow] = []

    def add_element(self, element: DFDElement) -> None:
        self.elements[element.id] = element

    def add_flow(self, flow: DataFlow) -> None:
        self.flows.append(flow)

    def find_trust_boundary_crossings(self) -> List[Tuple[DataFlow, int]]:
        """Find data flows that cross trust boundaries."""
        crossings = []
        for flow in self.flows:
            source = self.elements.get(flow.source)
            dest = self.elements.get(flow.destination)
            if source and dest and source.trust_level != dest.trust_level:
                trust_diff = abs(source.trust_level - dest.trust_level)
                crossings.append((flow, trust_diff))
        return sorted(crossings, key=lambda x: x[1], reverse=True)

    def identify_threats_per_element(self) -> Dict[str, List[StrideCategory]]:
        """Map applicable STRIDE categories to element types."""
        threat_mapping = {
            ElementType.EXTERNAL_ENTITY: [
                StrideCategory.SPOOFING,
                StrideCategory.REPUDIATION,
            ],
            ElementType.PROCESS: [
                StrideCategory.SPOOFING,
                StrideCategory.TAMPERING,
                StrideCategory.REPUDIATION,
                StrideCategory.INFORMATION_DISCLOSURE,
                StrideCategory.DENIAL_OF_SERVICE,
                StrideCategory.ELEVATION_OF_PRIVILEGE,
            ],
            ElementType.DATA_STORE: [
                StrideCategory.TAMPERING,
                StrideCategory.REPUDIATION,
                StrideCategory.INFORMATION_DISCLOSURE,
                StrideCategory.DENIAL_OF_SERVICE,
            ],
            ElementType.DATA_FLOW: [
                StrideCategory.TAMPERING,
                StrideCategory.INFORMATION_DISCLOSURE,
                StrideCategory.DENIAL_OF_SERVICE,
            ],
        }

        result = {}
        for elem_id, elem in self.elements.items():
            result[elem_id] = threat_mapping.get(elem.type, [])
        return result

    def analyze_unencrypted_flows(self) -> List[DataFlow]:
        """Find unencrypted data flows crossing trust boundaries."""
        risky_flows = []
        for flow in self.flows:
            if not flow.encrypted:
                source = self.elements.get(flow.source)
                dest = self.elements.get(flow.destination)
                if source and dest and source.trust_level != dest.trust_level:
                    risky_flows.append(flow)
        return risky_flows

    def generate_threat_enumeration(self) -> List[Dict]:
        """Generate comprehensive threat enumeration."""
        threats = []
        element_threats = self.identify_threats_per_element()

        for elem_id, categories in element_threats.items():
            elem = self.elements[elem_id]
            for category in categories:
                threats.append({
                    "element_id": elem_id,
                    "element_name": elem.name,
                    "element_type": elem.type.value,
                    "stride_category": category.name,
                    "description": f"{category.name} threat against {elem.name}",
                    "trust_level": elem.trust_level
                })

        return threats
