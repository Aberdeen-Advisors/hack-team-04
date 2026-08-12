ROLES = {
    "Orchestration Agent": {"icon": "🎛️", "phase": "All phases", "job": "Validate context, route work, reconcile outputs, and flag gaps.", "output": "Routing plan, status, conflicts, gaps, and next agent action"},
    "Healthcare SME Agent": {"icon": "🩺", "phase": "All phases", "job": "Apply patient, clinical workflow, operations, safety, and compliance lenses.", "output": "Healthcare impacts, risks, questions, and KPIs"},
    "Workshop Planner Agent": {"icon": "🗺️", "phase": "Prepare", "job": "Build the agenda, pre-work, materials, exercises, and expected outputs.", "output": "Workshop plan and output checklist"},
    "Facilitator Agent": {"icon": "🎤", "phase": "Live", "job": "Keep discussion focused, balanced, inclusive, and action-oriented.", "output": "Prompts, follow-ups, time alerts, engagement alerts, and parking lot"},
    "Insight Agent": {"icon": "💡", "phase": "Live", "job": "Detect themes, root causes, consensus, tensions, risks, and opportunities.", "output": "Evidence-grounded insight summary"},
    "Decision Agent": {"icon": "✅", "phase": "Live + Readout", "job": "Separate proposals from confirmed decisions and track execution.", "output": "Decision, action, question, dependency, and escalation logs"},
    "Deliverable Agent": {"icon": "📄", "phase": "Readout", "job": "Turn workshop evidence into polished executive materials.", "output": "Readout, action plan, RAID log, and PowerPoint outline"},
}

DEFAULT_ROLES = list(ROLES.keys())

SAMPLE = {
    "client_name": "Northstar Health System",
    "workshop_type": "Future-state design",
    "healthcare_setting": "Ambulatory care · outpatient clinics",
    "success_criteria": "Reduce check-in time\nMaintain medication accuracy\nPreserve equitable access\nLeave with pilot owners and measures",
    "ai_focus": "Medication accuracy, patient access, staff burden, privacy, and executable decisions",
    "ai_exclusions": "Do not provide medical advice. Do not invent agreement, owners, dates, or clinical protocols.",
    "live_objective": "Resolve the minimum safe intake dataset and identity-verification approach",
    "goal": "Redesign outpatient patient intake to reduce check-in time and administrative burden while maintaining clinical safety, accessibility, and privacy.",
    "participants": """Dr. Maya Lee — Clinical lead
Sarah Martinez — Front-desk operations
Mike Chen — Digital product & EHR
Aisha Johnson — Patient experience
Tom Reynolds — Compliance & privacy""",
    "constraints": """Must work with the existing EHR
Limited front-desk staffing and training time
HIPAA and organizational privacy requirements
Must support low digital literacy and multiple languages
Pilot needs to launch within 8 weeks""",
    "transcript": """Dr. Lee: Medication accuracy is the safety-critical piece. We should collect the history before the visit.
Sarah: I support pre-visit intake, but our completion rate will fall if the form gets longer. Staff cannot chase every patient.
Mike: We can retrieve the current medication list from the EHR and ask patients to confirm changes rather than re-enter everything.
Aisha: That helps digitally confident patients, but we need a clear assisted path and translated instructions. A smartphone cannot be the only door.
Tom: We should avoid collecting extra information just because the form makes it easy. Consent language and data retention need review.
Dr. Lee: I’m comfortable with verification, provided clinical staff see what changed and unresolved items are flagged.
Sarah: Let’s pilot SMS pre-check-in for two clinics, keep a short assisted check-in at the desk, and measure completion and average check-in time.
Mike: I can scope the EHR integration this week. We still need to decide whether identity verification happens before the link opens or inside the flow.
Aisha: We should test the prototype with older adults and patients who prefer Spanish before launch.
Tom: Agreed, and compliance can review the prototype before usability testing.""",
}


