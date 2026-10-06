# Northstar · GTM workflow brief

All data is synthetic. Addresses use `.example` and must never be uploaded or contacted. `verified: true` is a simulation flag, not real email verification.

## Team request

The team copies research into a campaign tool and a CRM. Duplicate rows, unverified data and repeated webhook deliveries can produce confusing records. Build the smallest local flow that makes the next action reliable. No baseline time or real conversion results have been supplied.

## Inputs and initial state

Read `fixture.json`. The account begins at Research. CRM contacts, activities, campaign drafts, processed events and retry queue begin empty. The suppression set already contains Jordan. All sources are in the packet; S99 does not exist. Do not infer missing email addresses or create evidence for S99.

Morgan appears twice with different source references. Merge by trimmed, lowercased email within the same account and preserve both valid sources. R1/R2 and R3 can produce paused drafts. R4 is suppressed; R5 is held for missing verified email; R6 is held for an unknown source. A valid source alone does not establish commercial qualification.

## Simplified local contract

Use functions, objects or local files. These names describe behavior, not real API routes:

| Adapter operation | Minimum behavior |
| --- | --- |
| `crm.upsert_contact(key, data)` | One identity per normalized email and account; preserve sources and owner |
| `campaign.upsert_draft(key, data)` | One paused draft per eligible person; include source IDs and `review_required: true` |
| `campaign.pause(key, reason)` | Prevent further follow-up for a reply or opt-out |
| `crm.update_contact(key, data)` | Record contact state, next action and owner; preserve account stage |
| `crm.upsert_activity(event_id, data)` | One activity per event; identify source event and observed outcome |
| `log(operation, key, outcome)` | Trace success, hold, duplicate and retry; do not log credentials |

You choose fields and storage. Show field mapping and stable keys. Mock responses can be in-memory objects. No server, database, UI framework, real authentication, scheduler or live webhook endpoint is required. Source code must be copyable from the submitted HTML.

## Event order and failure injection

1. Import all six input rows, then import them again.
2. Process the four events in array order. E1 is a reply from Alex; E2 is Morgan's opt-out. Each occurs twice with the same ID.
3. On the first E1 call to `crm.update_contact`, return/raise a simulated 503 once. All subsequent attempts succeed. Pause follow-ups immediately, retain pending work, and demonstrate recovery with a bounded retry or explicit manual replay.
4. Record an event as fully processed only after its required effects succeed. Repeated deliveries after success must not add another activity. A partial failure must not permanently discard the event.
5. Import the original rows once more. Suppression and reply state must survive; no resumed outreach or new drafts for those people.

Retries are simulated immediately. You do not need backoff timers, a distributed queue or exactly-once delivery infrastructure. Explain the limitation and one necessary production safeguard.

## Observable checks

- After initial import: exactly two paused drafts (Morgan and Alex), each requiring review; one Morgan identity with S1 and S2; three other people held/suppressed with reasons.
- After repeated import: no additional drafts, contact identities or activities.
- E1: Alex has a reply, follow-up remains paused, the next action is human review by the Account Owner. Research does not become Qualified.
- E2: Morgan is suppressed, follow-up paused, with no automated next outbound action. The suppression set survives subsequent imports.
- After recovery and repeated events: two distinct event activities, one for E1 and one for E2; neither event permanently lost. Logs show the initial E1 failure and the successful recovery.
- CRM persistence for held/suppressed inputs is optional; they must remain visible in the audit output. Therefore total CRM contact count is not an acceptance criterion. Eligible contact/draft identities and event activities are.

## Objections to address

Simulate at least two operator/reviewer questions and the account-owner question:

- RevOps: “Why not put every row in the campaign and clean it up later?”
- Sales: “Alex replied. Why is the account still at Research?”
- Technical reviewer: “The CRM failed after the campaign paused. What happens on retry?”
- Account Owner: “Can we call these qualified opportunities and claim a conversion improvement from this demo?”

## Measurement and handoff

Choose two measures, such as eligible-record accuracy, duplicate actions per replay, unresolved failures, operator minutes per reviewed batch, or reply-to-reviewed-next-action delay. Define units or numerator/denominator. Mark observed fixture counts as synthetic. If you propose a pilot, define its baseline, comparable workload, review period, responsible role and continue/adjust/stop criterion; do not invent results.

Document how a colleague runs the code, inspects outputs, handles held records, retries failures and stops the flow. Write down what would need review before connecting real Lemlist and CRM APIs.
