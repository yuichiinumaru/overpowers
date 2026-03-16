---
name: company-search-kimi
description: Multi-source company research tool generating structured reports with "Tianyancha/Qichacha-level information granularity". Uses kimi_search + kimi_fetch for real-time public web retrieval without relying on fragile site scrapers.
tags: [company-research, kimi, due-diligence, business-intelligence, search]
version: "1.0.0"
---

# Company Research V2 Skill

Multi-source company research tool generating "Tianyancha/Qichacha-level information granularity" structured reports.
Does not rely on fragile site scrapers: uses kimi_search + kimi_fetch for real-time public web/announcement/news/regulatory disclosure retrieval and deep-dive,
performing: entity disambiguation → cross-validation → structured summarization → risk annotation.

---

## ✅ When to Use

Use when user needs any of the following tasks:
- Company search / company research / company background / due diligence framework
- Business registration info (establishment, registered capital, legal representative, shareholders, changes, etc.)
- Equity structure / penetration equity / ultimate beneficial owner (if inferable from public sources)
- External investment / branches / subsidiary structure
- Financing history / investors / valuation (based on announcements, media, registration changes as evidence)
- Judicial risk / enforcement / dishonesty / court hearings / judgment documents
- Business risk (administrative penalties, abnormal operations, serious violations, tax/environmental/safety public disclosures)
- Intellectual property (trademarks, patents, copyrights)
- Bidding / government procurement / major contracts (public platforms)
- Employment and public opinion (recruitment profiles, media reports, negative sentiment)
- Competitor and industry position analysis

---

## 🧰 Tools Required

- kimi_search (multi-source search: news/announcements/regulatory/encyclopedia/recruitment/bidding/judicial public, etc.)
- kimi_fetch (grab key page full text for detail verification and field extraction)
- (optional) web_search / web_fetch as fallback (when kimi results are insufficient or international info needed)

---

## 🎯 Output Standard

1) Use "Tianyancha/Qichacha common modules" as framework, output structured report
2) Each key conclusion should have "at least two source cross-validations" where possible
3) Annotate all key information with:
- **Source URL/title**
- **Crawl date**
- **Consistency (multi-source consistent/single source)**
- **Confidence level (A/B/C)**
4) Clearly state: public search ≠ paid database full data; mark fields that cannot be obtained as "not found/suspected paid-only/internal channel required".

---

## 🧭 Workflow

### Step 0 — Entity Recognition & Disambiguation (Mandatory)
Objective: Confirm which entity user wants to research, avoid confusion with same-name companies.

**Actions:**
- Use kimi_search to simultaneously search:
  - Company full name / abbreviation / brand name
  - Possible entities: XX Co., Ltd., XX Technology, XX Network, XX Transport
  - "Unified social credit code/registration number/legal representative/headquarters city" keywords

**Output:**
- Provide "candidate entity list" (max 5), select "Primary Entity"
- Annotate selection basis (e.g.: official website filing, registration entry, media consistent mention)

> If unique disambiguation is impossible: report can still be output, but add prominent notice: entity has ambiguity, conclusions only valid for candidate set.

---

### Step 1 — Search Phase (Coverage Dimensions)
Use kimi_search to search by module, recommended at least 3-5 results per module:

#### 1) Business Registration & Entity Info
- Company full name/abbreviation/former names
- Unified social credit code (if publicly visible)
- Establishment date, registered capital, paid-in capital (if publicly visible)
- Legal representative, key personnel (directors/supisors/executives public info)
- Registration status (active/dissolved/revoked, etc.)
- Registration authority, approval date
- Registered address/office address (public disclosure)
- Business scope (based on registration/announcements)

#### 2) Equity Structure & Control (Benchmark Tianyancha/Qichacha)
- Shareholder list, shareholding ratio (public disclosure)
- Capital contribution method/subscription-actual payment changes (registration changes/announcements)
- Controlling shareholder, actual controller (infer if possible)
- Penetration path (only based on publicly verifiable sources)

#### 3) External Investment/Branches/Subsidiaries
- External investment company list (public sources)
- Branches/offices (if public)
- Key related companies (same legal rep/same address/same brand)

#### 4) Registration Changes & Major Events Timeline
- Legal rep/shareholder/registered capital/address/business scope changes
- Name changes (former names)
- Equity pledges, chattel mortgages (if publicly retrievable)

#### 5) Financing & Capital Operations
- Financing rounds, dates, amounts, investors (cross-validate with announcements/authoritative media/registration changes)
- M&A/restructuring/equity transfers
- If listed company related: announcements, annual reports, investor relations materials

#### 6) Judicial Risk (Benchmark "Judicial Risk" Module)
- Judgment documents (cause of action, role: plaintiff/defendant, key points)
- Court hearing announcements
- Enforced execution/restriction of high consumption
- Dishonest judgment debtors (if public)
- Key: filter "strongly related to main business/large amount/high frequency" cases

