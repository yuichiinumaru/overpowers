# Full-Stack Feature Workflow

End-to-end feature development using **specialized agents for each layer** of the stack.

## When to Use

- Building complete features (frontend + backend + database)
- Greenfield projects needing full stack
- Features requiring API, UI, and data layer

## Agent Assignment by Layer

| Layer | Agents | Skills |
|-------|--------|--------|
| **Database** | `database-optimizer`, `elasticsearch-specialist` | `database-optimization` |
| **Backend** | `backend-architect`, `api-documenter`, `nodejs-specialist` | `api-design` |
| **Frontend** | `frontend-developer`, `react-guru`, `vue3-specialist` | `frontend-patterns` |
| **Testing** | `test-automator`, `qa-engineer` | `testing-framework` |
| **DevOps** | `deployment-engineer`, `ci-cd-specialist` | `github-workflow-automation` |

## Workflow Steps

### 1. Feature Specification

```
/invoke product-manager

Define:
- User story
- Acceptance criteria
- Data requirements
- UI/UX expectations
```

### 2. Database Layer

```
/invoke database-optimizer

Design:
- Schema/migrations
- Indexes
- Relationships
- Seed data
```

**Deliverables:**
- [ ] Migration files
- [ ] Schema diagram
- [ ] Performance considerations

### 3. Backend API

```
/invoke backend-architect

Implement:
- API endpoints
- Business logic
- Validation
- Error handling
```

**Then:**
```
/invoke api-documenter

Document:
- OpenAPI/Swagger spec
- Request/response examples
- Authentication requirements
```

**Deliverables:**
- [ ] API routes
- [ ] Service layer
- [ ] API documentation

### 4. Frontend UI

```
/invoke frontend-developer

Build:
- Components
- State management
- API integration
- Error handling
```

**Enhance:**
```
/invoke ui-ux-designer

Polish:
- Responsive design
- Animations
- Loading states
- Empty states
```

**Deliverables:**
- [ ] UI components
- [ ] Integration with API
- [ ] Responsive layout

### 5. Testing

Run in parallel:

```
# Unit tests
/invoke test-automator
Focus: Component and function tests

# Integration tests
/invoke qa-engineer  
Focus: API and E2E tests
```

**Deliverables:**
- [ ] Unit tests (>80% coverage)
- [ ] Integration tests
- [ ] E2E happy path

### 6. CI/CD Setup

```
/invoke ci-cd-specialist

Configure:
- GitHub Actions workflow
- Test automation
- Deployment pipeline
```

**Use skill:**
```
/skill github-workflow-automation
```

### 7. Code Review

```
/invoke code-reviewer

Full stack review:
- [ ] Database efficiency
- [ ] API best practices
- [ ] Frontend patterns
- [ ] Test coverage
- [ ] Security checks
```

### 8. Deployment

```
/invoke deployment-engineer

Deploy:
- Run migrations
- Deploy backend
- Deploy frontend
- Verify health checks
```

## Layer Communication Contract

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Frontend   │────▶│   Backend   │────▶│  Database   │
│  (React/Vue)│     │  (Node/API) │     │ (Postgres)  │
└─────────────┘     └─────────────┘     └─────────────┘
      │                    │                    │
      ▼                    ▼                    ▼
   Types/Schema        OpenAPI Spec         Migrations
```

Ensure contract alignment:
- Frontend types match API responses
- API validation matches DB constraints
- Error codes consistent across layers

## Checklist Before Merge

- [ ] Database migrations work
- [ ] API passes all tests
- [ ] Frontend integrates correctly
- [ ] All tests green
- [ ] Documentation updated
- [ ] Security review passed
- [ ] Performance acceptable
