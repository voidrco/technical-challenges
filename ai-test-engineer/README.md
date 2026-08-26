<p align="center">
  <img src="https://unicorn-images.b-cdn.net/277503c3-f842-45d5-88de-69c30719b278?optimizer=gif" width="200" alt="Voidr Logo" />
</p>

<h3 align="center">From Hourly IT Services to AI-Native Operations</h3>

# AI Test Engineer Technical Challenge

Take-Home Challenge

Time: 5 days | Stack: Playwright

---

## Overview

As an AI Test Engineer at Voidr, you'll pilot AI Agents that autonomously test mission-critical systems for companies like AB-InBev, Stone, Serasa, and Philips. Playwright is the engine our agents use to interact with applications — and mastering it is foundational to the role.

This challenge evaluates your ability to create maintainable, reliable test automation with Playwright that demonstrates technical depth and practical judgment. It's a preview of the foundation you'll build on every day: writing and structuring the kind of tests that our AI Agents execute autonomously at scale.

---

## Target Applications

### API - Restful Booker

**Documentation:** https://restful-booker.herokuapp.com/apidoc/index.html

### Web Interface - Automation in Testing

**URL:** https://automationintesting.online/

---

## Requirements

### API Tests

Minimum of 10 test cases covering:

- Success scenarios (happy paths)
- Negative scenarios (validation errors, edge cases)
- Multiple API endpoints
- Status code, schema, and data validation

### UI Tests

Minimum of 10 test cases covering:

- Success scenarios (critical user flows)
- Negative scenarios (form validation, error messages)
- Page element interactions
- Visual and behavioral assertions

---

## Technical Constraints

- **Language:** TypeScript (required)
- **Test Framework:** Playwright (required)
- **Code Structure:** Use Page Objects or Application Actions patterns
- The solution must be runnable locally with clear setup instructions

---

## Evaluation Criteria

| Dimension | What We Look For |
|-----------|------------------|
| **Test Planning** | Clarity and justification of test strategy, focus on critical scenarios aligned with business impact |
| **Test Coverage** | Breadth of coverage and accuracy in verifying essential functionality, including error scenarios and critical flows |
| **Code Quality** | Code organization and maintainability, best practices in test automation, clean and readable code |
| **AI Collaboration** | How effectively you leverage AI as a co-pilot for test creation — this is the core of the AI Test Engineer role at Voidr |
| **Tool Integration** | Effective use of Playwright, Docker, and GitHub Actions to ensure automation and consistency |
| **Communication** | README quality, documented trade-offs, clear explanations of technical decisions |

### What We're NOT Looking For

- 100% coverage: Quality over quantity
- Over-engineered solutions: Solve the problem at hand, not hypothetical future problems
- Perfect code: We value pragmatic decisions and documented trade-offs

---

## Deliverables

1. **Source code** in a private GitHub repository

2. **README** with:
   - Installation instructions
   - How to run the tests
   - Project structure
   - Test strategy and rationale behind test cases
   - AI usage documentation (see below)

3. **Video walkthrough** (maximum 5 minutes)
   - Brief explanation of your solution and approach
   - Quick demo of your tests running
   - Record using Loom, OBS, or any screen recorder

---

## AI-Assisted Development (Required)

At Voidr, AI Test Engineers pilot AI Agents every day — using AI to generate, validate, and refine tests is the job, not a bonus. This challenge must be completed using AI assistance because we want to see how you work with AI as a co-pilot, which is exactly what you'll do here.

### Playwright MCP Configuration

Configure and use Playwright MCP (Model Context Protocol) in your IDE. MCP allows AI assistants to interact directly with Playwright for browser automation — the same pattern our AI Agents use in production.

**Resources:**
- [Playwright MCP Server](https://github.com/microsoft/playwright-mcp)
- [MCP Documentation](https://modelcontextprotocol.io/)

Document your MCP configuration in the README.

### AI Usage Documentation

In your README, include a section explaining:

- Which AI tools you used (Cursor, Claude, GitHub Copilot, etc.)
- How you used AI to generate and refine test cases — did you prompt it to analyze the application? To suggest edge cases? To write assertions?
- Specific examples of prompts or interactions that were particularly effective
- How you validated and refined AI-generated code — what did the AI get wrong, and how did you fix it?
- What you learned about using AI for test automation and how it changed your workflow

We're not looking for candidates who avoid AI — we want professionals who know how to pilot it strategically, evaluate what it generates, and understand when to trust or override its output. This is the core skill of an AI Test Engineer.

---

## Stretch Goals

These are optional but will be highly valued:

- **Agent-Driven Testing:** Create a simple agent loop where an LLM analyzes the application state and decides what to test next — this bridges directly to what you'll do at Voidr
- **CI/CD:** GitHub Actions configuration with automatic test execution on push/PR
- **Performance:** Parallel test execution and efficient worker usage
- **Visual Testing:** Visual regression testing implementation
- **Docker:** Containerized execution environment
- **Reporting:** Automatic test report publishing

---

## Timeline

- **Duration:** 5 days from when you receive this challenge
- **Effort:** Focus on quality over quantity. Well-structured tests that demonstrate technical reasoning are more valuable than extensive coverage.

---

## How to Submit

When you finish the challenge, follow these steps:

### Step 1: Grant Repository Access

Add **operationsvoidr** as a collaborator to your private GitHub repository.

### Step 2: Send Your Submission Email

Send an email to **hiring@jobs.voidr.co** with:

**Subject:** `[ Technical Challenge Voidr ] - Your Full Name`

**Body:**
- Brief text introduction of your solution (2-3 paragraphs)
- Link to your GitHub repository
- Link to your 5-minute video walkthrough

---

## What Happens Next

### If you pass this stage

You'll receive an email with a link to schedule a 30-minute technical session with our CTO, Victor Buchalla.

During this session, you'll:
- Walk through your solution and key decisions
- Explain the rationale behind technical choices
- Discuss what you would improve given more time
- Demonstrate deep understanding of all code, including AI-generated parts

Be prepared to extend or modify the solution live (pair programming style).

### If you don't pass this stage

You'll receive structured, honest feedback explaining why it wasn't a match this time.

---

## Questions?

If anything is unclear or you encounter issues with the test applications, reach out via email: **hiring@jobs.voidr.co**

Asking good questions is a positive signal, not a negative one.

---

Interested in joining the team? Check open positions at [voidr.co](https://voidr.co)
