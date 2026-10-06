<p align="center">
  <img src="https://unicorn-images.b-cdn.net/277503c3-f842-45d5-88de-69c30719b278?optimizer=gif" width="200" alt="Voidr Logo" />
</p>

<h3 align="center">From Hourly IT Services to AI-Native Operations</h3>

# Go-to-Market Engineer Technical Challenge

Take-Home Challenge

Time: 5 days | Role: Go-to-Market Engineer · Internship / Junior

---

## Overview

This challenge evaluates how you turn a commercial requirement into a small, testable automation that someone else can operate.

You will receive fictional account records and campaign events. Build a local flow that checks the data, prepares paused campaign drafts, updates a mock CRM, and makes failures visible without creating duplicate actions. Explain what the flow improves and how you would measure it.

We evaluate working logic, judgment and learning. Academic and personal projects count. No paid subscription, deployed service or professional sales experience is required.

> **Language requirement:** Submit the HTML and record the presentation in **English**. AI-assisted preparation is welcome; you must be able to explain the decisions and code. Accent and native fluency are not evaluation criteria.

---

## What is Voidr?

Before starting, understand the operating context of the team you are helping:

- **Website:** https://www.voidr.co
- **LinkedIn:** https://linkedin.com/company/voidrco
- **Product pages:** Explore relevant product and solution pages

In your HTML, cite two official public sources with access dates and one supported observation about Voidr. Explain why that observation matters to the data or review your commercial flow needs. Do not invent customer results or financial returns. If a source is inaccessible, note the limitation and use another official page.

---

## Voidr Engagement Model — Fixed Premises

Use these premises for this exercise:

- **Start with the workflow:** identify the manual task, its user, the input and the decision it supports before choosing technology.
- **Keep evidence separate from inference:** an external signal can justify research; it does not establish a customer's problem, budget or purchasing authority.
- **Commercial ownership stays explicit:** RevOps sets commercial rules and the account owner reviews next actions. Automation does not authorize a new promise or independently qualify an opportunity.
- **Review before outreach:** campaign payloads remain paused drafts. Show a human-review checkpoint; no live enrollment or sending is part of this exercise.
- **Respect contact state:** replies pause follow-ups; opt-outs suppress future outreach, including retries and subsequent imports.
- **Make repeated execution safe:** repeated records and events must not create duplicate contacts, activities or drafts.
- **Make failure visible:** preserve the last valid state, identify the failed operation and provide a bounded retry or manual recovery path.
- **Simulation only:** all records, events and integrations run locally. Do not contact real people, access company systems, upload leads or use production credentials.

Your task is a commercial operations automation. You are not expected to design a customer deployment, create a revenue strategy or demonstrate financial ROI from synthetic data.

---

## Materials Provided

- [Fictional workflow brief and local integration contract](./case/workflow-brief.md)
- [Input records and events](./case/fixture.json)
- [Voidr workflow presentation template](./template/voidr-gtm-template.html)

All names and records are synthetic. Use the supplied source IDs; do not research the fictional company. The simplified mock contract is an exercise interface, not the real Lemlist or Voidr CRM API. No external network calls, paid accounts or credentials are needed.

---

## Your Mission

Prepare a small workflow for the team researching **Northstar Retail Systems**.

Your work should allow the team to:

1. inspect which records can become reviewed campaign drafts and why others are held or suppressed;
2. run the transformation and see linked account, contact, activity and next-action records;
3. process a reply and an opt-out, including repeated events and a simulated integration failure;
4. inspect execution evidence and recover without duplicating actions;
5. decide whether to pilot the flow based on defined quality and effort measures.

Use one language or a local workflow tool you can explain. A short Python or JavaScript script with in-memory adapters is sufficient. Implement the transformation and event logic; a diagram alone is not sufficient. Keep real API adapters and scheduling as documented next steps.

---

## Challenge Components

### Part 1: Workflow Implementation and Operations Deck

Create a 4–6 slide presentation using the template, supported by a compact technical appendix inside the same HTML.

Build and explain:

- **Data preparation:** normalize identifiers, merge the duplicate without losing sources, validate source IDs and contact data, and show a reason for every held or suppressed record.
- **Paused campaign drafts:** map eligible records to a mock Lemlist draft and CRM contact. Preserve source references and a review checkpoint. One short source-grounded message example is enough; writing a full sales cadence is not required.
- **Event handling:** apply the supplied reply and opt-out, ignore duplicate events, and keep suppression effective on another import.
- **Failure and recovery:** simulate the specified one-time CRM error, show a pending/retryable operation and recover with bounded retry or an explicit manual retry. Do not mark the event complete before required effects succeed.
- **Tests and evidence:** show assertions or explicit checks for normal import, duplicate import, reply, opt-out, repeated events and failure recovery. Show expected versus actual outputs and a useful log excerpt.
- **Measurement:** define two operational metrics with numerators, denominators or units, and a small experiment with a baseline, comparison, review period and decision rule. Synthetic counts do not establish real productivity or conversion gains.

Keep a reproducible implementation in the HTML appendix as copyable source code with run instructions and fixture references. An exported local workflow is acceptable if its logic can be inspected and reproduced without a paid service. You may implement the flow directly in the HTML instead. Do not add a third submission or require reviewers to access an external code repository.

#### Format and Design Requirements

