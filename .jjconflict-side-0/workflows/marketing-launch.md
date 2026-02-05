# Marketing Launch Workflow

Coordinate a product launch using our **marketing and growth agents** alongside technical deployment.

## When to Use

- New product/feature launches
- Major updates requiring announcement
- Open-source project releases
- SaaS feature rollouts

## Marketing Agent Team

| Agent | Role |
|-------|------|
| `growth-hacker` | Growth strategy & experiments |
| `app-store-optimizer` | ASO for mobile apps |
| `tiktok-strategist` | Short-form video strategy |
| `reddit-community-builder` | Community engagement |
| `visual-storyteller` | Visual content creation |
| `whimsy-injector` | Memorable messaging |

## Workflow Steps

### 1. Launch Planning

```
/invoke growth-hacker

Define:
- Target audience segments
- Key messaging
- Launch timeline
- Success metrics (KPIs)
```

### 2. Content Preparation

**Visual Assets:**
```
/invoke visual-storyteller

Create:
- Hero images
- Feature screenshots
- Demo GIFs
- Social media graphics
```

**Messaging:**
```
/invoke whimsy-injector

Make memorable:
- Taglines
- Feature descriptions  
- Social posts
- Email subject lines
```

### 3. Platform-Specific Strategy

**For Mobile Apps:**
```
/invoke app-store-optimizer

Optimize:
- App store listing
- Keywords
- Screenshots
- Description
```

**For Social Launch:**
```
/invoke tiktok-strategist

Plan:
- Demo video content
- Trending hooks
- Hashtag strategy
```

**For Community Building:**
```
/invoke reddit-community-builder

Prepare:
- Launch announcement post
- FAQ responses
- Community guidelines
```

### 4. Technical Deployment

```
/invoke deployment-engineer

Checklist:
- [ ] Production deploy ready
- [ ] Feature flags configured
- [ ] Monitoring enabled
- [ ] Rollback plan ready
```

Run deployment scripts:
```bash
./scripts/cloudflare-cli.sh deploy
./scripts/vercel-cli.sh deploy --prod
```

### 5. Launch Execution

**Day-of Checklist:**
- [ ] Deploy to production
- [ ] Publish blog post
- [ ] Send email announcement
- [ ] Post on social platforms
- [ ] Submit to directories
- [ ] Engage with early feedback

### 6. Post-Launch Monitoring

```
/invoke feedback-synthesizer

Monitor:
- User feedback
- Social mentions
- Bug reports
- Feature requests
```

## Related Services

| Service | Config File |
|---------|-------------|
| Cloudflare | `services/hosting/cloudflare.md` |
| Vercel | `services/hosting/vercel.md` |
| AWS SES | `services/email/ses.md` |

## Related Skills

- `competitive-ads-extractor` - Competitor analysis
- `artifacts-builder` - Create launch artifacts
- `github-workflow-automation` - Automate releases

## Launch Metrics Template

| Metric | Day 1 | Week 1 | Month 1 |
|--------|-------|--------|---------|
| Signups | | | |
| Active Users | | | |
| Social Mentions | | | |
| NPS Score | | | |