#### 7) Business Risk (Benchmark "Business Risk/Abnormal Operations/Serious Violations")
- Administrative penalties (market regulation, transport, tax, environmental protection, cyberspace, etc. public disclosure)
- Abnormal operations list/serious violations (if publicly retrievable)
- Spot inspection results (if public)
- Work safety/environmental protection/data compliance related penalties (if any)

#### 8) Intellectual Property & Qualifications (Benchmark "IP/Qualification Certificates")
- Trademarks (core brands, categories)
- Patents (invention/utility model/design)
- Software copyrights
- Industry qualifications (e.g.: transport permit, value-added telecom license, payment/small loan license, etc. - expand by industry)

#### 9) Bidding/Government Procurement/Major Cooperation
- Bidding award announcements
- Government procurement contracts
- Key partner disclosures (announcements/news/official website)

#### 10) Recruitment & Organizational Profile (Benchmark "Recruitment Info/Company Size")
- Recruitment platform job types, tech stack, city distribution
- Salary range (if public)
- Organizational capability inference: R&D/operations/sales/risk control/compliance, etc. emphasis

#### 11) Public Opinion & News (Benchmark "News Updates")
- Key news in last 3/6/12 months
- Negative sentiment: complaints, regulatory naming, major accidents, data breaches, etc.
- Annotate each news item: source level (official/authoritative media/self-media) and confidence

#### 12) Competitive Landscape & Industry Position
- Competitor list (direct competitors/substitutes/upstream-downstream)
- Market share (do not fabricate if no authoritative data)
- Differentiation points: pricing, channels, compliance qualifications, technical barriers

---

### Step 2 — Deep Retrieval (kimi_fetch Key Pages)
Must fetch the following "high-value evidence pages":
- Official website/official announcements/regulatory notices
- Listed company annual reports/announcements (if related)
- Judgment/enforcement info detail pages (grab if accessible)
- Registration change detail pages (if publicly visible)
- Bidding award announcement full text

Grab objective: extract key fields, not just cite snippets.

---

### Step 3 — Organize Output (Structured Report + Evidence Chain)
Report must have two layers:
1) **Conclusion Layer (for business/investment committee/boss)**
2) **Evidence Layer (for due diligence/legal/analyst review)**

---

## Output Format (Only Output Below Content)

