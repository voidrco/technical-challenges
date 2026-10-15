# AI Software Engineer · Junior — Reliable AI Exploration Worker

Take-home challenge · TypeScript + Playwright · 5 calendar days · 8–12 hours, hard cap of 12 hours

## Why this challenge

At Voidr, engineers build reusable software and AI capabilities for critical applications. This exercise evaluates architecture, implementation, integration of AI, testing, observability, reliability and technical communication. Build a small working component and show how you verified it.

This is a **Junior opening with an advanced engineering problem**. The problem deliberately includes architecture and failure modes commonly handled by senior engineers. Show how far you can take a thin working implementation, how you investigate unknowns and which trade-offs you make. Years of senior employment are not a requirement. We will review implemented behavior, reasoning and learning ability, with unfinished work explicitly recorded within the time cap.

## The mission

Build an agent that explores a web application, proposes useful interactions and produces a report of potential issues with reproducible evidence. A CLI is sufficient. Use TypeScript and Playwright; choose your own agent framework or write the orchestration yourself.

Primary target: https://with-bugs.practicesoftwaretesting.com

We also supply a [local fixture](./fixtures/README.md). Use it for repeatable automated tests and whenever the external application is unavailable. It is intentionally small and is not a replacement for a full application. Do not infer coverage of the external site from fixture results.

Prioritize one meaningful journey, such as browsing products and updating a cart. You are not expected to cover authentication, checkout and every area of the site.

## Required behavior

### 1. A bounded exploration loop

The agent observes the page, asks an LLM to propose the next action, validates that proposal, executes an allowed action and records the result. Support navigation, element interaction and screenshots. Keep observations, proposed actions, execution results and findings separate.

- Constrain the action vocabulary and validate model output at runtime. TypeScript types alone do not validate external data.
- Restrict navigation to the configured origin. Page text and model output must not change this boundary or authorize shell commands, filesystem access or external requests.
- Set maximum actions, wall-clock duration and model calls. Bound retries and repeated actions; stop cleanly on budget exhaustion.
- Record a short operational rationale for an action: hypothesis, expected observation and evidence. We do not need a transcript of internal model reasoning.
- Model errors, browser timeouts and unavailable pages must produce an understandable result, rather than an infinite loop or an invented success.

### 2. Human guidance

At a documented checkpoint, summarize progress and proposed next steps. The user can continue, stop or provide guidance. Explain what triggers the checkpoint. A stop request must prevent subsequent browser/model actions; save partial results.

### 3. Implement `find_broken_images` yourself

The agent must call this tool through the same tool interface used by its exploration loop. You may use Playwright or an agent library for other interactions, but do not use a prebuilt broken-image detector.

Return a structured result per relevant image, including source, alt text, a usable locator or page position, evidence and status/reason. Distinguish:

- A confirmed failed load or invalid/missing image source.
- An image still loading, lazy-loaded or outside the inspected viewport.
- An intentionally hidden image, which is not automatically a broken image.
- An inconclusive result.

Check completion/loading state before relying on natural dimensions. If you report an HTTP status, show how it was actually observed; do not infer a 404 from zero dimensions. Do not issue arbitrary additional requests to off-origin URLs merely because they appear in image attributes.

### 4. Report findings and limits

Produce machine-readable JSON plus a readable summary. For each finding, include:

- Stable ID, category, severity and confidence, with a short justification.
- Page/route, reproduction steps and expected versus observed behavior.
- Screenshot or other observed evidence, linked to the relevant trace/action.
- Whether it is confirmed, a hypothesis requiring review or an inconclusive observation.

Deduplicate repeated observations. State what was explored, what was not, why the run stopped and how to resume or investigate. Model-generated allegations without observed evidence must not appear as confirmed bugs. A clean or inconclusive run is valid if honestly reported.

### 5. Make it verifiable and maintainable

Provide a documented command or library boundary for an engineer to run the agent with a target, budgets and output directory. An HTTP service or cloud deployment is not required. Include structured logs with a run identifier, action result and stop reason. Do not log credentials or full sensitive payloads.

Separate the model adapter, browser execution, image tool and reporting sufficiently to test them. Include a real-provider adapter configured through environment variables and an offline scripted/fake adapter for deterministic tests. Clearly label simulated versus real model runs. If you have access to a provider, include one short real-model run; if you do not, document the limitation. Paid API access and cloud accounts are not prerequisites, and offline evidence must never be represented as a real-model run.

Include automated tests for these behaviors, using the supplied fixture or an equivalent local fixture:

1. A genuinely failed image is detected; a working, hidden or not-yet-loaded image is not mislabeled as a confirmed failure.
2. A malformed model response or forbidden/off-origin action is rejected before browser execution.
3. A repeated action, timeout or transient failure cannot cause unbounded work; the agent saves a partial report with an accurate stop reason.
4. Two observations of the same issue do not create duplicate confirmed findings.
5. User stop prevents the next browser/model action.

You choose the testing approach. Tests must assert externally meaningful behavior, rather than just mirror the implementation. Explain one failure you investigated and how you verified the correction; do not invent an incident.

### 6. The senior-level problem: a resumable worker with isolated runs

Two fictional teams want to use the same agent. One run can fail while another is still executing. Turn your exploration loop into a small worker that handles the [supplied incident scenarios](./fixtures/fault-scenarios.json).

