# Git, GitHub, and GitHub Actions Basics

## 1. What Is GitHub Actions?

GitHub Actions is a built-in automation feature provided by GitHub. It allows developers to define custom workflows that run automatically when certain events happen in a repository.

Common examples of those events are:

- pushing code to a branch
- creating or updating a pull request
- running a scheduled job
- manually triggering a workflow

These workflows can be used for:

- continuous integration
- continuous deployment
- testing
- code quality checks
- automation of repetitive repository tasks

## 2. Why GitHub Actions Is Important

When a project grows, the team usually repeats the same activities again and again:

- build the project
- run tests
- review code quality
- validate pull requests
- deploy to environments

Doing this manually is slow and error-prone. GitHub Actions helps automate these steps so developers can focus more on writing features and fixing problems.

## 3. GitHub vs Git

This is one of the most important distinctions.

### GitHub

GitHub is a remote code hosting platform and repository service. It is the place where teams store code, collaborate, create branches, raise pull requests, and manage project history.

In simple words:

- GitHub is where the code lives remotely
- teams use it for collaboration
- it acts as the shared source of truth

### Git

Git is a distributed version control system.

It helps developers:

- track source code changes
- create and switch branches
- merge branches
- pull and push code
- resolve conflicts
- collaborate safely with multiple developers

In simple words:

- Git is the version control tool
- GitHub is the hosted platform built around repositories

## 4. Why Version Control Matters

In real teams, multiple developers work on the same project at the same time. One developer may work on feature A, another on feature B, and another on bug fixes or testing support.

Without version control, teams face problems like:

- overwritten code
- missing changes
- confusion about the latest version
- difficulty merging work
- poor traceability of who changed what

Git solves this by maintaining a structured change history and allowing safe collaboration through branches and merges.

## 5. Branching Concept from the Transcript

A common pattern is:

1. Start from the `main` branch.
2. Create a separate branch for a new story or feature.
3. Do development in that branch.
4. Write test cases.
5. Validate the work locally.
6. Raise a pull request.
7. Merge into `main` only after checks pass.

This protects the main branch from unstable or incomplete work.

## 6. Merge Conflicts

A merge conflict happens when two developers modify the same part of the same file and Git cannot decide automatically which version should be kept.

Conflict resolution usually means:

- understanding both changes
- combining the correct logic
- retesting before merging

This is a normal part of collaboration, and good Git habits make it manageable.

## 7. Where GitHub Actions Fits In

Git helps manage code history.
GitHub stores and organizes the repository.
GitHub Actions automates what should happen around that code.

A simple way to remember it:

- `Git` tracks code changes
- `GitHub` hosts and manages repositories
- `GitHub Actions` automates workflows on top of repository events

## 8. Practical MLOps Relevance

For MLOps projects, GitHub Actions can automate tasks such as:

- running unit tests for pipeline code
- validating training scripts
- checking formatting or linting
- building Docker images
- deploying services or workflows
- updating documentation or metadata

That makes it useful not only for web apps, but also for data science and ML systems.

## Key Takeaways

- GitHub Actions is GitHub's workflow automation feature.
- GitHub is the remote repository platform.
- Git is the version control system used to manage changes.
- Branching and pull requests help teams collaborate safely.
- GitHub Actions automates checks and deployments around the repository.
