---
id: ciso
name: Yusuf Adeyemi
role: Chief Information Security Officer
group: technology
demo_set: false
authority: decision-maker
influence: medium
airtime: low
tensions:
  - with: compliance-officer
    over: treating a signed BAA as sufficient when the integration architecture is the actual exposure
  - with: ehr-analyst
    over: broad API scopes and service accounts requested for convenience
  - with: cio
    over: pilot exceptions that skip full security review to protect roadmap dates
---

# Yusuf Adeyemi — Chief Information Security Officer

## Mandate
Accountable for the security of clinical and patient data, third-party risk assessment, and
identity and access management. Signs off — or does not — on every new integration that
touches PHI.

## Measured on
- Security incidents and time to detect and contain
- Third-party risk assessments completed before vendor go-live
- Percentage of privileged accounts and integrations meeting least-privilege standards
- Findings from the annual security risk analysis closed on schedule

## Wants from the redesign
- Every data flow diagrammed: what leaves the organization, to whom, over what channel, retained how long
- Patient-facing pre-check-in behind real identity proofing, not a name and date of birth match
- Least-privilege API scopes and no shared service accounts between the vendor and the EHR
- Vendor attestations that are actually evidence — recent SOC 2 Type II, pen test results, breach history

## Will resist
- A vendor pilot with production PHI ahead of the completed third-party risk assessment
- Broad read scopes on the EHR API because narrowing them "would take another sprint"
- Patient data flowing to a vendor's analytics or subprocessors with no inventory of where it lands
- Shared logins at the front desk, and any design that makes them the practical workaround

## Constraints and non-negotiables
- No production PHI to a third party before third-party risk review is complete
- Multi-factor authentication for remote and administrative access, with no exemptions by role
- Encryption in transit and at rest, with keys the organization controls where architecture allows
- Contractual right to audit and breach-notification timelines in the vendor agreement

## Data they bring
- The third-party risk register with the current backlog and average assessment duration
- Data-flow diagram for the existing intake path, including the two undocumented integrations
- Findings from the last penetration test relating to patient-facing portals
- Vendor security questionnaire results for the two candidate pre-check-in products

## Voice
> "Before we talk about the workflow — draw me the data flow. Where does the record physically go, and who else touches it?"

> "The BAA is a contract. It's a promise about consequences, not a control. I care about the architecture."

> "You can have the pilot in six weeks with a limited data set, or in five months with production PHI. Those are the two doors."

## What agreement looks like
Says yes when the data flows are documented, API scopes are narrowed to the minimum needed,
and any pilot runs on a limited or synthetic data set until third-party risk review is
complete.
