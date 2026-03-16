---
name: fullstack-dev-engineer
description: "Provides full-stack development architecture design, technology stack selection, front-end development, back-end development, and operation and deployment guidance; used when users need consultation on architecture design, technology selection, front-end development, back-end development, operation and deployment, or best practices."
metadata:
  openclaw:
    category: "development"
    tags: ['development', 'devops', 'tools']
    version: "1.0.0"
---

# Full-Stack All-Round Development Engineer

## Task Objectives
- This Skill is used to: Assist users in completing full-stack development tasks from architecture design, front-end development, back-end development, to operations and deployment.
- Capabilities include: System architecture design, technology stack selection, front-end development, back-end development, project planning, code generation, operations and deployment, best practice guidance.
- Trigger conditions: Users need to design system architecture, select technical solutions, develop front-end/back-end projects, deploy applications, generate code, or consult on development best practices.

## Prerequisites
This Skill requires no additional dependencies; all capabilities are realized through the agent's language understanding and code generation abilities.

## Operation Steps

### 1. Requirements Analysis
- Understand user business requirements and functional requirements.
- Clarify system non-functional requirements (performance, scalability, security, maintainability).
- Identify technical constraints and environmental limitations (deployment environment, team skills, budget).

### 2. Architecture Design
- Reference Architecture Patterns: Consult [architecture-patterns.md](references/architecture-patterns.md) to select appropriate architecture patterns.
- Design system module division and component relationships.
- Clarify data flow and interface design.
- Generate architecture design documents and architecture diagram descriptions.

### 3. Technology Stack Selection
- Reference Technology Comparison: Consult [tech-stack-comparison.md](references/tech-stack-comparison.md) for technology stack comparison.
- Select suitable front-end, back-end, database, and middleware based on project requirements.
- Consider technology maturity, community activity, learning curve, and team fit.
- Provide technology selection explanations and alternative solutions.

### 4. Project Planning
- Develop development plans and milestones.
- Design project directory structure.
- Plan development environment and deployment process.
- Define code standards and collaboration workflows.

### 5. Code Implementation
- Reference Best Practices: Consult [best-practices.md](references/best-practices.md) to follow development best practices.
- Reference Code Standards: Consult [code-standards.md](references/code-standards.md) to maintain code quality.
- Generate module code and core functionality implementation.
- Write unit tests and integration tests.
- Generate API documentation and usage instructions.

### 6. Front-end Development
- Reference Front-end Guide: Consult [frontend-guide.md](references/frontend-guide.md) to understand front-end development practices.
- Select front-end technology stack (React/Vue/Angular).
- Design component architecture and state management solutions.
- Implement responsive layouts and interactive features.
- Optimize front-end performance and user experience.
- Write front-end tests (unit tests, E2E tests).

### 7. Operations and Deployment
- Reference Operations Guide: Consult [devops-guide.md](references/devops-guide.md) to understand operations practices.
- Configure containerized environment (Docker/Kubernetes).
- Design CI/CD pipelines.
- Configure monitoring and alerting systems.
- Set up log collection and analysis.
- Develop backup and disaster recovery plans.
- Implement security hardening measures.

### 8. Delivery and Optimization
- Code review and optimization suggestions.
- Performance optimization and security hardening.
- Deployment documentation and operations guides.
- Subsequent iteration and maintenance suggestions.

## Resource Index
- Architecture Pattern Reference: [architecture-patterns.md](references/architecture-patterns.md) (Refer to when designing system architecture)
- Technology Stack Comparison: [tech-stack-comparison.md](references/tech-stack-comparison.md) (Refer to when selecting technical solutions)
- Front-end Development Guide: [frontend-guide.md](references/frontend-guide.md) (Refer to during front-end development)
- Operations Practice Guide: [devops-guide.md](references/devops-guide.md) (Refer to during operations and deployment)
- Best Practices: [best-practices.md](references/best-practices.md) (Refer to during development)
- Code Standards: [code-standards.md](references/code-standards.md) (Refer to when writing code)

## Notes
- Make full use of the agent's code understanding and generation capabilities, and avoid writing scripts for simple tasks.
- Prioritize mature, stable technology stacks with good community support.
- Balance current needs and future scalability during architecture design.
- Generated code should adhere to principles of clarity, maintainability, and testability.
- Adjust design complexity based on the actual complexity of the project to avoid over-engineering.

## Usage Examples

### Example 1: Design E-commerce Platform Architecture
**Function Description**: Design an overall architecture solution for a small to medium-sized e-commerce platform.
**Execution Method**: The agent provides design guidance based on architecture pattern references.
**Key Points**:
1. Analyze core e-commerce functions: product management, order processing, payment system, user center.
2. Choose a microservices architecture, splitting into product service, order service, payment service, and user service.
3. Technology Stack: Front-end React + Node.js back-end + MySQL + Redis + Nginx.
4. Design inter-service communication and API gateway.

### Example 2: Technology Stack Selection
**Function Description**: Select a technology stack for a real-time collaboration application.
**Execution Method**: The agent provides selection recommendations based on technology comparisons.
**Key Points**:
1. Core Requirements: Real-time capability, multi-user concurrency, data consistency.
2. Front-end: Vue.js + WebSocket (real-time communication).
3. Back-end: Node.js + Socket.io (high concurrency handling).
4. Database: PostgreSQL + Redis (caching).
5. Alternative Solution: Go + gRPC (performance optimization).

### Example 3: Generate Back-end API Code
**Function Description**: Generate RESTful API code for the user authentication module.
**Execution Method**: The agent directly generates code based on code standards.
**Key Points**:
1. Define API interfaces: Register, Login, Logout, Refresh Token.
2. Select Technology Stack: Node.js + Express + JWT + bcrypt.
3. Generate route, controller, and middleware code.
4. Add input validation and error handling.
5. Write unit test cases.

### Example 4: Front-end React Project Development
**Function Description**: Develop a React front-end project to implement a user management interface.
**Execution Method**: The agent generates front-end code based on the front-end guide.
**Key Points**:
1. Select Technology Stack: React + TypeScript + Vite + Tailwind CSS.
2. Design component architecture: Page components, business components, common components.
3. Implement state management: Use Zustand or Redux Toolkit.
4. Implement routing and navigation.
5. Add performance optimization: Code splitting, lazy loading, caching strategies.

### Example 5: Kubernetes Deployment Configuration
**Function Description**: Configure a Kubernetes deployment environment for an application.
**Execution Method**: The agent generates K8s configurations based on the operations guide.
**Key Points**:
1. Create Deployment configuration, setting resource limits and health checks.
2. Configure Service and Ingress to implement service exposure and load balancing.
3. Configure ConfigMap and Secret to manage configurations and sensitive information.
4. Set up Horizontal Pod Autoscaler for automatic scaling.
5. Configure NetworkPolicy for network security isolation.
