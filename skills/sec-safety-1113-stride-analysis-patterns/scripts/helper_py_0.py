#!/usr/bin/env python3

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Optional
import json

class StrideCategory(Enum):
    SPOOFING = "S"
    TAMPERING = "T"
    REPUDIATION = "R"
    INFORMATION_DISCLOSURE = "I"
    DENIAL_OF_SERVICE = "D"
    ELEVATION_OF_PRIVILEGE = "E"


class Impact(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


class Likelihood(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


@dataclass
class Threat:
    id: str
    category: StrideCategory
    title: str
    description: str
    target: str
    impact: Impact
    likelihood: Likelihood
    mitigations: List[str] = field(default_factory=list)
    status: str = "open"

    @property
    def risk_score(self) -> int:
        return self.impact.value * self.likelihood.value

    @property
    def risk_level(self) -> str:
        score = self.risk_score
        if score >= 12:
            return "Critical"
        elif score >= 6:
            return "High"
        elif score >= 3:
            return "Medium"
        return "Low"


@dataclass
class Asset:
    name: str
    sensitivity: str
    description: str
    data_classification: str


@dataclass
class TrustBoundary:
    name: str
    description: str
    from_zone: str
    to_zone: str


@dataclass
class ThreatModel:
    name: str
    version: str
    description: str
    assets: List[Asset] = field(default_factory=list)
    boundaries: List[TrustBoundary] = field(default_factory=list)
    threats: List[Threat] = field(default_factory=list)

    def add_threat(self, threat: Threat) -> None:
        self.threats.append(threat)

    def get_threats_by_category(self, category: StrideCategory) -> List[Threat]:
        return [t for t in self.threats if t.category == category]

    def get_critical_threats(self) -> List[Threat]:
        return [t for t in self.threats if t.risk_level in ("Critical", "High")]

    def generate_report(self) -> Dict:
        """Generate threat model report."""
        return {
            "summary": {
                "name": self.name,
                "version": self.version,
                "total_threats": len(self.threats),
                "critical_threats": len([t for t in self.threats if t.risk_level == "Critical"]),
                "high_threats": len([t for t in self.threats if t.risk_level == "High"]),
            },
            "by_category": {
                cat.name: len(self.get_threats_by_category(cat))
                for cat in StrideCategory
            },
            "top_risks": [
                {
                    "id": t.id,
                    "title": t.title,
                    "risk_score": t.risk_score,
                    "risk_level": t.risk_level
                }
                for t in sorted(self.threats, key=lambda x: x.risk_score, reverse=True)[:10]
            ]
        }


class StrideAnalyzer:
    """Automated STRIDE analysis helper."""

    STRIDE_QUESTIONS = {
        StrideCategory.SPOOFING: [
            "Can an attacker impersonate a legitimate user?",
            "Are authentication tokens properly validated?",
            "Can session identifiers be predicted or stolen?",
            "Is multi-factor authentication available?",
        ],
        StrideCategory.TAMPERING: [
            "Can data be modified in transit?",
            "Can data be modified at rest?",
            "Are input validation controls sufficient?",
            "Can an attacker manipulate application logic?",
        ],
        StrideCategory.REPUDIATION: [
            "Are all security-relevant actions logged?",
            "Can logs be tampered with?",
            "Is there sufficient attribution for actions?",
            "Are timestamps reliable and synchronized?",
        ],
        StrideCategory.INFORMATION_DISCLOSURE: [
            "Is sensitive data encrypted at rest?",
            "Is sensitive data encrypted in transit?",
            "Can error messages reveal sensitive information?",
            "Are access controls properly enforced?",
        ],
        StrideCategory.DENIAL_OF_SERVICE: [
            "Are rate limits implemented?",
            "Can resources be exhausted by malicious input?",
            "Is there protection against amplification attacks?",
            "Are there single points of failure?",
        ],
        StrideCategory.ELEVATION_OF_PRIVILEGE: [
            "Are authorization checks performed consistently?",
            "Can users access other users' resources?",
            "Can privilege escalation occur through parameter manipulation?",
            "Is the principle of least privilege followed?",
        ],
    }

    def generate_questionnaire(self, component: str) -> List[Dict]:
        """Generate STRIDE questionnaire for a component."""
        questionnaire = []
        for category, questions in self.STRIDE_QUESTIONS.items():
            for q in questions:
                questionnaire.append({
                    "component": component,
                    "category": category.name,
                    "question": q,
                    "answer": None,
                    "notes": ""
                })
        return questionnaire

    def suggest_mitigations(self, category: StrideCategory) -> List[str]:
        """Suggest common mitigations for a STRIDE category."""
        mitigations = {
            StrideCategory.SPOOFING: [
                "Implement multi-factor authentication",
                "Use secure session management",
                "Implement account lockout policies",
                "Use cryptographically secure tokens",
                "Validate authentication at every request",
            ],
            StrideCategory.TAMPERING: [
                "Implement input validation",
                "Use parameterized queries",
                "Apply integrity checks (HMAC, signatures)",
                "Implement Content Security Policy",
                "Use immutable infrastructure",
            ],
            StrideCategory.REPUDIATION: [
                "Enable comprehensive audit logging",
                "Protect log integrity",
                "Implement digital signatures",
                "Use centralized, tamper-evident logging",
                "Maintain accurate timestamps",
            ],
            StrideCategory.INFORMATION_DISCLOSURE: [
                "Encrypt data at rest and in transit",
                "Implement proper access controls",
                "Sanitize error messages",
                "Use secure defaults",
                "Implement data classification",
            ],
            StrideCategory.DENIAL_OF_SERVICE: [
                "Implement rate limiting",
                "Use auto-scaling",
                "Deploy DDoS protection",
                "Implement circuit breakers",
                "Set resource quotas",
            ],
            StrideCategory.ELEVATION_OF_PRIVILEGE: [
                "Implement proper authorization",
                "Follow principle of least privilege",
                "Validate permissions server-side",
                "Use role-based access control",
                "Implement security boundaries",
            ],
        }
        return mitigations.get(category, [])
