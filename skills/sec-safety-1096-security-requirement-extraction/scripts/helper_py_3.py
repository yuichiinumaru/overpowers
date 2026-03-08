#!/usr/bin/env python3

class SecurityUserStoryGenerator:
    """Generate security-focused user stories."""

    STORY_TEMPLATES = {
        SecurityDomain.AUTHENTICATION: {
            "as_a": "security-conscious user",
            "so_that": "my identity is protected from impersonation",
        },
        SecurityDomain.AUTHORIZATION: {
            "as_a": "system administrator",
            "so_that": "users can only access resources appropriate to their role",
        },
        SecurityDomain.DATA_PROTECTION: {
            "as_a": "data owner",
            "so_that": "my sensitive information remains confidential",
        },
        SecurityDomain.AUDIT_LOGGING: {
            "as_a": "security analyst",
            "so_that": "I can investigate security incidents",
        },
        SecurityDomain.INPUT_VALIDATION: {
            "as_a": "application developer",
            "so_that": "the system is protected from malicious input",
        },
    }

    def generate_story(self, requirement: SecurityRequirement) -> str:
        """Generate a user story from requirement."""
        template = self.STORY_TEMPLATES.get(
            requirement.domain,
            {"as_a": "user", "so_that": "the system is secure"}
        )

        story = f"""
## {requirement.id}: {requirement.title}

**User Story:**
As a {template['as_a']},
I want the system to {requirement.description.lower()},
So that {template['so_that']}.

**Priority:** {requirement.priority.name}
**Type:** {requirement.req_type.value}
**Domain:** {requirement.domain.value}

**Acceptance Criteria:**
{self._format_acceptance_criteria(requirement.acceptance_criteria)}

**Definition of Done:**
- [ ] Implementation complete
- [ ] Security tests pass
- [ ] Code review complete
- [ ] Security review approved
- [ ] Documentation updated

**Security Test Cases:**
{self._format_test_cases(requirement.test_cases)}

**Traceability:**
- Threats: {', '.join(requirement.threat_refs) or 'N/A'}
- Compliance: {', '.join(requirement.compliance_refs) or 'N/A'}
"""
        return story

    def _format_acceptance_criteria(self, criteria: List[str]) -> str:
        return "\n".join(f"- [ ] {c}" for c in criteria) if criteria else "- [ ] TBD"

    def _format_test_cases(self, tests: List[str]) -> str:
        return "\n".join(f"- {t}" for t in tests) if tests else "- TBD"

    def generate_epic(
        self,
        requirement_set: RequirementSet,
        domain: SecurityDomain
    ) -> str:
        """Generate an epic for a security domain."""
        reqs = requirement_set.get_by_domain(domain)

        epic = f"""
# Security Epic: {domain.value.replace('_', ' ').title()}

## Overview
This epic covers all security requirements related to {domain.value.replace('_', ' ')}.

## Business Value
- Protect against {domain.value.replace('_', ' ')} related threats
- Meet compliance requirements
- Reduce security risk

## Stories in this Epic
{chr(10).join(f'- [{r.id}] {r.title}' for r in reqs)}

## Acceptance Criteria
- All stories complete
- Security tests passing
- Security review approved
- Compliance requirements met

## Risk if Not Implemented
- Vulnerability to {domain.value.replace('_', ' ')} attacks
- Compliance violations
- Potential data breach

## Dependencies
{chr(10).join(f'- {d}' for r in reqs for d in r.dependencies) or '- None identified'}
"""
        return epic