- **4–6 slides** recommended, plus a compact technical appendix in the same file
- Use the provided [standalone HTML template](./template/voidr-gtm-template.html)
- You may remove, duplicate, reorder or adapt layouts
- Preserve recognizable Voidr branding and readable hierarchy
- Submit **one self-contained `.html` file** that opens directly in a modern browser; embed code, checks and relevant output as text or local interactive elements
- All visible copy must be in **English**; escape source code so it displays correctly
- Remove bracketed placeholders and visible `Template · ...` instructions

AI may help edit the HTML and code. Visual polish beyond a readable deck is not scored. The appendix is available for inspection without expanding the 10–15 minute recording.

---

### Part 2: Workflow Demonstration and Handoff (Video Deliverable)

Record a **10–15 minute** walkthrough for the fictional internal team.

#### Scenario

You are presenting the local prototype to:

- **Head of RevOps** — Wants clear rules, a measurable bottleneck and a manageable pilot
- **Sales Engineer** — Needs usable records, paused follow-ups after replies and a clear next action
- **Technical Reviewer** — Checks data provenance, reproducibility, failure handling and duplicate prevention
- **Account Owner** — Questions whether the data supports an approach or a change of commercial stage

#### What You Must Demonstrate

1. **Workflow and Data Judgment**
   - Explain the task, user, scope and source limitations
   - Show eligible, held and suppressed records with reasons

2. **Working Local Flow**
   - Run the import and inspect the draft/CRM outputs
   - Run it again and show that it creates no duplicate contacts, activities or drafts

3. **Events and Recovery**
   - Demonstrate reply and opt-out handling, including repeated events
   - Show the one-time integration error, pending state and successful recovery
   - Reimport after the opt-out and show that the contact stays suppressed

4. **Objections and Correction**
   - Address at least two operator/reviewer objections and one account-owner objection from the packet
   - Distinguish what you implemented from what is proposed for a real integration

5. **Handoff and Measurement**
   - Explain how another person runs, checks, stops and retries the flow
   - Close with the pilot owner role, measures, review point and decision rule

#### Video Guidelines

- Use Loom, OBS or any screen recorder
- Present the HTML and demonstrate the local implementation and outputs
- Simulate the objections yourself; no other participant is required
- Keep the complete recording between **10 and 15 minutes**; longer submissions may not be reviewed in full
- Spoken and visible presentation content must be in **English**
- Focus on working behavior and decisions; do not spend the recording reading code line by line

---

### Part 3: AI-Assisted Preparation (Required)

You **must** use AI during this challenge. Use it to clarify requirements, draft transformations, inspect edge cases, write tests or prepare the presentation.

Keep a record of tools, prompts, useful outputs, corrections and at least one suggestion you rejected or substantially changed. You do not need a separate AI explanation in the video; retain the record for the interview. In the HTML, identify one meaningful AI-assisted decision and how you verified it.

Do not use confidential information from current or former employers. Keep the fixture and execution local; no paid AI API is required.

---

## Deliverables

1. **Workflow Deck and Technical Appendix**
   - One self-contained HTML file; 4–6 slides plus appendix
   - Copyable implementation, reproduction instructions, checks and outputs included in that file
   - All visible content in English

2. **Workflow Demonstration Video**
   - Between 10 and 15 minutes
   - Loom link or video file
   - Working flow, failure recovery, objections, measurement and next step

---

## Timeline

- **Duration:** 5 days from receipt
- **Expected effort:** Approximately 4–6 hours
- Suggested allocation: 30 min reading/research, 120 min implementation, 45 min checks, 45 min deck/appendix, 30 min recording (4.5 hours, with time for corrections)
- If other commitments require more time, let us know

---

## How to Submit

Send an email to **hiring@jobs.voidr.co** with:

**Subject:** `[ Technical Challenge Voidr ] - Your Full Name`

**Body:**

- A brief introduction to an automation you built and maintained, including its user and your contribution; academic and personal work count
- Link to or attachment of your single HTML file
- Link to your 10–15 minute video
- Approximate time spent and any incomplete detail

Check that the HTML opens and that the video is accessible outside your account. The fixture may be retrieved from this repository; all candidate-authored implementation and evidence must be in the HTML.

---

## What Happens Next

### If you pass this stage

You will receive an invitation to a **45-minute session with the hiring team**. Participants and format will be confirmed in the invitation.

During the session, you will explain the code and rules, discuss your use of AI, trace a failed event, and consider a small change to the inputs. We want to understand what you verified and what still needs work, rather than see the same presentation again.

### If you don't pass this stage

You will receive structured feedback on the work reviewed and why it was not a match this time.

---

## Questions?

Contact **hiring@jobs.voidr.co** if an instruction is unclear.

Asking precise questions and documenting missing information are positive signals. State reasonable assumptions about the mock interface without claiming they describe production systems.

---

## About the Role

Go-to-Market Engineers at Voidr build and maintain tools that help the commercial team research accounts, prepare outreach, handle replies and keep decisions traceable.

Key responsibilities include:

- turning recurring commercial tasks into small, testable workflows;
- integrating data sources, prospecting tools and CRM through APIs, webhooks and scripts;
- reviewing data and AI outputs, controlling duplicates and handling failures;
- documenting operation and recovery so other people can use the workflow;
- measuring quality and effort with the team and improving the rules.

This is an early-career role with review and guidance. Bring practical programming and an explainable automation used by another person; professional employment is not required. Professional spoken and written English is part of the role.

Interested? Visit [Voidr careers](https://www.voidr.co/pt-br/empresa/carreiras).

---

**Note:** This challenge is used in actual hiring processes. Submit your own work and be ready to explain AI-assisted decisions.
