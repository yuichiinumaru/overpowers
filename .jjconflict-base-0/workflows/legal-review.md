# Legal Review Workflow

Automate legal document review using our **legal-focused skills** extracted from awesome-legal-skills.

## When to Use

- Reviewing contracts before signing
- Creating NDAs and privacy policies
- Analyzing terms of service
- Ensuring compliance

## Legal Skills Available

| Skill | Language | Purpose |
|-------|----------|---------|
| `nda-review-en-jamie-tso` | English | NDA analysis |
| `nda-review-es-javier-de-cendra` | Spanish | NDA analysis |
| `nda-review-pt-br-carlos-negrao` | Portuguese (BR) | NDA analysis |
| `nda-review-fr-claire-lavabre` | French | NDA analysis |
| `privacy-policy-fr-malik-taiar` | French | GDPR review |
| `data-processing-addendum-en-anthropic` | English | DPA review |
| `docx-processing-en-anthropic` | English | Document processing |
| `contract-clause-extraction` | English | Clause extraction |
| `employment-agreement-en-anthropic` | English | Employment contracts |

## Workflow Steps

### 1. Document Preparation

Place documents in a working directory:

```bash
mkdir -p legal-review/
cp contract.pdf legal-review/
```

### 2. Document Processing

```
/skill docx-processing-en-anthropic

Input: legal-review/contract.pdf
Output: Structured text ready for analysis
```

### 3. Clause Extraction

```
/skill contract-clause-extraction

Extract:
- Key obligations
- Liability clauses
- Termination conditions
- Payment terms
- Warranty provisions
```

### 4. Type-Specific Review

**For NDAs:**
```
/skill nda-review-en-jamie-tso

Check:
- [ ] Definition of confidential information
- [ ] Duration of obligations
- [ ] Exclusions from confidentiality
- [ ] Return/destruction of information
- [ ] Permitted disclosures
```

**For Privacy Policies:**
```
/skill privacy-policy-fr-malik-taiar

Verify:
- [ ] Data collection disclosure
- [ ] Processing purposes
- [ ] Third-party sharing
- [ ] User rights (access, deletion)
- [ ] Cookie consent
```

**For Employment:**
```
/skill employment-agreement-en-anthropic

Review:
- [ ] Compensation terms
- [ ] Non-compete clauses
- [ ] IP assignment
- [ ] Termination conditions
- [ ] Benefits
```

### 5. Risk Assessment

Generate summary with:
- Key terms extracted
- Risk items highlighted
- Suggested modifications
- Missing clauses

### 6. Multi-Language Support

For international documents, use language-specific skills:

| Language | NDA Skill |
|----------|-----------|
| English | `nda-review-en-jamie-tso` |
| Spanish | `nda-review-es-javier-de-cendra` |
| Portuguese | `nda-review-pt-br-carlos-negrao` |
| French | `nda-review-fr-claire-lavabre` |

## Output Template

```markdown
# Legal Review: [Document Name]

## Summary
Brief overview of document purpose and parties.

## Key Terms
| Term | Value |
|------|-------|
| Duration | X years |
| Jurisdiction | [State/Country] |
| Governing Law | [Law] |

## Risk Items
1. ⚠️ [High Risk] - Description
2. ⚡ [Medium Risk] - Description

## Recommendations
- [ ] Modify clause X
- [ ] Add missing clause Y
- [ ] Clarify term Z

## Approval Status
- [ ] Legal review complete
- [ ] Modifications requested
- [ ] Ready for signature
```

## Related Skills

- `web-research` - Research legal precedents
- `document-skills` - Document formatting
