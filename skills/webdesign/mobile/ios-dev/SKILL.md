---
name: ios-dev
description: "General iOS App development, build, signing, testing, and App Store submission process (China region) guide. Used when users ask about iOS development/submission/review/signing/TestFlight/App Store Connect/privacy compliance/subscription configuration, or when the trigger word iosdev is entered."
metadata:
  openclaw:
    category: "development"
    tags: ['development', 'devops', 'tools']
    version: "1.0.0"
---

# iOS Development and Publishing Skills (China)

## Quick Start
- First, confirm: App type (Individual/Enterprise), target region (China), minimum iOS version, whether it includes subscriptions/logins/UGC.
- If only a process checklist is needed, output the six steps: "Development → Build → Sign → Upload → Review → Release".
- When details are needed, load the corresponding file from `references` on demand.

## Workflow (Recommended Output Structure)
1. Requirement and Constraint Confirmation (Bundle ID, Team, Minimum iOS, Feature Sensitivity)
2. Development and Build Preparation (Dependency Management, Configuration, Version Number)
3. Signing and Archiving (Certificates, Provisioning, Archive)
4. Testing and Verification (Physical Device, Crashes, Feature Checklist)
5. App Store Connect Preparation (Metadata, Screenshots, Privacy Policy)
6. Submission for Review and Follow-up (Review Notes, Rejection Handling, Version Iteration)

## Reference Loading Guide
- Build/Signing/Dependencies and Version Number → `references/ios-development.md`
- App Store Release Process (China) → `references/app-store-release-cn.md`
- IAP/Subscription Configuration and Testing → `references/iap-subscription.md`
- Privacy, ATS, Security, and Compliance → `references/privacy-security.md`

## Output Constraints
- Output only the general process, do not reference project-specific private information.
- Avoid providing real keys or accounts; use placeholders.
- When referencing official links, prioritize Apple Developer / App Store Review Guidelines.
