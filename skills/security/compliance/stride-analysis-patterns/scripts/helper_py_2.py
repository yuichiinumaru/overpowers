#!/usr/bin/env python3

from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class Interaction:
    """Represents an interaction between two components."""
    id: str
    source: str
    target: str
    action: str
    data: str
    protocol: str


class StridePerInteraction:
    """Apply STRIDE to each interaction in the system."""

    INTERACTION_THREATS = {
        # Source type -> Target type -> Applicable threats
        ("external", "process"): {
            "S": "External entity spoofing identity to process",
            "T": "Tampering with data sent to process",
            "R": "External entity denying sending data",
            "I": "Data exposure during transmission",
            "D": "Flooding process with requests",
            "E": "Exploiting process to gain privileges",
        },
        ("process", "datastore"): {
            "T": "Process tampering with stored data",
            "R": "Process denying data modifications",
            "I": "Unauthorized data access by process",
            "D": "Process exhausting storage resources",
        },
        ("process", "process"): {
            "S": "Process spoofing another process",
            "T": "Tampering with inter-process data",
            "I": "Data leakage between processes",
            "D": "One process overwhelming another",
            "E": "Process gaining elevated access",
        },
    }

    def analyze_interaction(
        self,
        interaction: Interaction,
        source_type: str,
        target_type: str
    ) -> List[Dict]:
        """Analyze a single interaction for STRIDE threats."""
        threats = []
        key = (source_type, target_type)

        applicable_threats = self.INTERACTION_THREATS.get(key, {})

        for stride_code, description in applicable_threats.items():
            threats.append({
                "interaction_id": interaction.id,
                "source": interaction.source,
                "target": interaction.target,
                "stride_category": stride_code,
                "threat_description": description,
                "context": f"{interaction.action} - {interaction.data}",
            })

        return threats

    def generate_threat_matrix(
        self,
        interactions: List[Interaction],
        element_types: Dict[str, str]
    ) -> List[Dict]:
        """Generate complete threat matrix for all interactions."""
        all_threats = []

        for interaction in interactions:
            source_type = element_types.get(interaction.source, "unknown")
            target_type = element_types.get(interaction.target, "unknown")

            threats = self.analyze_interaction(
                interaction, source_type, target_type
            )
            all_threats.extend(threats)

        return all_threats
