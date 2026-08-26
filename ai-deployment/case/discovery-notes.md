# Northstar Retail Systems — Initial Discovery Notes

> Candidate material for the AI Deployment Technical Challenge

## Important Context

Northstar Retail Systems is a fictional company. The company, people, and identifying details are fictionalized. Some quantities and technical details have been generalized or altered. The operating patterns are representative of a real enterprise discovery conversation.

These notes are evidence from one initial call — not a finished diagnosis. Some statements are estimates, some terms may be imprecise, and important baselines are missing. Do not silently convert an estimate or opinion into a confirmed fact.

Do not search for Northstar Retail Systems. External research may help you understand Voidr or general technical concepts, but it is not evidence about this customer.

---

## Meeting Context

**Meeting type:** First discovery conversation  
**Meeting duration:** Approximately 50 minutes  
**Customer objective:** Explore whether AI-assisted quality and deployment practices could reduce release risk and manual effort  
**Decision status:** No solution, initial value-demonstration phase, budget, scope, or timeline has been approved. Some participants may use “PoC” informally; in this case, treat it as the same initial phase described in the challenge.

### Customer Participants

- **VP of Product & Customer Operations**  
  Business sponsor for the conversation. Focused on customer trust, operational friction, and taking a defensible recommendation to the executive committee.

- **Principal Engineer**  
  Deep knowledge of the legacy ERP, database logic, and internal engineering tools. Interested in AI, but skeptical of generic claims and concerned about integration effort.

- **Quality & Support Manager**  
  Responsible for functional QA and the escalation path from customer support to engineering.

---

## Raw Notes from the Conversation

### Product and Customer Base

- Northstar develops an ERP platform for retail and distribution companies.
- The core product has been in development for more than 20 years.
- Most customers run the software in their own infrastructure or through a Northstar cloud partner.
- Northstar maintains one primary product version for the installed base rather than a separate code line for each customer.
- Customers receive frequent updates, especially when fiscal or regulatory rules change.
- The current customer base ranges from small retailers to companies with business-critical operations and high availability expectations.
- A customer does not distinguish between an application issue, a database issue, or an infrastructure issue. From the customer's perspective, Northstar owns the outcome.

### Architecture and Modernization

- A long-running migration from a legacy desktop client to a web-based Java application is roughly **70% complete**. This is a conversational estimate, not a verified program metric.
- The platform is still largely monolithic and highly configurable.
- Newer modules place more business logic in Java services.
- Several core domains — including fiscal calculation, accounting, warehouse operations, and receiving — still depend heavily on database procedures and packages.
- Database changes are not represented in the primary Git workflow. An internal Northstar tool records database changes directly from the database.
- An engineer estimated that the product contains roughly **5 million lines of code**, but no recent count exists.
- A change intended for one configuration or module can affect behavior somewhere else in the product.
- The company has one production line and a parallel beta line. Major releases are planned annually, while fixes and smaller changes ship throughout the year.

### Functional Quality Process

- The quality team has approximately **10 people**.
- Testing is described as almost entirely manual.
- The QA professionals are business-domain specialists. They understand product configuration and business rules but are not expected to be software developers.
- The team documents many scenarios but cannot execute all of them for every change.
- A single commercial or fiscal flow may have **15–25 meaningful configuration variants**.
- A full fiscal validation can require product setup, inbound and outbound transactions, calculation checks, and final accounting or tax outcomes.
- One end-to-end fiscal journey can take between half a day and a full day to validate manually.
- A complete regression of a large module would take weeks or months, so the team prioritizes around the change being released.
- Test data is reasonably organized for common paths, but not every scenario has reliable data.
- Some journeys depend on external integrations or customer-specific configurations that cannot be reproduced internally.
- When Northstar lacks the environment or data, the team may validate in a customer's homologation environment. Not every customer maintains one.

### Release and Support Operations

- The team reports an average of **2–4 urgent fixes per week**, but the exact period, severity distribution, and root-cause breakdown were not confirmed.
- Patches can introduce problems outside the area the developer or tester was focused on.
- When a customer reports an issue, first-line support investigates and escalates to engineering when necessary.
- The contractual response target is typically 48 hours.
- For a business-critical customer incident, the practical expectation can become **2–4 hours**.
- The call did not establish the current escape rate, change failure rate, mean time to detect, mean time to resolve, or number of engineering hours spent on rework.