def mock_agenda(duration=90, roles=None):
    base = [
        ("Frame the outcome", .11, "Align on success, scope, and non-negotiables.", "Facilitator Agent"),
        ("Map today’s journey", .16, "Locate delay, rework, and safety-sensitive moments.", "Healthcare SME Agent"),
        ("Hear every perspective", .16, "Surface clinical, operational, technical, and privacy needs.", "Insight Agent"),
        ("Design the future state", .28, "Create a feasible pre-visit and assisted check-in flow.", "Workshop Planner Agent"),
        ("Stress-test the concept", .17, "Test trade-offs against safety, inclusion, feasibility, and privacy.", "Healthcare SME Agent"),
        ("Decide and mobilize", .12, "Capture choices, owners, measures, and next steps.", "Decision Agent"),
    ]
    minutes = [round(duration * item[1]) for item in base]
    minutes[-1] += duration - sum(minutes)
    selected = roles or DEFAULT_ROLES
    return {
        "agenda": [{"title": x[0], "minutes": minutes[i], "purpose": x[2], "owner_role": x[3]}
                   for i, x in enumerate(base)],
        "opening_questions": [
            "What must be true at the end of this session for it to be worth everyone’s time?",
            "Where does today’s process create the greatest risk or avoidable effort?",
            "Which constraint should become a design principle?",
        ],
        "exercise": {"name": "Future-state trade-off sprint", "instructions": "Small groups sketch a future-state flow, then score it against safety, ease, inclusion, feasibility, and privacy. Combine the strongest elements.", "output": "One shared flow, explicit trade-offs, and unresolved assumptions."},
        "role_outputs": [{"role": name, "output": ROLES[name]["output"]} for name in selected if name in ROLES],
        "pre_work": ["Current intake process map", "Baseline check-in measures", "Known EHR constraints", "Participant review of the objective"],
        "materials": ["Current-state journey map", "Future-state process canvas", "Voting matrix", "Decision and action log"],
        "expected_decisions": ["Pilot scope", "Identity-verification pattern", "Minimum safe dataset", "Prototype and validation owners"],
        "output_checklist": ["Future-state direction", "Confirmed decisions", "Open-question log", "Prioritized action plan", "Success measures"],
    }


def mock_analysis(roles=None):
    selected = roles or DEFAULT_ROLES
    insights = {
        "Orchestration Agent": "Engage Healthcare SME, Facilitator, Insight, and Decision agents; not yet ready for deliverable generation.",
        "Healthcare SME Agent": "Medication exceptions require clinical review; compliance should validate the identity flow.",
        "Workshop Planner Agent": "Protect time for identity verification and minimum-data decisions.",
        "Facilitator Agent": "Confirm the pilot direction, then resolve the two remaining design choices.",
        "Insight Agent": "The central trade-off is completeness versus completion, with equitable access as a constraint.",
        "Decision Agent": "Three explicit decisions and four accountable next steps are supported by the transcript.",
        "Deliverable Agent": "Not ready: identity verification and minimum-data questions remain open.",
    }
    return {
        "session_status": {"on_track": True, "status_note": "On track — direction aligned; two choices still need resolution.", "current_topic": "Future-state design"},
        "key_points": [
            "The group favors pre-visit digital intake paired with assisted clinic check-in.",
            "Medication verification is preferred over re-entering the full list.",
            "Accessibility, minimal data collection, and visible clinical exceptions are core requirements.",
        ],
        "decisions": [
            "Pilot SMS pre-check-in in two clinics while retaining assisted front-desk check-in.",
            "Prototype EHR-based medication verification and flag unresolved changes for clinical review.",
            "Test with older adults and Spanish-preferring patients before launch.",
        ],
        "proposed_decisions": [{"proposal": "Place identity verification inside the intake flow", "confirmation_needed": "Group approval after trade-off review", "prompt": "Should this be a confirmed direction or an option to test?"}],
        "tensions": [
            {"topic": "Completeness vs. completion", "perspectives": "Clinical needs enough detail for safety; operations expects longer forms to reduce completion.", "facilitator_move": "Define the minimum safe dataset and progressively disclose conditional questions."},
            {"topic": "Digital efficiency vs. equitable access", "perspectives": "SMS reduces routine work, but smartphone access and confidence vary.", "facilitator_move": "Treat digital and assisted paths as one service with shared outcomes."},
            {"topic": "Identity verification", "perspectives": "Everyone agrees it is required, but placement in the flow is unresolved.", "facilitator_move": "Score both patterns on abandonment, privacy risk, and integration effort."},
        ],
        "open_questions": ["Where should identity verification occur?", "What is the minimum safe medication flow?", "Which clinics should pilot?"],
        "follow_up_questions": ["What information can be removed without increasing risk?", "What triggers staff assistance?", "Which two-week leading indicator proves the pilot is working?"],
        "role_insights": [{"role": name, "insight": insights[name]} for name in selected if name in insights],
        "exercise": {"name": "Trade-off matrix", "instructions": "Score identity-before-link and identity-in-flow from 1–5 on patient effort, privacy, abandonment, and technical complexity.", "output": "A provisional identity pattern and its riskiest assumption."},
        "actions": [
            {"action": "Scope EHR medication verification", "owner": "Mike", "due": "This week", "status": "Not started"},
            {"action": "Draft minimum safe intake dataset", "owner": "Dr. Lee + Tom", "due": "Week 1", "status": "Not started"},
            {"action": "Recruit representative usability participants", "owner": "Aisha", "due": "Week 2", "status": "Not started"},
            {"action": "Select pilot clinics and baseline measures", "owner": "Sarah", "due": "Week 2", "status": "Not started"},
        ],
        "parking_lot": [
            {"topic": "Long-term analytics dashboard", "reason": "Not required to select the pilot workflow", "revisit": "Pilot retrospective"},
            {"topic": "Enterprise-wide rollout", "reason": "Depends on pilot evidence", "revisit": "After pilot results"},
        ],
        "dependencies": [{"dependency": "Compliance review", "impact": "Blocks usability testing", "owner": "Tom"}, {"dependency": "EHR feasibility", "impact": "Shapes pilot scope", "owner": "Mike"}],
        "transcript_summary": "The group converged on a two-path intake pilot combining SMS pre-check-in with assisted service. Medication data should be verified from the EHR rather than re-entered, with discrepancies routed to clinical review. The main unresolved choices are identity-verification placement and the minimum safe dataset. Accessibility testing and compliance review are required before launch.",
    }


