---
name: frontend-performance
description: "Analyzes and improves frontend performance: LCP, FCP, CLS, bundle size, lazy loading, and runtime efficiency. Use when 性能优化, 首屏慢, 卡顿, 打包体积, performance optimization, or improving Core Web Vitals."
metadata:
  openclaw:
    category: "performance"
    tags: ['performance', 'analysis', 'development']
    version: "1.0.0"
---

# Frontend Performance Optimization

Focusing on loading performance and runtime performance, provide implementable optimization solutions and priorities.

## Trigger Scenarios

- Users say "performance optimization," "slow first screen," "page lag," "large bundle size," "poor LCP/FCP."
- Provide Lighthouse reports, Performance recordings, or specific slow pages/operations.

## Analysis Dimensions

### 1. Loading Performance (LCP / FCP / TTI)

| Problem | Common Causes | Optimization Direction |
|------|----------|----------|
| Slow LCP | Large images, render-blocking resources, slow server | Image optimization, prioritize critical resources, SSR/prefetch |
| Slow FCP | JS/CSS blocking, multiple dependencies for the first screen | Code splitting, inline critical CSS, defer non-critical |
| Long TTI | Main thread long tasks, large bundles | Code splitting, lazy loading, reduce main thread work |

### 2. Experience Stability (CLS / Jank)

| Problem | Common Causes | Optimization Direction |
|------|----------|----------|
| High CLS | Images/fonts without dimensions, dynamically inserted content | Aspect ratio/dimensions, `font-display`, reserve placeholders |
| Scrolling/Operation Jank | Excessive reflows, long tasks, large lists | Virtual lists, debouncing/throttling, `requestAnimationFrame`, reduce reflow |

### 3. Resources & Bundling

| Problem | Optimization Direction |
|------|----------|
| Large JS size | Split by route/on-demand, tree-shaking, replace large dependencies, analyze bundle |
| Large Images | Format (WebP/AVIF), dimensions, lazy loading, CDN |
| Many Requests | Merging, caching strategies, preconnect/preload |

## Execution Flow

### 1. Quantify Current State

- If Lighthouse is available: Record LCP/FCP/CLS/TTI and Speed Index.
- If specific slow operations exist: Describe the operation + subjective time or Performance recording duration.
- If there are bundle size concerns: Provide the current main chunk sizes.

### 2. Identify Bottlenecks

- Loading: Use Network waterfall chart to see which requests are blocking or too large.
- Runtime: Use Performance recordings to identify long tasks, layout/style calculations.
- Bundling: Use analysis tools (e.g., `@next/bundle-analyzer`) to inspect large modules.

### 3. List Solutions and Assign Cost-Effectiveness

For each solution, note:
- **Benefit**: Expected improvement in metrics or user experience.
- **Cost**: Amount of change, risks, dependencies.
- **Priority**: High/Medium/Low (prioritize high benefit, low cost).

### 4. Determine Implementation Order

- Start with "quick wins": e.g., image dimensions, `font-display`, critical CSS, first screen lazy loading.
- Then implement "medium changes": e.g., route-level code splitting, virtual lists, caching strategies.
- Finally, consider "major changes": e.g., architectural adjustments, SSR, edge rendering.

## Output Template

```markdown
## Performance Optimization Report

### Current State
- Metrics or Phenomena: ...
- Main Bottlenecks: ...

### Optimization Solutions (by Priority)
| Solution | Benefit | Cost | Priority |
|------|------|------|--------|
| 1. ... | ... | ... | High/Medium/Low |
| 2. ... | ... | ... | ... |

### Recommended Implementation Order
1. ...
2. ...

### Verification Methods
- After optimization, it is recommended to re-test: Lighthouse, Performance, key operation timings.
```

## Project Specifics

- Next.js: Use `dynamic` for lazy loading, Image component, analyze with `next/bundle-analyzer`.
- React: Avoid creating new objects/functions within render that cause unnecessary re-renders of child components; use `memo`/`useMemo`/`useCallback` when necessary.
- Long Lists: Prioritize virtual scrolling (e.g., `react-window`, `tanstack-virtual`) before considering pagination.
