#!/usr/bin/env python3

from dataclasses import dataclass
from typing import List, Dict, Tuple

@dataclass
class ThreatInput:
    id: str
    category: str  # STRIDE category
    title: str
    description: str
    target: str
    impact: str
    likelihood: str


class RequirementExtractor:
    """Extract security requirements from threats."""

    # Mapping of STRIDE categories to security domains and requirement patterns
    STRIDE_MAPPINGS = {
        "SPOOFING": {
            "domains": [SecurityDomain.AUTHENTICATION, SecurityDomain.SESSION_MANAGEMENT],
            "patterns": [
                ("Implement strong authentication for {target}",
                 "Ensure {target} authenticates all users before granting access"),
                ("Validate identity tokens for {target}",
                 "All authentication tokens must be cryptographically verified"),
                ("Implement session management for {target}",
                 "Sessions must be securely managed with proper expiration"),
            ]
        },
        "TAMPERING": {
            "domains": [SecurityDomain.INPUT_VALIDATION, SecurityDomain.DATA_PROTECTION],
            "patterns": [
                ("Validate all input to {target}",
                 "All input must be validated against expected formats"),
                ("Implement integrity checks for {target}",
                 "Data integrity must be verified using cryptographic signatures"),
                ("Protect {target} from modification",
                 "Implement controls to prevent unauthorized data modification"),
            ]
        },
        "REPUDIATION": {
            "domains": [SecurityDomain.AUDIT_LOGGING],
            "patterns": [
                ("Log all security events for {target}",
                 "Security-relevant events must be logged for audit purposes"),
                ("Implement non-repudiation for {target}",
                 "Critical actions must have cryptographic proof of origin"),
                ("Protect audit logs for {target}",
                 "Audit logs must be tamper-evident and protected"),
            ]
        },
        "INFORMATION_DISCLOSURE": {
            "domains": [SecurityDomain.DATA_PROTECTION, SecurityDomain.CRYPTOGRAPHY],
            "patterns": [
                ("Encrypt sensitive data in {target}",
                 "Sensitive data must be encrypted at rest and in transit"),
                ("Implement access controls for {target}",
                 "Data access must be restricted based on need-to-know"),
                ("Prevent information leakage from {target}",
                 "Error messages and logs must not expose sensitive information"),
            ]
        },
        "DENIAL_OF_SERVICE": {
            "domains": [SecurityDomain.AVAILABILITY, SecurityDomain.INPUT_VALIDATION],
            "patterns": [
                ("Implement rate limiting for {target}",
                 "Requests must be rate-limited to prevent resource exhaustion"),
                ("Ensure availability of {target}",
                 "System must remain available under high load conditions"),
                ("Implement resource quotas for {target}",
                 "Resource consumption must be bounded and monitored"),
            ]
        },
        "ELEVATION_OF_PRIVILEGE": {
            "domains": [SecurityDomain.AUTHORIZATION],
            "patterns": [
                ("Enforce authorization for {target}",
                 "All actions must be authorized based on user permissions"),
                ("Implement least privilege for {target}",
                 "Users must only have minimum necessary permissions"),
                ("Validate permissions for {target}",
                 "Permission checks must be performed server-side"),
            ]
        },
    }

    def extract_requirements(
        self,
        threats: List[ThreatInput],
        project_name: str
    ) -> RequirementSet:
        """Extract security requirements from threats."""
        req_set = RequirementSet(
            name=f"{project_name} Security Requirements",
            version="1.0"
        )

        req_counter = 1
        for threat in threats:
            reqs = self._threat_to_requirements(threat, req_counter)
            for req in reqs:
                req_set.add(req)
            req_counter += len(reqs)

        return req_set

    def _threat_to_requirements(
        self,
        threat: ThreatInput,
        start_id: int
    ) -> List[SecurityRequirement]:
        """Convert a single threat to requirements."""
        requirements = []
        mapping = self.STRIDE_MAPPINGS.get(threat.category, {})
        domains = mapping.get("domains", [])
        patterns = mapping.get("patterns", [])

        priority = self._calculate_priority(threat.impact, threat.likelihood)

        for i, (title_pattern, desc_pattern) in enumerate(patterns):
            req = SecurityRequirement(
                id=f"SR-{start_id + i:03d}",
                title=title_pattern.format(target=threat.target),
                description=desc_pattern.format(target=threat.target),
                req_type=RequirementType.FUNCTIONAL,
                domain=domains[i % len(domains)] if domains else SecurityDomain.DATA_PROTECTION,
                priority=priority,
                rationale=f"Mitigates threat: {threat.title}",
                threat_refs=[threat.id],
                acceptance_criteria=self._generate_acceptance_criteria(
                    threat.category, threat.target
                ),
                test_cases=self._generate_test_cases(
                    threat.category, threat.target
                )
            )
            requirements.append(req)

        return requirements

    def _calculate_priority(self, impact: str, likelihood: str) -> Priority:
        """Calculate requirement priority from threat attributes."""
        score_map = {"LOW": 1, "MEDIUM": 2, "HIGH": 3, "CRITICAL": 4}
        impact_score = score_map.get(impact.upper(), 2)
        likelihood_score = score_map.get(likelihood.upper(), 2)

        combined = impact_score * likelihood_score

        if combined >= 12:
            return Priority.CRITICAL
        elif combined >= 6:
            return Priority.HIGH
        elif combined >= 3:
            return Priority.MEDIUM
        return Priority.LOW

    def _generate_acceptance_criteria(
        self,
        category: str,
        target: str
    ) -> List[str]:
        """Generate acceptance criteria for requirement."""
        criteria_templates = {
            "SPOOFING": [
                f"Users must authenticate before accessing {target}",
                "Authentication failures are logged and monitored",
                "Multi-factor authentication is available for sensitive operations",
            ],
            "TAMPERING": [
                f"All input to {target} is validated",
                "Data integrity is verified before processing",
                "Modification attempts trigger alerts",
            ],
            "REPUDIATION": [
                f"All actions on {target} are logged with user identity",
                "Logs cannot be modified by regular users",
                "Log retention meets compliance requirements",
            ],
            "INFORMATION_DISCLOSURE": [
                f"Sensitive data in {target} is encrypted",
                "Access to sensitive data is logged",
                "Error messages do not reveal sensitive information",
            ],
            "DENIAL_OF_SERVICE": [
                f"Rate limiting is enforced on {target}",
                "System degrades gracefully under load",
                "Resource exhaustion triggers alerts",
            ],
            "ELEVATION_OF_PRIVILEGE": [
                f"Authorization is checked for all {target} operations",
                "Users cannot access resources beyond their permissions",
                "Privilege changes are logged and monitored",
            ],
        }
        return criteria_templates.get(category, [])

    def _generate_test_cases(
        self,
        category: str,
        target: str
    ) -> List[str]:
        """Generate test cases for requirement."""
        test_templates = {
            "SPOOFING": [
                f"Test: Unauthenticated access to {target} is denied",
                "Test: Invalid credentials are rejected",
                "Test: Session tokens cannot be forged",
            ],
            "TAMPERING": [
                f"Test: Invalid input to {target} is rejected",
                "Test: Tampered data is detected and rejected",
                "Test: SQL injection attempts are blocked",
            ],
            "REPUDIATION": [
                "Test: Security events are logged",
                "Test: Logs include sufficient detail for forensics",
                "Test: Log integrity is protected",
            ],
            "INFORMATION_DISCLOSURE": [
                f"Test: {target} data is encrypted in transit",
                f"Test: {target} data is encrypted at rest",
                "Test: Error messages are sanitized",
            ],
            "DENIAL_OF_SERVICE": [
                f"Test: Rate limiting on {target} works correctly",
                "Test: System handles burst traffic gracefully",
                "Test: Resource limits are enforced",
            ],
            "ELEVATION_OF_PRIVILEGE": [
                f"Test: Unauthorized access to {target} is denied",
                "Test: Privilege escalation attempts are blocked",
                "Test: IDOR vulnerabilities are not present",
            ],
        }
        return test_templates.get(category, [])
