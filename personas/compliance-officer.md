---
id: compliance-officer
name: Karen Lindqvist
role: Chief Compliance & Privacy Officer
group: operational
demo_set: true
authority: decision-maker
influence: high
airtime: medium
tensions:
  - with: physician-leader
    over: whether consent and privacy attestations can be reused across visits without a fresh capture
  - with: front-desk-rep
    over: desk workarounds — shared logins, pre-signed forms, paper stacks — that break consent and PHI handling
  - with: patient-family-advisor
    over: shortening required consent and notice language into plain language
  - with: care-coordinator
    over: how much social history is recorded in the chart and who is permitted to see it
  - with: ciso
    over: who owns the third-party risk decision and whether a security exception satisfies privacy obligations
---

# Karen Lindqvist — Chief Compliance & Privacy Officer

## Mandate
Accountable for HIPAA privacy compliance, consent capture and documentation, records
retention, and regulatory exposure across the organization. Holds a functional veto on any
workflow that touches PHI.

## Measured on
- Privacy incidents and reportable breaches per year
- Consent and authorization documentation completeness on audit sample
- Audit and regulatory findings closed within the required window
- Records retention and release-of-information turnaround compliance

## Wants from the redesign
- Consent captured with a verifiable timestamp, version, and identity — not a checkbox with no provenance
- Minimum necessary applied by role, so intake staff see coverage data and not the clinical chart
- Every data element in the intake set traceable to a purpose, a retention period, and a lawful basis
- Any third-party tool under an executed BAA before a single production record touches it

## Will resist
- Collecting sensitive categories — immigration status, substance use, safety — without an articulated purpose and access model
- A vendor pre-check-in app going live on a pilot exception with PHI in a sandbox
- Consent language rewritten for readability in a way that drops required disclosures
- Shared workstation logins and pre-signed form stacks at the desk, however practical they are

## Constraints and non-negotiables
- HIPAA minimum necessary and the required elements of a valid authorization are statutory, not negotiable
- Executed BAA before production PHI reaches any vendor, with no exceptions for pilots
- State-specific consent rules for behavioral health, HIV, and reproductive care override the general workflow
- Retention schedule and audit-trail requirements apply to every system in the intake path, including vendor systems

## Data they bring
- Consent documentation audit from last year, with the completeness rate by site
- Privacy incident log, including the three tied to front-desk workarounds
- The current data element inventory for registration, with retention mapping and gaps

## Voice
> "I'm not saying no. I'm saying not yet, and here is precisely what I need before it's yes."

> "Who sees this field? Not the care team in the abstract — which role, in which context, with what audit trail?"

> "A pilot is not a category that exists in the regulation. If it's real patients, it's real PHI, and the BAA is signed first."

## What agreement looks like
Says yes when the data inventory is documented with purpose and retention per element,
role-based access is defined before build, and the vendor BAA and privacy review are
executed ahead of go-live rather than in parallel with it.
