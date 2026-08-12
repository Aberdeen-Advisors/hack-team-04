# Stakeholder Personas

This folder holds the cast of the workshop. Each file describes one stakeholder who
would realistically be in the room for a patient-intake redesign at a US ambulatory
healthcare organization — what they are accountable for, what they want, what they
will fight, and how they actually talk.

These are **input data for the AI Workshop Designer**, not documentation. The app
reads them; nobody has to read them aloud.

## What a persona file is

One markdown file per stakeholder. YAML frontmatter at the top holds the machine-readable
facts (role, power, who they clash with). Below that, fixed markdown sections hold the
human-readable substance. Filenames are the persona `id` in kebab-case: `front-desk-rep.md`.

The people are fictional. No real organization is named anywhere in this folder.

## The three ways the app uses them

1. **Agenda tailoring.** Given the personas attending, the app shapes the agenda to the
   room: it weights time toward the topics the attendees are measured on, plans who to
   call on and when, and protects airtime for people who will not take it themselves
   (`airtime: low` — the front-desk rep, the contact-center lead). `authority` and
   `influence` tell it where a decision can actually be made versus only advised.

2. **Disagreement detection.** The `tensions` blocks form a graph of known fault lines.
   While the workshop is running, the app matches live discussion against that graph and
   surfaces conflicts as they emerge — "this is the financial-clearance-timing
   disagreement between Patient Access and the front desk" — instead of letting them get
   smoothed over. It also uses the graph to suggest follow-up questions and to make sure
   the readout records the real disagreements, not just the consensus.

3. **Synthetic dry-run transcript.** Before the real session, the app generates a fake
   workshop from these files so the team can rehearse and demo. The **Voice** section is
   what makes that transcript sound like people rather than one narrator — three sample
   lines per persona, in their own register.

## Field reference

| Field | Type | Allowed values / notes |
|---|---|---|
| `id` | string | kebab-case, must match the filename |
| `name` | string | fictional first + last name |
| `role` | string | job title as it would appear on a badge |
| `group` | enum | `clinical`, `operational`, `technology`, `cross-cutting` |
| `demo_set` | boolean | `true` for the six personas used in the demo, else `false` |
| `authority` | enum | `sponsor`, `decision-maker`, `influencer`, `implementer`, `advisory` |
| `influence` | enum | `high`, `medium`, `low` — formal power in the organization |
| `airtime` | enum | `high`, `medium`, `low` — how much they speak unprompted |
| `tensions[].with` | id | the `id` of another persona in this folder |
| `tensions[].over` | string | the substance of the disagreement, in this persona's words |

Markdown sections, in order and always present: `Mandate`, `Measured on`,
`Wants from the redesign`, `Will resist`, `Constraints and non-negotiables`,
`Data they bring`, `Voice`, `What agreement looks like`.

## The reciprocity rule

**Every tension must be mirrored.** If `front-desk-rep` lists a tension with
`vp-patient-access`, then `vp-patient-access` must list a tension with `front-desk-rep` —
worded from their side, because the two sides of a real disagreement never describe it the
same way. The `over:` text should differ; the pairing must not.

An unmirrored tension is a bug: the disagreement graph becomes directional and the app
will surface a conflict for one participant and miss it for the other. There are currently
**35 tension pairs** across 17 personas, and every persona has at least two.

## Adding or editing a persona

1. Copy `_schema.md`, fill every field and section, name the file after the `id`.
2. Add your tensions — and add the mirrored entry to each counterpart's file.
3. Re-run the consistency check: every `with:` id resolves to a real file, and every
   tension is reciprocal.
