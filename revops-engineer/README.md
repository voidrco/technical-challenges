<p align="center">
  <img src="https://unicorn-images.b-cdn.net/277503c3-f842-45d5-88de-69c30719b278?optimizer=gif" width="200" alt="Voidr Logo" />
</p>

<h3 align="center">From Hourly IT Services to AI-Native Operations</h3>

# RevOps Engineer Technical Challenge

Take-Home Challenge

Time: 3 days | Role: RevOps Engineer Mid

---

## Overview

This challenge evaluates your ability to take messy, real-world data and turn it into actionable insights under pressure. You'll clean up a chaotic CRM export, build a forecast the CEO can present to the board, and show us how you think about fixing broken processes.

This is not a theoretical exercise — it's the kind of fire drill that happens in early-stage startups. We want to see if you can deliver when it matters.

---

## What is Voidr?

Before starting the challenge, you need to understand what Voidr does. Use the following resources:

- **Website:** https://voidr.co
- **LinkedIn:** https://linkedin.com/company/voidrco
- **Product pages:** Explore all sections of the website

Your understanding of Voidr's business will help you make better decisions when the data doesn't give you clear answers.

---

## The Situation

You just joined Voidr as the first RevOps Engineer. It's Monday. Here's what happened:

> **The CEO walks up to your desk at 9am:**
> 
> "Hey, so... the board meeting is Thursday. I told them I'd present our pipeline forecast and unit economics. The thing is, I've been tracking deals in my head and in a spreadsheet that's... not great. I just gave you access to HubSpot and exported everything I have. Can you build me a forecast I can actually present? I need it by Wednesday night."
>
> He drops a USB drive on your desk labeled `deals_export_FINAL_v3.csv` and walks away.

You open the file. It's a mess.

---

## What You Receive

Download the dataset here: [deals_export_FINAL_v3.csv](./deals_export_FINAL_v3.csv)

```csv
deal_id,company_name,deal_name,amount,currency,stage,created,expected_close,actual_close,owner,source,segment,notes
D001,FinBank SA,AI Test Automation - Core,280000,BRL,Closed Won,2025-06-15,2025-10-15,2025-10-28,milson@voidr.co,Founder Network,Enterprise,
D002,HealthPlus Tech,QA Platform - Patient Portal,95000,BRL,Won,20/07/2025,2025-11-01,15-Nov-2025,Marina Silva,Inbound,Mid-Market,
D003,LogiTech Express,Test Automation - Logistics,180000,BRL,Negotiation,2025-08-10,,, Marina,Outbound BDR,Enterprise,waiting for procurement
D004,InsureSafe Digital,AI Testing - Claims,320000,BRL,Proposal Sent,2025-09-01,2025-12-15,,milson,Partner,Enterprise,
D005,RetailMax,QA Automation - E-commerce,75000,BRL,Discovery,2025-09-15,,,marina.silva@voidr.co,inbound,Mid Market,
D006,AutoParts Online,Test Coverage - Inventory,110000,BRL,discovery,2025-10-01,2026-01-15,,Marina Silva,Outbound BDR,Mid-Market,
D007,NeoCredit Fintech,AI Agents - Credit Engine,50000,USD,Proposal,2025-08-20,2025-11-30,,Milson,Event,enterprise,hot deal
D008,MedDevice Corp,QA Platform - FDA Compliance,350000,BRL,Technical Validation,2025-07-01,2025-09-30,,milson@voidr.co,Outbound BDR,Enterprise,
D009,EduTech Brasil,Test Automation - LMS,65000,BRL,Lost,2025-05-10,,2025-09-20,Marina,Inbound,Mid-Market,chose competitor
D010,PayFlow Systems,AI Testing - Payment Gateway,195000,BRL,Closed Won,2025-04-01,2025-08-01,2025-08-15,milson,Founder Network,Enterprise,
D011,CloudBank Digital,QA Automation - Digital Bank,290000,BRL,Negociação,2025-10-15,2026-02-28,,Marina Silva,Outbound BDR,Enterprise,
D012,FoodChain Logistics,Test Platform - Supply Chain,85000,BRL,Discovery,2025-11-01,,,marina,Inbound,Mid-Market,
D013,NeoCredit Fintech,AI Agents - Credit Engine,250000,BRL,Proposal Sent,2025-08-20,2025-11-30,,Milson,Event,Enterprise,same deal as D007 - corrected value
D014,TechManufatura SA,QA Industrial,45000,USD,Nego,2025-10-20,2026-01-30,,Marina,Outbound,enterprise,
D015,DataVault Analytics,Data Validation Suite,180000,BRL,Proposal Sent,2025-10-01,2025-12-20,,milson@voidr.co,Founder Network,Enterprise,
D016,HealthPlus Tech,QA Platform Expansion,120000,BRL,Negotiation,2025-11-10,2026-01-15,,Marina Silva,Expansion,Mid-Market,upsell from D002
D017,FastRetail Group,Synthetic Monitor - Checkout,230000,BRL,Discovery,2025-10-20,,,Marina,Outbound BDR,Enterprise,
D018,UrbanMobility Tech,QA Platform - Ride Sharing,310000,BRL,discovery,2025-12-10,2026-03-15,,marina.silva@voidr.co,Inbound,Enterprise,
D019,AgroTech Solutions,Data Quality Dashboard,95000,BRL,Closed Won,2025-06-01,2025-10-01,2025-10-05,Milson,Founder Network,Mid-Market,
D020,SecureID Fintech,AI Testing - KYC Flow,470000,BRL,Negotiation,2025-09-05,2025-12-01,,milson,Event,Enterprise,
D021,MedDevice Corp,QA Platform - FDA Compliance,350000,BRL,Negotiation,2025-07-01,2025-11-30,,milson@voidr.co,Outbound BDR,Enterprise,duplicate? same company as D008
```

