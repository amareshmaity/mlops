# CI, CD, and Workflow Fundamentals

## 1. What CI and CD Mean

CI/CD stands for:

- **Continuous Integration**
- **Continuous Deployment** or sometimes **Continuous Delivery**

These are core software engineering practices used to make code integration and release more reliable.

## 2. Continuous Integration (CI)

Continuous Integration means developers frequently merge code changes into a shared repository, and every important change triggers automated validation steps.

Typical CI activities include:

- building the application
- running unit tests
- running integration tests
- checking whether old functionality still works
- validating pull requests before merge

The main goal of CI is to catch issues early, before broken code reaches the main branch or production environments.

## 3. CI Example from the Lecture

Imagine three developers are working on different stories:

- Developer A works on Story A
- Developer B works on Story B
- Developer C works on Story C

Each developer creates a separate branch from `main`, implements the feature, and then attempts to merge back.

Before merging, the team wants automated checks such as:

- run test cases
- build the project
- verify that previous functionality is not broken
- review whether the code follows good practices

That automated validation flow is part of CI.

## 4. Continuous Deployment (CD)

Continuous Deployment extends CI by automatically moving validated code into deployment environments.

After the code:

- passes required checks
- is merged successfully
- is considered stable enough

it can be deployed automatically to a target environment.

This reduces manual release work and speeds up delivery.

## 5. Deployment Environments Mentioned in the Transcript

The transcript explains a common environment progression:

- `Dev`
- `QA`
- `UAT`
- `Production`

### Dev Environment

Used by developers to test whether the newly deployed project works in a running environment.

### QA Environment

Used by the QA team to find bugs and validate expected behavior more thoroughly.

### UAT Environment

UAT stands for User Acceptance Testing. It is often treated like a pre-production stage where the application is validated before final release.

### Production Environment

This is the live environment used by real users.

## 6. Why Teams Do Not Deploy Directly to Production

Direct deployment to production is risky because:

- bugs may still exist
- configuration issues may appear only after deployment
- previous functionality may break
- the application may behave differently on real servers

Moving gradually through environments helps reduce release risk.

## 7. What a Workflow Means

A workflow is a series of automated steps that run when a specific event happens.

In GitHub Actions, a workflow is usually defined in a YAML file and can include tasks such as:

- install dependencies
- build the application
- run tests
- publish artifacts
- deploy to a server or cloud environment

## 8. Events and Triggers

One of the most important ideas in GitHub Actions is that workflows are event-driven.

Examples of events:

- a `push` to a branch
- a `pull_request`
- a scheduled run
- a manual dispatch

When the event occurs, the workflow starts and performs its defined steps.

The transcript highlights this clearly: a pull request or merge can act as the event that triggers the workflow.

## 9. CI and CD as Automated Guardrails

You can think of CI/CD as a set of automatic guardrails around your project.

Instead of relying on memory or manual discipline, the workflow system ensures that important checks happen every time.

This is especially useful for teams because:

- standards become consistent
- errors are caught earlier
- release speed improves
- collaboration becomes smoother

## 10. Role of Docker in Deployment

The lecture briefly mentions Docker in the deployment discussion.

Why Docker helps:

- packages the application with its dependencies
- reduces "works on my machine" problems
- makes deployment more consistent across servers
- simplifies moving applications between environments

In real MLOps workflows, GitHub Actions and Docker are often used together.

## 11. Benefits of CI/CD and Workflows

- improved collaboration
- faster delivery
- fewer manual errors
- better code quality
- repeatable release process
- clearer feedback for developers

## Key Takeaways

- CI focuses on automatically validating code changes.
- CD focuses on automatically deploying validated code.
- A workflow is an event-driven automation pipeline.
- Pull requests and merges often trigger CI/CD steps.
- Multiple environments help teams release software more safely.