Implement a narrow local solution. A CLI, local files/SQLite and test doubles are enough; no distributed queue, Kubernetes or real account/authentication system is required.

**Run lifecycle and isolation**

- Accept a run configuration with `tenantId`, `runId`, allowed origin, budgets and output location. Define the lifecycle states and valid transitions; a persisted stop or completion must not silently revert to running.
- Demonstrate two runs with the same `runId` under different fictional tenants. Keep their browser sessions, artifacts, observations and results separate, and prevent user-controlled identifiers from escaping the output directory.
- Limit concurrent work. Show two active runs in a deterministic test or small local execution; shared mutable state must not mix their results or budgets.

**Recovery and ambiguous effects**

- Persist enough progress to stop the worker, restart it and continue the same logical run without resetting its consumed budgets or duplicating already committed findings.
- Model at least one failure after a browser interaction may have happened but before its outcome was persisted. Distinguish a known failure from an unknown outcome. Demonstrate how your implementation avoids blindly repeating a potentially mutating action; pausing for review or re-observing the state is acceptable when justified.
- Explain the failure guarantees you actually provide. Do not claim exactly-once browser effects just because requests or findings are deduplicated.
- A stop request must cancel pending work where possible, block later dispatch and preserve the report. Describe what happens to an action already in flight; do not claim that cancellation reverses effects.

**Evaluate the agent, not just its TypeScript**

Create a tiny repeatable evaluation with at least three scripted model behaviors: valid guidance, malformed output and a proposed off-origin action. Include one case where the model confidently claims a nonexistent bug. Report the observed outcome of each case and whether the agent was allowed to mark the finding confirmed. These are controlled local tests, not a benchmark claiming real-world accuracy.

Execute and report all six supplied incident scenarios against your solution. Your test harness can inject browser/model failures; it must exercise your actual orchestration and persistence logic, not merely return hardcoded expected statuses. State which cases pass, fail or remain incomplete and link each to evidence. Test names and interfaces are your choice; expected invariants are public in the scenario file.

Include an architecture decision note of at most one page covering persistence boundaries, action replay, isolation and the next bottleneck at greater scale. Explain one alternative you rejected. This note belongs in the existing README; do not create a second design project.

## Deliverables

1. Source code in a private repository, with a lockfile and `.env.example` containing placeholders only. Give **operationsvoidr** read access.
2. A concise README covering setup, the commands for execution/tests, architecture, interface and report format, trade-offs, known limits and what you would improve for production. State time spent and where you stopped. Include the one-page architecture decision note and the incident/evaluation results.
3. A sample report and trace/evidence, clearly labeling target, adapter mode and configuration. Include automated test output. Explain any target outage or unexecuted check.
4. A simple architecture diagram, included in the README.
5. A video of up to 7 minutes **in English** demonstrating the same solution, a test and one important trade-off. Written materials may be in Portuguese or English; we assess clarity and understanding, not accent.
6. AI usage notes, up to half a page: tools used, one useful interaction, something you verified or corrected, and your own contribution. AI-assisted development is required; you must understand all submitted code.

Do not build a UI, account system, complete testing platform or production infrastructure. Local persistence and the small worker in section 6 are required. A thin HTTP API, cloud deployment, MCP and automatic test generation remain optional design discussion topics; they do not compensate for weak core behavior. Spend the time on a reliable small solution.

## Time, scope and boundaries

- Five calendar days from receipt. Tell us if other commitments require an extension.
- Budget 8–12 focused hours and stop at 12. Record unfinished work and priorities; overtime and feature count do not earn extra credit.
- Use only the supplied fixture and the designated intentionally buggy application. Do not scan unrelated services, use real personal data or enter real payment details. Do not load-test or attempt exploitation.
- No paid services are required. Secrets stay outside the repository and recordings.
- This is a fictional hiring exercise; candidate work will not be used in production.

## Evaluation

| Dimension | Weight | What we inspect |
|---|---:|---|
| Architecture, worker and interfaces | 25% | A working thin implementation; explicit lifecycle, isolation and persistence boundaries; justified trade-offs. |
| AI integration and control | 20% | Runtime validation, bounded decisions, separation of data and instructions, transparent simulation. |
| Testing and recovery | 25% | Executed incident scenarios, bounded concurrency/retries, crash recovery, ambiguous effects and cancellation. |
| Evidence and AI evaluation | 20% | Repeatable model evaluation, reproducible findings, traceability, deduplication and honest limits. |
| Communication and engineering judgment | 10% | Clear decisions, English explanation, maintainability and critical use of AI. |

A person reviews the evidence; a total score alone does not determine advancement. We evaluate the submitted scope and job requirements, not spending, visual polish or number of features. You may ask questions and document reasonable assumptions.

## Submission and next step

Email **hiring@jobs.voidr.co**, copying **nathalia@voidr.co**.

Subject: **[Technical Challenge Voidr] - Your Full Name - AI Software Engineer**

Include repository and video links plus the report/evidence. Verify read permissions. Do not include credentials.

If you advance, the technical team will discuss the existing work and ask for a small live change or debugging task concerning run isolation, persisted budgets or recovery. We will assess whether you can trace the behavior and safely change it, including code written with AI assistance. No second take-home is required. We will agree on the session time separately.
