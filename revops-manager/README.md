<p align="center">
  <img src="https://unicorn-images.b-cdn.net/277503c3-f842-45d5-88de-69c30719b278?optimizer=gif" width="200" alt="Voidr Logo" />
</p>

<h3 align="center">From Hourly IT Services to AI-Native Operations</h3>

# RevOps Manager Technical Challenge

Take-Home Challenge

Time: 3 days | Role: RevOps Manager Senior

---

## Overview

This challenge evaluates two things:

1. **Can you solve problems under pressure?** — Same messy data crisis as the Engineer role. You need to deliver.
2. **Can you think strategically about building RevOps?** — Given where the company is headed, what should the RevOps function look like?

We're hiring a RevOps Manager to build the function from scratch. That means you need to be able to get your hands dirty AND think about the bigger picture.

---

## What is Voidr?

Before starting, you need to understand Voidr's business and where we're headed. Use these resources:

- **Website:** https://voidr.co
- **LinkedIn:** https://linkedin.com/company/voidrco
- **Product pages:** Explore all sections of the website

Your understanding of Voidr's market, product, and growth trajectory will be critical for Part 2 of this challenge.

---

## The Situation

You just joined Voidr as the first RevOps Manager. It's Monday morning. Two things happened:

### Crisis #1: The Board Meeting

> **The CEO walks up to your desk:**
> 
> "Hey, so the board meeting is Thursday. I told them I'd present our pipeline forecast. The thing is, I've been tracking deals in my head and in a spreadsheet that's... not great. I gave you access to HubSpot and exported everything I have. Can you build me a forecast I can present by Wednesday night?"

He drops a USB drive on your desk labeled `deals_export_FINAL_v3.csv`.

### Crisis #2: The Strategy Question

> Later that day, the CEO comes back:
>
> "Oh, one more thing. The board is going to ask about our path to R$ 30M ARR. Right now we're at ~R$ 12M, 100% founder-led sales. I just hired a VP Sales who starts next week. We're also about to launch a channel partnership with a healthcare ISV — that's a whole new GTM motion.
>
> I need you to think about what the RevOps function should look like to support all this. Not a 50-page strategy doc — just your thinking on what we should build, in what order, and why. The board likes to see that we have a plan."

---

## Company Context

Here's what you know about Voidr's situation:

| Dimension | Current State |
|-----------|---------------|
| **ARR** | ~R$ 12M (~30 customers) |
| **Target** | R$ 30M ARR in 18 months |
| **Sales Motion** | 100% founder-led (CEO closes every deal) |
| **Sales Team** | VP Sales starting next week, 2 BDRs ramping |
| **Average Deal** | R$ 300-500K ACV (enterprise) |
| **Sales Cycle** | 4-5 months |
| **Product Lines** | 3 lines: Synthetic Monitoring, E2E Release Assurance, Data Quality |
| **GTM Models** | Model A (Direct) today. Model B (Channel/OEM) launching in 60 days with healthcare ISV partner |
| **CRM** | HubSpot Free, barely used. CEO tracks deals in his head. |
| **RevOps** | You're it. No team, no processes, no infrastructure. |

---

## Part 1: The Forecast Crisis (Same as Engineer Challenge)

### What You Receive

Download the dataset: [deals_export_FINAL_v3.csv](./deals_export_FINAL_v3.csv)

The file is a mess:
- Duplicate deals
- Inconsistent stage names
- Mixed currencies (BRL/USD)
- Different date formats
- Owner inconsistencies
- Missing data

### What You Deliver

**1A. The Forecast (Spreadsheet)**
- Clean, deduplicated pipeline
- Weighted pipeline by stage
- Revenue projection for next 3 months
- Board-ready format

**1B. Data Cleanup Log (1 page)**
- Problems found, how you fixed them, decisions you made

**1C. What You'd Fix Next (1 page)**
- Top 3 CRM/process fixes to prevent this mess
- Why these 3 first

---

## Part 2: The Strategic Roadmap

This is what separates a Manager from an Engineer. Given the company context above, answer these questions:

### 2A. RevOps Priorities (2 pages max)

The CEO asks: *"If you could only build 5 things in the next 90 days, what would they be and why?"*

Consider:
- The VP Sales starts next week — what does he need on day 1?
- The channel partnership launches in 60 days — what infrastructure does that require?
- The board wants to see path to R$ 30M — what metrics/reporting do you need?
- You're one person — what can you realistically build vs. what needs to wait?