### AI and Internal Tooling

- A point-of-sale product team already uses AI across requirements and development.
- That team created internal testing tooling because its product interacts with hardware and cannot be tested like a browser application.
- The core ERP organization is earlier in its adoption journey.
- The principal engineer is beginning an AI enablement effort with one technical leader in part of the fiscal domain.
- Northstar is familiar with AI code-review products and will expect a clear explanation of how a proposed Voidr capability differs from a general-purpose code-review tool.
- The customer does not want another tool that creates maintenance work for a team that is already overloaded.

---

## Sanitized Conversation Excerpts

These excerpts preserve the meaning of the conversation but are not verbatim quotes.

> "Automated testing is a possible solution. The problem we need to define is whether the primary pain is insufficient capacity, customer-facing regression, or both."

> "We can document the scenarios, but we cannot execute every permutation. The product is too configurable and the combinations keep multiplying."

> "The tester focuses on the requested change. In a monolith, that change can affect something outside the tested path."

> "For a fiscal flow, the final result may be the tax or credit the customer will use. Reaching that outcome requires the complete workflow, not one isolated screen."

> "If the customer cannot operate, they do not care whether the cause is the database, the application server, or the application. They hold us accountable for the product."

> "We already have internal AI initiatives. We need to understand what is genuinely different, and whether it works with our legacy constraints."

> "The database history is not in Git. We capture changes with an internal mechanism, so integration will not be standard."

> "Before we take this to the executive committee, we need a credible view of cost, customer effort, technical feasibility, and the value an initial phase would prove."

---

## Preliminary Needs Mentioned by the Customer

The participants mentioned interest in several possibilities. Interest does not equal validated fit.

- Reduce manual effort and repetitive validation work
- Detect risky changes before they affect customers
- Monitor critical business journeys after releases
- Improve diagnosis when a journey fails
- Introduce automated functional testing without requiring QA specialists to become developers
- Evaluate load and stability for selected workflows
- Enable the internal team to operate and expand whatever is implemented
- Establish quality and customer-impact indicators that leadership can use

---

## Customer Concerns and Decision Constraints

- **Legacy feasibility:** Can Voidr work with business logic and change history outside the normal Git path?
- **Overlap:** Why is this different from AI code review, an internal AI pipeline, or automation Northstar could build itself?
- **Customer effort:** How many Northstar people and hours would implementation require?
- **Environment and data:** What can be proven without complete test data or a universal homologation environment?
- **Operational ownership:** Who maintains the journeys, integrations, and failure triage after initial implementation?
- **Timing:** Will a new initiative distract from the modernization program?
- **Value:** Which KPI should justify the initiative — customer trust, escaped defects, rework, release confidence, team capacity, or another measure?
- **Commercial case:** The sponsor needs enough evidence to take an investment recommendation to the executive committee.

---

## Information Not Established in the Call

The following items remain unknown. This list is not exhaustive.

- Verified application inventory and architecture map
- Exact migration scope and completion definition
- Number and business value of critical journeys
- Incident volume by severity, customer, module, and cause
- Escaped-defect or change-failure baseline
- Manual validation hours by release type
- Engineering and support hours spent on rework
- Revenue, penalties, churn, or NPS impact attributable to quality issues
- Existing observability sources and data retention
- CI/CD and approval workflow for application and database changes
- Technical interface of the internal database change-capture tool
- Security, privacy, hosting, and data-residency requirements
- Environment availability, test accounts, data-reset strategy, and external sandbox coverage
- Initial-phase sponsor, working team, decision process, budget, and target date
- Which single journey would provide the best combination of business relevance and technical feasibility

---

## Your Responsibility

Use these notes to build a preliminary diagnosis — not to pretend discovery is complete.

You may make assumptions when necessary, but label them and explain what would change if they are wrong. Your proposed next step should reduce uncertainty while proving meaningful customer value.
