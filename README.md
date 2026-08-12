<div align="center">

# ORBIT

### AI Workshop Facilitation by Aberdeen Advisors

**Prepare with intent. Guide the room in real time. Turn discussion into action.**

![Python](https://img.shields.io/badge/Python-3.12-09375F?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.40%2B-09375F?style=flat-square&logo=streamlit&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-Optional-44B0B1?style=flat-square&logo=openai&logoColor=09375F)
![Status](https://img.shields.io/badge/Status-Demo%20Prototype-E8F4F4?style=flat-square&labelColor=09375F&color=44B0B1)

</div>

---

## Overview

Orbit is an AI-assisted workspace for designing, facilitating, and documenting complex workshops. The prototype demonstrates one complete workflow for a healthcare process-redesign session: establish context, generate a practical workshop plan, support the facilitator with a live control tower, guide the group through a diverge–converge activity, and produce an executive-ready readout.

Orbit supports the human facilitator; it does not replace one. Its role-based agents organize evidence, surface tensions, distinguish decisions from proposals, and help turn discussion into accountable next steps.

The included Northstar Health System scenario, participant names, transcript, and outputs are entirely fictional.

## Product workflow

### 1. Prepare

Configure the workshop using:

- Client and organizational context
- Workshop intent and healthcare setting
- Objective, constraints, and success criteria
- Participant roles and perspectives
- AI focus areas, guardrails, and exclusions
- Session duration and active facilitation agents

Orbit generates a timed agenda, opening questions, interactive exercises, pre-work, required materials, expected decisions, and an output checklist.

### 2. Live Workshop

The facilitator-facing control tower transforms a simulated transcript into:

- Session pacing and status signals
- Key discussion points and emerging themes
- Confirmed decisions and proposals requiring confirmation
- Tensions, competing perspectives, and suggested facilitator moves
- Follow-up questions and role-specific guidance
- Editable action and parking-lot trackers
- Dependencies and unresolved questions

An alternate **Diverge → Converge** mode extracts ideas as sticky notes, clusters overlapping concepts, develops potential solutions, and supports editable prioritization.

### 3. Readout & Action Plan

Orbit consolidates workshop evidence into a client-ready readout containing:

- Executive summary
- Confirmed decisions
- Recommended future-state direction
- Risks and mitigations
- Success measures
- Action plan with owners, due dates, and status
- Parking-lot items
- Full transcript summary

The result can be downloaded as Markdown for further refinement or conversion into other deliverables.

## Agent system

| Agent | Primary responsibility | Phase |
|---|---|---|
| **Orchestration Agent** | Validates context, coordinates specialist work, reconciles outputs, and flags gaps | All phases |
| **Healthcare SME Agent** | Applies patient, clinical workflow, operational, safety, and compliance lenses | All phases |
| **Workshop Planner Agent** | Creates the agenda, pre-work, exercises, materials, and output checklist | Prepare |
| **Facilitator Agent** | Recommends prompts, follow-ups, pacing interventions, and parking-lot items | Live |
| **Insight Agent** | Detects themes, root causes, consensus, tensions, risks, and opportunities | Live |
| **Decision Agent** | Separates proposals from confirmed decisions and tracks execution | Live + Readout |
| **Deliverable Agent** | Converts structured evidence into polished executive outputs | Readout |

The hackathon prototype models these roles in one lightweight application service. They are not independently deployed autonomous services.

## Confidence convention

Every generated output carries an indicative confidence label:

| Level | Threshold | UI treatment |
|---|---:|---|
| High | 85–100% | Green |
| Medium | 70–84% | Yellow |
| Low | Below 70% | Red |

These values are **illustrative demo scores**, not calibrated probabilities or measured model reliability. A production confidence system would require evaluation data, evidence coverage rules, historical performance, and organization-specific validation.

## Technology

- **Interface:** Streamlit
- **Runtime:** Python
- **AI integration:** OpenAI Responses API, optional
- **Local configuration:** `python-dotenv`
- **State:** Streamlit session state
- **Default operation:** Deterministic Demo mode with no API key

```text
                         ┌─────────────────────┐
                         │   Streamlit UI      │
                         │ Prepare · Live ·    │
                         │ Readout             │
                         └──────────┬──────────┘
                                    │
                         ┌──────────▼──────────┐
                         │ WorkshopAI service  │
                         └───────┬───────┬─────┘
                                 │       │
                    ┌────────────▼─┐   ┌─▼─────────────────┐
                    │ Demo fixtures │   │ OpenAI Responses  │
                    │ Default path  │   │ Optional path     │
                    └───────────────┘   └───────────────────┘
```

## Repository structure

```text
.
├── app.py                  # Streamlit interface and workflow state
├── ai_service.py           # Demo/API generation service
├── sample_data.py          # Fictional scenario and deterministic outputs
├── requirements.txt        # Python dependencies
├── .env.example            # Optional local API configuration template
├── .streamlit/
│   └── config.toml         # Orbit/Aberdeen application theme
└── README.md
```

## Run locally

### Windows PowerShell

Install Python 3.12 if it is not already available:

```powershell
winget install --id Python.Python.3.12 -e
```

Restart VS Code, open the project folder, and run:

```powershell
py -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

### macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501). Leave **Demo mode** selected for the credential-free walkthrough.

## Optional OpenAI configuration

The application works without an API key. To enable dynamic generation locally:

1. Copy `.env.example` to `.env`.
2. Add your key and an available text model:

```dotenv
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-5.6-terra
```

3. Restart the application and select **OpenAI API** in the sidebar.

Never commit `.env` or an API key. The repository’s `.gitignore` excludes local secret files.

## Deploy the demo

The simplest demonstration deployment is [Streamlit Community Cloud](https://share.streamlit.io/):

1. Connect the GitHub repository.
2. Select the `main` branch.
3. Set the entry point to `app.py`.
4. Select Python 3.12 in advanced settings.
5. Deploy.

Demo mode needs no hosted secret. If API mode is enabled, store the API key in the hosting platform’s secret manager—never in the repository.

## Suggested demonstration

1. **Prepare:** review the fictional Northstar context, agent roles, guardrails, and generated agenda.
2. **Control Tower:** analyze the sample transcript and highlight pacing, tensions, confirmation prompts, actions, and dependencies.
3. **Interactive Activity:** switch to Diverge → Converge and show idea extraction, clustering, solutions, and prioritization.
4. **Readout:** generate and download the executive summary and action plan.

## Security and responsible use

This repository is a demonstration prototype and is **not approved for protected health information, confidential client material, or production healthcare workflows**.

- Do not enter real patient information or PHI.
- Do not use Streamlit Community Cloud to process sensitive health information.
- Do not interpret outputs as medical advice or clinical protocols.
- Human facilitators must validate decisions, owners, dates, and recommendations.
- Production use requires organization-approved hosting, authentication, authorization, audit logging, encryption, retention controls, monitoring, and vendor review.

For real healthcare or client data, deploy only in an Aberdeen-approved enterprise environment.

## Prototype boundaries and roadmap

The current prototype intentionally favors demo reliability over infrastructure complexity.

**Implemented**

- Three-stage workshop workflow
- Seven role-based agents
- Deterministic Demo mode
- Optional OpenAI generation
- Simulated transcript analysis
- Live facilitator control tower
- Diverge–converge activity
- Decisions, actions, dependencies, and parking lot
- Confidence labels
- Markdown readout export

**Future state**

- Microsoft Teams or Zoom transcript integration
- Automatic agenda countdown and pacing alerts
- Participant contribution analysis
- Document, whiteboard, chat, and polling ingestion
- Persisted workshop history and organizational context
- Evidence-backed confidence calibration
- Authentication and enterprise access controls
- PowerPoint, PDF, Word, and structured-data exports
- Cross-industry specialist-agent libraries

## Brand system

Orbit follows the Aberdeen Advisors web adaptation:

- Aberdeen Blue `#09375F`
- Aberdeen Teal `#44B0B1`
- Onyx `#404040`
- Poppins with Calibri fallback
- Restrained white surfaces, generous whitespace, and thin teal accents

---

<div align="center">

**ORBIT**  
*AI Workshop Facilitation by Aberdeen Advisors*

Demo prototype · August 2026

</div>