**Format:** Prioritized list with rationale. Not a Gantt chart — just clear thinking.

### 2B. Model A vs. Model B (1 page)

The company is about to run two GTM motions simultaneously:
- **Model A (Direct):** VP Sales + BDRs selling to enterprise, R$ 300-500K ACV
- **Model B (Channel):** Healthcare ISV partner white-labeling the product for their hospital customers

**Question:** How should the CRM and RevOps infrastructure handle both motions? Specifically:
- Same pipeline or separate pipelines?
- How do you track partner-sourced vs. direct deals?
- How do you handle rev share tracking for channel deals?
- What's the minimum you need to launch Model B without breaking Model A?

### 2C. Team & Tools (1 page)

You're building this function from scratch. 

**Answer:**
1. What tools do you need beyond HubSpot Free? (Be specific: HubSpot tier, BI tool, integrations)
2. When do you need to hire your first RevOps Analyst? What triggers that hire?
3. What's your estimated budget (tools + people) as a % of ARR?

---

## Part 3: AI Usage Documentation (Required)

Document your AI usage:
- Which tools you used
- How you used them (data cleaning, strategic thinking, research)
- Example prompts that worked well
- What you learned

---

## Evaluation Criteria

| Dimension | What We Evaluate |
|-----------|------------------|
| **Execution** | Did you deliver a usable forecast from messy data? Can you get stuff done? |
| **Prioritization** | Do your 90-day priorities make sense given the constraints? |
| **Strategic Thinking** | Do you understand the complexity of running multiple GTM motions? |
| **Practical Judgment** | Are your recommendations buildable by one person in 90 days, or are you boiling the ocean? |
| **Communication** | Is your thinking clear? Could the CEO present this to the board? |

### What We're NOT Looking For

- Perfect RevOps playbooks — we want practical thinking for THIS company
- Enterprise-grade solutions — we're a startup, act like it
- Theory without application — show us what you'd actually do
- AI-generated strategy docs — we want YOUR judgment

---

## Deliverables Summary

**Part 1: The Forecast Crisis**
1. Forecast spreadsheet (Google Sheets or Excel)
2. Data cleanup log (1 page)
3. What you'd fix next (1 page)

**Part 2: The Strategic Roadmap**
4. 90-day priorities (2 pages max)
5. Model A vs. Model B approach (1 page)
6. Team & tools plan (1 page)

**Part 3: AI Usage**
7. AI documentation (can be included in other docs)

**Total:** ~6-7 pages of writing + 1 spreadsheet

---

## Timeline

- **Duration:** 3 days from when you receive this challenge
- **Effort:** This should take approximately 5-8 hours of focused work
- **Simulated deadline:** Pretend the board meeting is Thursday and the VP Sales starts Monday

---

## How to Submit

Send an email to **hiring@jobs.voidr.co** with:

**Subject:** `[ Technical Challenge Voidr ] - Your Full Name`

**Body:**
- Brief introduction about yourself and your RevOps leadership experience (2-3 paragraphs)
- Link to your forecast spreadsheet
- Attached or linked: all written deliverables

---

## What Happens Next

### If you pass this stage

You'll receive an email with a link to schedule a 60-minute session with our CEO.

During this session, you'll:
- Walk through your forecast and strategic roadmap
- Discuss trade-offs in your prioritization decisions
- Role-play: "The VP Sales just asked you why there's no MEDDIC tracking in the CRM. What do you tell him?"
- Talk about how you've built RevOps from scratch before

### If you don't pass this stage

You'll receive structured, honest feedback explaining why it wasn't a match this time.

---

## Questions?

If anything is unclear, reach out via email: **hiring@jobs.voidr.co**

Asking good questions is a positive signal, not a negative one.

---

## About the Role

As RevOps Manager at Voidr, you'll build the entire revenue operations function from scratch. You'll own the CRM, forecasting, pipeline processes, and reporting — and eventually hire and lead a team.

You'll report to the VP Sales with a dotted line to the CEO. You'll work across Sales, AI Deployment (CS), and Marketing to make sure every process works and every number is trustworthy.

This is a build-from-zero role at a company transitioning from founder-led sales to a structured GTM engine. If you've done this before and want to do it again, we'd love to talk.

Interested? Check the full job description at [voidr.co/careers](https://voidr.co/pt-br/empresa/carreiras/revops-manager-senior)

---

**Note:** This challenge is used in actual hiring processes. We expect candidates to develop their own original solutions.
