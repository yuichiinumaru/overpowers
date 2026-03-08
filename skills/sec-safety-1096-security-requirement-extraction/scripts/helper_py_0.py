#!/usr/bin/env python3

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Optional, Set
from datetime import datetime

class RequirementType(Enum):
    FUNCTIONAL = "functional"
    NON_FUNCTIONAL = "non_functional"
    CONSTRAINT = "constraint"


class Priority(Enum):
    CRITICAL = 1
    HIGH = 2
    MEDIUM = 3
    LOW = 4


class SecurityDomain(Enum):
    AUTHENTICATION = "authentication"
    AUTHORIZATION = "authorization"
    DATA_PROTECTION = "data_protection"
    AUDIT_LOGGING = "audit_logging"
    INPUT_VALIDATION = "input_validation"
    ERROR_HANDLING = "error_handling"
    SESSION_MANAGEMENT = "session_management"
    CRYPTOGRAPHY = "cryptography"
    NETWORK_SECURITY = "network_security"
    AVAILABILITY = "availability"


class ComplianceFramework(Enum):
    PCI_DSS = "pci_dss"
    HIPAA = "hipaa"
    GDPR = "gdpr"
    SOC2 = "soc2"
    NIST_CSF = "nist_csf"
    ISO_27001 = "iso_27001"
    OWASP = "owasp"


@dataclass
class SecurityRequirement:
    id: str
    title: str
    description: str
    req_type: RequirementType
    domain: SecurityDomain
    priority: Priority
    rationale: str = ""
    acceptance_criteria: List[str] = field(default_factory=list)
    test_cases: List[str] = field(default_factory=list)
    threat_refs: List[str] = field(default_factory=list)
    compliance_refs: List[str] = field(default_factory=list)
    dependencies: List[str] = field(default_factory=list)
    status: str = "draft"
    owner: str = ""
    created_date: datetime = field(default_factory=datetime.now)

    def to_user_story(self) -> str:
        """Convert to user story format."""
        return f"""
**{self.id}: {self.title}**

As a security-conscious system,
I need to {self.description.lower()},
So that {self.rationale.lower()}.

**Acceptance Criteria:**
{chr(10).join(f'- [ ] {ac}' for ac in self.acceptance_criteria)}

**Priority:** {self.priority.name}
**Domain:** {self.domain.value}
**Threat References:** {', '.join(self.threat_refs)}
"""

    def to_test_spec(self) -> str:
        """Convert to test specification."""
        return f"""
## Test Specification: {self.id}

### Requirement
{self.description}

### Test Cases
{chr(10).join(f'{i+1}. {tc}' for i, tc in enumerate(self.test_cases))}

### Acceptance Criteria Verification
{chr(10).join(f'- {ac}' for ac in self.acceptance_criteria)}
"""


@dataclass
class RequirementSet:
    name: str
    version: str
    requirements: List[SecurityRequirement] = field(default_factory=list)

    def add(self, req: SecurityRequirement) -> None:
        self.requirements.append(req)

    def get_by_domain(self, domain: SecurityDomain) -> List[SecurityRequirement]:
        return [r for r in self.requirements if r.domain == domain]

    def get_by_priority(self, priority: Priority) -> List[SecurityRequirement]:
        return [r for r in self.requirements if r.priority == priority]

    def get_by_threat(self, threat_id: str) -> List[SecurityRequirement]:
        return [r for r in self.requirements if threat_id in r.threat_refs]

    def get_critical_requirements(self) -> List[SecurityRequirement]:
        return [r for r in self.requirements if r.priority == Priority.CRITICAL]

    def export_markdown(self) -> str:
        """Export all requirements as markdown."""
        lines = [f"# Security Requirements: {self.name}\n"]
        lines.append(f"Version: {self.version}\n")

        for domain in SecurityDomain:
            domain_reqs = self.get_by_domain(domain)
            if domain_reqs:
                lines.append(f"\n## {domain.value.replace('_', ' ').title()}\n")
                for req in domain_reqs:
                    lines.append(req.to_user_story())

        return "\n".join(lines)

    def traceability_matrix(self) -> Dict[str, List[str]]:
        """Generate threat-to-requirement traceability."""
        matrix = {}
        for req in self.requirements:
            for threat_id in req.threat_refs:
                if threat_id not in matrix:
                    matrix[threat_id] = []
                matrix[threat_id].append(req.id)
        return matrix