```markdown
## 🔍 {Company Name} Company Research Report

- Report generation time: {YYYY-MM-DD}
- Entity scope: {Primary Entity full name + region + unified social credit code (if public)}
- Data sources: public web multi-source retrieval (not paid database direct connection), key conclusions cross-validated where possible

---

### 0️⃣ Research Subject
- Candidate entities:
  - A: xxx (basis: ...)
  - B: xxx (basis: ...)
- This report selects primary entity: xxx
- Remaining doubts: xxx (if any)

---

### 1️⃣ Basic Info

| Item | Content | Confidence | Evidence |
|------|------|--------|------|
| Company Full Name | xxx | A | [Source1] |
| Former Names | xxx | B | [Source2] |
| Establishment Date | xxx | A | [Source] |
| Registered Capital | xxx | B | [Source] |
| Paid-in Capital | xxx/Not disclosed | C | [Source] |
| Legal Representative | xxx | A | [Source] |
| Registration Status | Active/Dissolved... | A | [Source] |
| Unified Social Credit Code | xxx/Not disclosed | B/C | [Source] |
| Registered Address | xxx | B | [Source] |
| HQ/Office Location (inferred) | xxx | C | [Source] |
| Industry/Business Tags | xxx | B | [Source] |
| Business Scope Summary | xxx | B | [Source] |

---

### 2️⃣ Equity Structure & Control
#### 2.1 Shareholder Structure (Visible Scope)
| Shareholder | Shareholding % | Change Record | Confidence | Evidence |
|------|----------|----------|--------|------|
| xxx | xx% | xxxx | B | [Source] |

#### 2.2 Controlling/Actual Control & Penetration (Based on Verifiable Public Links Only)
- Controlling shareholder: xxx (basis: ...)
- Actual controller: xxx (basis: ...)
- Penetration path (if applicable): A → B → C

> Note: If no reliable penetration link found, clearly mark "Public info insufficient, cannot confirm ultimate beneficial owner".

---

### 3️⃣ External Investment / Subsidiaries / Branches
- Key subsidiaries (Top N):
  - xxx (role/business: ..., region: ...)
- External investment summary:
  - Investment target, ratio, date (if public)
- Related entity hints:
  - Same legal rep/same address/same brand, etc. clues (use caution)

---

### 4️⃣ Registration Changes & Milestone Timeline
| Date | Event | Impact Interpretation | Confidence | Evidence |
|------|------|----------|--------|------|
| YYYY-MM | Legal rep change | ... | B | [Source] |

---

### 5️⃣ Financing & Capital Operations
| Date | Round/Event | Amount | Investors/Counterparty | Confidence | Evidence |
|------|-----------|------|----------------|--------|------|
| YYYY-MM | Series A | xx | xxx | B | [Source] |

- Financing confidence rules:
  - A: Official announcements/regulatory exchange listed company announcements
  - B: Authoritative financial media multi-source consistent
  - C: Single media or self-media (clues only)

---

### 6️⃣ Judicial Risk (Litigation/Enforcement/Dishonesty)
#### 6.1 Risk Overview
- Judgment documents: x cases (visible scope)
- Enforced execution: x entries (visible scope)
- Dishonesty: x entries (visible scope)
- Court hearings: x entries (visible scope)

#### 6.2 Key Cases (Large Amount/High Frequency/Strongly Related to Main Business)
| Case No./Date | Cause | Role | Result/Progress | Amount | Risk Interpretation | Evidence |
|----------|------|------|-----------|------|----------|------|
| xxx | xxx | Defendant | xxx | xx | xxx | [Source] |

---

### 7️⃣ Business Risk (Administrative Penalties/Abnormal/Compliance)
| Type | Event | Date | Authority/Platform | Risk Level | Evidence |
|------|------|------|---------------|----------|------|
| Administrative Penalty | xxx | YYYY-MM | xxx | Medium/High | [Source] |

- Abnormal Operations/Serious Violations: {Yes/No/Not Found}

---

### 8️⃣ Intellectual Property & Qualifications
- Trademarks: core brands/categories/status (if public)
- Patents: count/type/key patents (if public)
- Software copyrights: representative entries (if public)
- Industry qualifications: business-strong related certificates (if public)

---

### 9️⃣ Bidding / Government Procurement / Major Cooperation
| Date | Project | Client/Procurer | Amount | Confidence | Evidence |
|------|------|-------------|------|--------|------|
| YYYY | xxx | xxx | xx | B | [Source] |

---

### 🔟 Recruitment & Organizational Profile (Auxiliary Business Focus Judgment)
- Recruitment city distribution: ...
- Job structure: R&D/product/operations/sales/compliance/risk control ratio clues
- Tech stack clues: ...

---

### 1️⃣1️⃣ Latest Updates (Last 3/6/12 Months)
| Date | Event | Impact Judgment | Confidence | Evidence |
|------|------|----------|--------|------|
| YYYY-MM-DD | xxx | xxx | B | [Source] |

---

### 1️⃣2️⃣ Industry Position / Competitive Landscape
- Industry positioning: ...
- Direct competitors: A/B/C
- Substitutes/upstream-downstream: ...
- Differentiation & barriers: ...

---

## ⚠️ Risk Notice (Important)
- This report is based on publicly retrieved information, not equivalent to Tianyancha/Qichacha paid database full fields.
- Equity penetration, actual payment, historical changes, full judicial records, etc. may have "publicly invisible/paid/internal channel required" gaps.
- Single-source information (especially self-media/forums) is clues only, not factual conclusions.
- If entity has same-name/multi-brand/multi-entity operations, further confirm unified social credit code scope.

---

## ✅ Summary (Executive Summary)
- One sentence summary: ...
- Core conclusions 3-5 items:
  1) ...
  2) ...
  3) ...
- Main risks 3-5 items:
  1) ...
  2) ...
  3) ...



## **🔎 Search Playbook (Recommended Search Query Templates)**

> Use "company name/primary entity full name + keywords" combination search for each module, prioritize authoritative sources.

- Business basics: {company} unified social credit code registered capital legal representative establishment date
- Shareholder equity: {company} shareholder shareholding ratio registration changes capital contribution
- Subsidiary investment: {company} external investment subsidiaries branches related companies
- Registration changes: {company} changes legal rep changes registered capital changes address changes former names
- Financing: {company} financing Series A investors amount valuation
- Judicial: {company} judgment documents case number enforced execution restriction of high consumption dishonesty
- Administrative penalty/abnormal: {company} administrative penalty abnormal operations serious violations regulatory bulletin
- IP: {company} trademark patent software copyright
- Bidding: {company} award announcement government procurement contract
- Recruitment: {company} recruitment job positions salary tech stack
- Public opinion: {company} complaints negative accidents rights defense regulation


## **🧪 Evidence & Confidence Rules (Mandatory Compliance)**


- Confidence A: Government/court/regulatory/exchange announcements, listed company annual report announcements, company official announcements
- Confidence B: Authoritative media/industry association reports, multi-source consistent
- Confidence C: Single media, self-media, forums, clues only
-

Cross-validation priority:

A(Official) > B(Authoritative Media Multi-source) > C(Clues)

## **🧩 Notes**

- No site scraping, no login/paywall bypass, no attempt to access non-public data.
- If user explicitly requests "benchmark Tianyancha fields", can output "field gap list" and explain why gaps exist (publicly unavailable/paid/internal network/offline required).
- For brand-type companies (multi-entity operations), must prioritize "brand-entity mapping relationship" as first-priority conclusion.
- No need to provide investigation steps, only provide final report.
