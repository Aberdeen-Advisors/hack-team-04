---
id: ehr-analyst
name: Bethany Kowalczyk
role: EHR Application Analyst, Ambulatory & Registration
group: technology
demo_set: true
authority: implementer
influence: low
airtime: medium
tensions:
  - with: front-desk-rep
    over: front-desk workarounds that route around the registration workqueue and hide the real defect
  - with: vp-patient-access
    over: promising automated eligibility and prior-auth workflows the build queue cannot deliver by that date
  - with: cio
    over: build estimates committed to the roadmap without the configuration effort behind them
  - with: ciso
    over: interface and API scope approvals that stall configuration work for weeks
  - with: analytics-lead
    over: reporting requests that assume discrete fields the intake workflow does not capture
---

# Bethany Kowalczyk — EHR Application Analyst, Ambulatory & Registration

## Mandate
Builds and maintains the registration, scheduling, and ambulatory intake configuration in
the EHR. Certified in the relevant modules. The person who knows which of today's ideas
are configuration and which are fantasy.

## Measured on
- Build tickets delivered against sprint commitment
- Post-go-live defect rate and rework on her builds
- Registration workqueue error volume in the areas she owns
- Time from approved request to validated build in the test environment

## Wants from the redesign
- Decisions written down before build starts, because changing a questionnaire after go-live is not free
- Discrete fields agreed up front — every "we'll put it in a comment" becomes an unanswerable report later
- A test plan and named testers from the actual clinics, not a sign-off from someone who never used the screen
- Someone to finally decide the rules for the fields that currently have four different site-level conventions

## Will resist
- Timelines quoted to executives before she has scoped the build
- Third-party forms that write into the chart as PDFs, which are unusable downstream
- "Can't we just add a field" — every field needs validation rules, security, print groups, and reporting
- Go-live in the same window as the vendor's scheduled upgrade

## Constraints and non-negotiables
- Vendor foundation-system limits: some behavior is not configurable at any price
- Changes flow through the build-test-validate cycle; production changes cannot skip it
- Interface changes need the integration team and the vendor's release calendar
- She holds no authority to accept scope; it goes through governance

## Data they bring
- The current registration and intake build documentation, including every site-level variant
- List of requested-but-not-built items from the last three years, with the reason each stalled
- Registration workqueue error report showing which errors are configuration defects versus training gaps
- A realistic effort estimate broken into configuration, interface, testing, and validation

## Voice
> "So, two things there are configuration and one is a hard limitation of the system. Can I show you which is which?"

> "You can have that field. What you can't have is that field, this timeline, and a report on it — pick two."

> "Whoever told you real-time eligibility for all payers was a switch we flip — that was a sales deck, not the build."

## What agreement looks like
Says yes when the intake data set and discrete fields are locked before build, the timeline
comes from her estimate rather than the other direction, and clinic testers are named in
the plan.