def mock_readout(analysis, roles=None):
    return {
        "title": "A safer, simpler patient intake experience",
        "executive_summary": "The team aligned on a dual-path intake model: concise SMS pre-check-in backed by an intentional assisted pathway. An eight-week, two-clinic pilot will validate adoption, speed, safety, equity, and operational effort before scale-up.",
        "transcript_summary": analysis.get("transcript_summary", ""),
        "decisions": analysis["decisions"],
        "recommendations": ["Use a secure, concise pre-check-in flow with clear progress.", "Pre-populate eligible EHR data and flag discrepancies.", "Offer translated guidance and an assisted pathway.", "Collect only necessary information and validate consent and retention."],
        "actions": analysis["actions"], "parking_lot": analysis.get("parking_lot", []),
        "risks": ["Low completion → keep the flow short and measure abandonment.", "Digital exclusion → retain and test assisted service.", "Missed medication discrepancies → flag changes in the clinical workflow.", "Verification friction → compare both patterns before selection."],
        "success_measures": ["Median and 90th-percentile check-in time", "Pre-visit completion and abandonment", "Staff minutes per arrival", "Medication discrepancies resolved", "Outcomes by language and service pathway"],
    }


def mock_activity():
    return {
        "prompt": "What factors are affecting the patient intake experience?",
        "ideas": [
            {"idea": "Patients repeat information already in the EHR", "source": "Mike", "theme": "Data & technology"},
            {"idea": "Long forms may reduce completion", "source": "Sarah", "theme": "Process burden"},
            {"idea": "A smartphone cannot be the only entry point", "source": "Aisha", "theme": "Access & inclusion"},
            {"idea": "Medication changes must be visible to clinicians", "source": "Dr. Lee", "theme": "Safety & workflow"},
            {"idea": "Only necessary information should be collected", "source": "Tom", "theme": "Privacy & compliance"},
            {"idea": "Staff cannot chase every incomplete form", "source": "Sarah", "theme": "Process burden"},
        ],
        "themes": [
            {"theme": "Process burden", "count": 2, "insight": "Reduce entry and staff follow-up."},
            {"theme": "Safety & workflow", "count": 1, "insight": "Route medication exceptions into clinical review."},
            {"theme": "Access & inclusion", "count": 1, "insight": "Maintain a deliberate assisted pathway."},
            {"theme": "Data & technology", "count": 1, "insight": "Reuse trusted EHR data where feasible."},
            {"theme": "Privacy & compliance", "count": 1, "insight": "Minimize collection and validate consent."},
        ],
        "solutions": [
            {"solution": "EHR-prepopulated medication verification", "theme": "Safety & workflow", "votes": 8},
            {"solution": "Short SMS pre-check-in with save-and-return", "theme": "Process burden", "votes": 7},
            {"solution": "Integrated assisted check-in path", "theme": "Access & inclusion", "votes": 6},
            {"solution": "Progressive disclosure for conditional questions", "theme": "Process burden", "votes": 5},
        ],
    }
