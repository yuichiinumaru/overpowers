#!/bin/bash

# Generate a Paid Ads Campaign Plan template.
# Usage: ./generate_campaign_plan.sh <campaign_name>

PLAN_NAME="$1"

if [ -z "$PLAN_NAME" ]; then
  echo "Usage: $0 <campaign_name>"
  exit 1
fi

FILE_NAME="campaign_plan_${PLAN_NAME}.md"

cat <<EOF > "$FILE_NAME"
# Campaign Plan: ${PLAN_NAME}

## 1. Campaign Goals
- **Objective:** (Awareness, traffic, leads, sales, app installs)
- **Target CPA/ROAS:**
- **Budget:**
- **Constraints:**

## 2. Product & Offer
- **Promoting:**
- **Landing Page URL:**
- **Value Proposition:**
- **Promotions/Urgency:**

## 3. Audience
- **Ideal Customer:**
- **Problem Solved:**
- **Interests/Keywords:**
- **Lookalikes Available?**

## 4. Platform Selection
- [ ] Google Ads
- [ ] Meta (FB/IG)
- [ ] LinkedIn
- [ ] Twitter/X
- [ ] TikTok

## 5. Campaign Structure
**Naming Convention:** [Platform]_[Objective]_[Audience]_[Offer]_[Date]

### Campaign: [Name]
- **Ad Set 1:** [Targeting]
  - Ad 1: [Creative A]
  - Ad 2: [Creative B]
- **Ad Set 2:** [Targeting]
  - Ads...

## 6. Ad Copy (PAS/BAB Framework)
### Option 1 (PAS)
- **Problem:**
- **Agitate:**
- **Solve:**
- **CTA:**

### Option 2 (BAB)
- **Before:**
- **After:**
- **Bridge:**
- **CTA:**

## 7. Setup Checklist
- [ ] Conversion tracking tested
- [ ] Analytics linked
- [ ] Audience lists created
- [ ] Creative assets in correct sizes
- [ ] UTM parameters added

## 8. Optimization Plan (Weekly)
- [ ] Check spend vs. budget
- [ ] CPA/ROAS vs. targets
- [ ] Frequency check
- [ ] Landing page conversion rate
EOF

echo "Campaign plan template generated: $FILE_NAME"