**The problems you'll find:**
- Duplicate deals (same deal entered twice with different IDs)
- Inconsistent stage names ("Negotiation", "Negociação", "Nego", "Proposal", "Proposal Sent")
- Mixed currencies (BRL and USD)
- Different date formats
- Owner sometimes is email, sometimes is name
- Segment inconsistencies ("Mid-Market", "Mid Market", "enterprise", "Enterprise")
- Deals that should be closed but aren't marked as such
- Missing expected close dates
- One deal with obviously wrong value (D007 vs D013 - same deal)

---

## What You Deliver

### Part 1: The Forecast (Spreadsheet)

Build a forecast the CEO can present to the board on Thursday.

**Requirements:**
- Clean, deduplicated pipeline
- Weighted pipeline by stage (you define the probabilities)
- Revenue projection for next 3 months (Nov, Dec, Jan)
- Summary metrics: total pipeline, weighted pipeline, average deal size, expected closes
- Must be in a format a non-technical CEO can present (clean, clear, no jargon)

**Deliver:** Google Sheets link or Excel file

---

### Part 2: Data Cleanup Log (1-2 pages)

Document what you found and what you did about it.

| Problem Found | What You Did | Why |
|---------------|--------------|-----|
| (example) Duplicate deal D007/D013 | Kept D013 (R$ 250K), deleted D007 (USD 50K was clearly wrong) | D013 had "corrected value" in notes |

**Include:**
- Every data quality issue you found
- How you resolved each one
- Decisions you made when there was no clear right answer

---

### Part 3: What You'd Fix Next (1 page)

You've delivered the forecast. The fire is out. Now what?

**Answer:**
1. What are the **top 3 things** you'd fix in the CRM/process to prevent this mess from happening again?
2. For each one: **why this before the others?**
3. **How long** would each take to implement?

---

### Part 4: AI Usage Documentation (Required)

You **must** use AI tools to complete this challenge. Document your AI usage:

- Which AI tools you used
- How you used them (data cleaning, formula help, prioritization thinking)
- Example prompts that worked well
- What you learned

---

## Evaluation Criteria

| Dimension | What We Evaluate |
|-----------|------------------|
| **Delivery Under Pressure** | Did you produce a usable forecast from messy data? Is it board-ready? |
| **Data Cleaning Skills** | Did you catch the problems? Were your fixes sensible? Did you document your decisions? |
| **Prioritization** | Do your "fix next" recommendations make sense? Can you explain why? |
| **Communication** | Is your work clear enough for a non-technical CEO to understand and present? |
| **AI Usage** | Did you use AI strategically to move faster? |

### What We're NOT Looking For

- Perfect forecasting methodology — we want practical, defensible numbers
- Beautiful dashboards — clarity beats aesthetics
- Boiling the ocean — we want to see you focus on what matters

---

## Deliverables Summary

1. **Forecast spreadsheet** — Google Sheets or Excel
2. **Data cleanup log** — 1-2 pages, PDF or Google Doc
3. **What you'd fix next** — 1 page
4. **AI usage documentation** — can be included in the cleanup log

---

## Timeline

- **Duration:** 3 days from when you receive this challenge
- **Effort:** This should take approximately 3-5 hours of focused work
- **Simulated deadline:** Pretend the board meeting is Thursday. Deliver something usable, not perfect.

---

## How to Submit

Send an email to **hiring@jobs.voidr.co** with:

**Subject:** `[ Technical Challenge Voidr ] - Your Full Name`

**Body:**
- Brief introduction about yourself and your RevOps experience (2-3 paragraphs)
- Link to your forecast spreadsheet
- Attached or linked: data cleanup log, recommendations, and AI usage doc

---

## What Happens Next

### If you pass this stage

You'll receive an email with a link to schedule a 45-minute session with one of our founders.

During this session, you'll:
- Walk through your forecast and defend your assumptions
- Explain how you'd handle a specific messy data scenario
- Talk about how you've solved similar problems in the past

### If you don't pass this stage

You'll receive structured, honest feedback explaining why it wasn't a match this time.

---

## Questions?

If anything is unclear, reach out via email: **hiring@jobs.voidr.co**

Asking good questions is a positive signal, not a negative one.

---

## About the Role

As a RevOps Engineer at Voidr, you'll build and maintain the operational infrastructure that powers our revenue growth. You'll own the CRM, clean up data messes, build dashboards, automate processes, and make sure the sales team has what they need to close deals.

This is a hands-on role in a fast-moving startup. You'll work directly with the CEO, AEs, and BDRs to ensure every process works and every number is trustworthy.

Interested? Check the full job description at [voidr.co/careers](https://voidr.co/pt-br/empresa/carreiras/revops-engineer-mid)

---

**Note:** This challenge is used in actual hiring processes. We expect candidates to develop their own original solutions.
