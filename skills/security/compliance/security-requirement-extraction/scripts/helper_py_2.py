#!/usr/bin/env python3

from typing import Dict, List, Set

class ComplianceMapper:
    """Map security requirements to compliance frameworks."""

    FRAMEWORK_CONTROLS = {
        ComplianceFramework.PCI_DSS: {
            SecurityDomain.AUTHENTICATION: ["8.1", "8.2", "8.3"],
            SecurityDomain.AUTHORIZATION: ["7.1", "7.2"],
            SecurityDomain.DATA_PROTECTION: ["3.4", "3.5", "4.1"],
            SecurityDomain.AUDIT_LOGGING: ["10.1", "10.2", "10.3"],
            SecurityDomain.NETWORK_SECURITY: ["1.1", "1.2", "1.3"],
            SecurityDomain.CRYPTOGRAPHY: ["3.5", "3.6", "4.1"],
        },
        ComplianceFramework.HIPAA: {
            SecurityDomain.AUTHENTICATION: ["164.312(d)"],
            SecurityDomain.AUTHORIZATION: ["164.312(a)(1)"],
            SecurityDomain.DATA_PROTECTION: ["164.312(a)(2)(iv)", "164.312(e)(2)(ii)"],
            SecurityDomain.AUDIT_LOGGING: ["164.312(b)"],
        },
        ComplianceFramework.GDPR: {
            SecurityDomain.DATA_PROTECTION: ["Art. 32", "Art. 25"],
            SecurityDomain.AUDIT_LOGGING: ["Art. 30"],
            SecurityDomain.AUTHORIZATION: ["Art. 25"],
        },
        ComplianceFramework.OWASP: {
            SecurityDomain.AUTHENTICATION: ["V2.1", "V2.2", "V2.3"],
            SecurityDomain.SESSION_MANAGEMENT: ["V3.1", "V3.2", "V3.3"],
            SecurityDomain.INPUT_VALIDATION: ["V5.1", "V5.2", "V5.3"],
            SecurityDomain.CRYPTOGRAPHY: ["V6.1", "V6.2"],
            SecurityDomain.ERROR_HANDLING: ["V7.1", "V7.2"],
            SecurityDomain.DATA_PROTECTION: ["V8.1", "V8.2", "V8.3"],
            SecurityDomain.AUDIT_LOGGING: ["V7.1", "V7.2"],
        },
    }

    def map_requirement_to_compliance(
        self,
        requirement: SecurityRequirement,
        frameworks: List[ComplianceFramework]
    ) -> Dict[str, List[str]]:
        """Map a requirement to compliance controls."""
        mapping = {}
        for framework in frameworks:
            controls = self.FRAMEWORK_CONTROLS.get(framework, {})
            domain_controls = controls.get(requirement.domain, [])
            if domain_controls:
                mapping[framework.value] = domain_controls
        return mapping

    def get_requirements_for_control(
        self,
        requirement_set: RequirementSet,
        framework: ComplianceFramework,
        control_id: str
    ) -> List[SecurityRequirement]:
        """Find requirements that satisfy a compliance control."""
        matching = []
        framework_controls = self.FRAMEWORK_CONTROLS.get(framework, {})

        for domain, controls in framework_controls.items():
            if control_id in controls:
                matching.extend(requirement_set.get_by_domain(domain))

        return matching

    def generate_compliance_matrix(
        self,
        requirement_set: RequirementSet,
        frameworks: List[ComplianceFramework]
    ) -> Dict[str, Dict[str, List[str]]]:
        """Generate compliance traceability matrix."""
        matrix = {}

        for framework in frameworks:
            matrix[framework.value] = {}
            framework_controls = self.FRAMEWORK_CONTROLS.get(framework, {})

            for domain, controls in framework_controls.items():
                for control in controls:
                    reqs = self.get_requirements_for_control(
                        requirement_set, framework, control
                    )
                    if reqs:
                        matrix[framework.value][control] = [r.id for r in reqs]

        return matrix

    def gap_analysis(
        self,
        requirement_set: RequirementSet,
        framework: ComplianceFramework
    ) -> Dict[str, List[str]]:
        """Identify compliance gaps."""
        gaps = {"missing_controls": [], "weak_coverage": []}
        framework_controls = self.FRAMEWORK_CONTROLS.get(framework, {})

        for domain, controls in framework_controls.items():
            domain_reqs = requirement_set.get_by_domain(domain)
            for control in controls:
                matching = self.get_requirements_for_control(
                    requirement_set, framework, control
                )
                if not matching:
                    gaps["missing_controls"].append(f"{framework.value}:{control}")
                elif len(matching) < 2:
                    gaps["weak_coverage"].append(f"{framework.value}:{control}")

        return gaps
