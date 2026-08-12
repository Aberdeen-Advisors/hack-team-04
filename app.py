import json
import os
from html import escape
from datetime import date

import streamlit as st
from dotenv import load_dotenv

from ai_service import WorkshopAI
from sample_data import DEFAULT_ROLES, ROLES, SAMPLE

load_dotenv()
st.set_page_config(page_title="Workshop Copilot", page_icon="✦", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,400;0,500;0,600;0,700;1,600&display=swap');
:root { --blue:#09375F; --teal:#44B0B1; --onyx:#404040; --white:#FFFFFF; --tint:#E8F4F4; --hairline:#E5E5E5; --link:#0072AD; --jade:#00A676; --jasper:#DB504A; --gold:#F7D002; }
.stApp { background:#FFFFFF; color:var(--onyx); }
html, body, [class*="css"] { font-family:'Poppins','Calibri',sans-serif; line-height:1.15; }
h1,h2,h3,h4,h5,h6 { font-family:'Poppins','Calibri',sans-serif !important;letter-spacing:0;color:var(--blue) !important; }
.hero { padding:1.1rem 0 .7rem; }
.eyebrow { color:var(--blue);font-size:.74rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase; }
.hero { border-bottom:2px solid var(--teal);margin-bottom:1.5rem; }
.hero h1 { font-size:2rem;margin:.3rem 0;color:var(--blue) !important; }
.hero p { color:var(--onyx);font-size:1.05rem;max-width:760px; }
.mode { display:inline-block;background:var(--tint);color:var(--blue);border-radius:3px;padding:.35rem .7rem;font-weight:700;font-size:.72rem; }
.card { background:var(--white);border:1px solid var(--hairline);border-left:3px solid var(--teal);border-radius:4px;padding:1.15rem 1.25rem;margin:.65rem 0;box-shadow:none; }
.label { font-size:.7rem;text-transform:uppercase;letter-spacing:.08em;color:var(--onyx);font-weight:700; }
.decision { border-left:4px solid var(--blue); }
.tension { border-left:4px solid var(--jasper); }
.agenda-time { color:var(--blue);font-weight:700; }
.role { border-top:1px solid var(--hairline);border-left:3px solid var(--teal);min-height:170px; }
.role-icon { font-size:1.6rem; }
.status-good { border-left:5px solid var(--jade); }
.status-watch { border-left:5px solid var(--gold); }
.status-risk { border-left:5px solid var(--jasper); }
.parking { border-left:4px solid var(--gold); }
.sticky { background:var(--tint);border:1px solid var(--hairline);border-left:3px solid var(--teal);border-radius:3px;padding:1rem;min-height:125px;box-shadow:none;transform:none;margin:.5rem 0;color:var(--onyx); }
.confidence { display:inline-block;border-radius:99px;padding:.24rem .62rem;font-size:.7rem;font-weight:800;letter-spacing:.035em;margin-top:.65rem; }
.confidence-high { background:#d9f5e5 !important;color:#12613f !important;border:1px solid #79c99d; }
.confidence-medium { background:#fff1c2 !important;color:#765500 !important;border:1px solid #ddb84c; }
.confidence-low { background:#ffe0df !important;color:#8f2622 !important;border:1px solid #df8580; }
[data-testid="stSidebar"] { background:var(--blue); }
[data-testid="stSidebar"] * { color:#f3f7f3 !important; }
.stButton>button { border-radius:3px;font-weight:600;border:1px solid var(--blue);background:var(--blue);color:white; }
.stButton>button:hover { background:#062A49;color:white;border-color:#062A49; }
div[data-testid="stMetric"] { background:white;border:1px solid var(--hairline);border-top:3px solid var(--teal);padding:14px;border-radius:3px; }
/* Keep form controls readable across Streamlit themes and Windows browsers. */
[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea,
[data-baseweb="input"] input,
[data-baseweb="textarea"] textarea {
    background:#ffffff !important;
    color:#404040 !important;
    -webkit-text-fill-color:#404040 !important;
    caret-color:#404040 !important;
}
[data-testid="stTextInput"] input::placeholder,
[data-testid="stTextArea"] textarea::placeholder {
    color:#404040 !important;
    -webkit-text-fill-color:#404040 !important;
    opacity:1 !important;
}
[data-baseweb="select"] > div,
[data-baseweb="base-input"],
[data-baseweb="input"] {
    background:#ffffff !important;
    color:#404040 !important;
}
[data-baseweb="select"] span,
[data-baseweb="select"] input,
[data-baseweb="popover"] li,
[role="option"] {
    color:#404040 !important;
    -webkit-text-fill-color:#404040 !important;
}
[data-baseweb="popover"],
[data-baseweb="menu"],
[role="listbox"] { background:#ffffff !important; }
[data-testid="stNumberInput"] input {
    background:#ffffff !important;
    color:#404040 !important;
    -webkit-text-fill-color:#404040 !important;
}
[data-testid="stDataEditor"],
[data-testid="stDataFrame"] { background:#ffffff !important; color:#404040 !important; }
[data-testid="stDataEditor"] canvas,
[data-testid="stDataFrame"] canvas { color-scheme:light !important; }

/* High-contrast application theme. Keep these rules last so OS/browser themes
   cannot turn inherited text white on the light workspace. */
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
[data-testid="stMainBlockContainer"] { color:#404040 !important; }
[data-testid="stMain"] p,
[data-testid="stMain"] span:not(.mode):not(.confidence):not(.agenda-time):not(.label),
[data-testid="stMain"] label,
[data-testid="stMain"] li,
[data-testid="stMain"] small,
[data-testid="stMain"] h1,
[data-testid="stMain"] h2,
[data-testid="stMain"] h3,
[data-testid="stMain"] h4,
[data-testid="stMain"] h5,
[data-testid="stMain"] h6,
[data-testid="stMarkdownContainer"] { color:#404040 !important; }
.card, .card *, .sticky, .sticky * { color:#404040 !important; }
.card b, .sticky b { color:#09375F !important; }
.card .label, .sticky .label, .label { color:#404040 !important; }
.card .agenda-time, .agenda-time { color:#09375F !important; }
.mode { color:#09375F !important; }
.confidence-high { color:#12613f !important; }
.confidence-medium { color:#765500 !important; }
.confidence-low { color:#8f2622 !important; }

/* Labels, help text, captions and expanders. */
[data-testid="stWidgetLabel"] p,
[data-testid="stCaptionContainer"] p,
[data-testid="stTooltipContent"],
[data-testid="stExpander"] summary,
[data-testid="stExpander"] summary * { color:#09375F !important; }
[data-testid="stCaptionContainer"] p { color:#404040 !important; }
[data-testid="stExpander"] { background:#ffffff !important;border:1px solid #E5E5E5 !important;border-radius:3px; }

/* Every editable control has a white surface and black text. */
[data-testid="stMain"] input,
[data-testid="stMain"] textarea,
[data-testid="stMain"] [contenteditable="true"],
[data-testid="stMain"] [data-baseweb="select"] > div,
[data-testid="stMain"] [data-baseweb="base-input"],
[data-testid="stMain"] [data-baseweb="input"] {
    background:#ffffff !important;
    color:#404040 !important;
    -webkit-text-fill-color:#404040 !important;
    caret-color:#404040 !important;
}
[data-testid="stMain"] input::placeholder,
[data-testid="stMain"] textarea::placeholder {
    color:#404040 !important;
    -webkit-text-fill-color:#404040 !important;
    opacity:1 !important;
}

/* Select menus, multiselect chips and popovers. */
[data-baseweb="popover"], [data-baseweb="popover"] *,
[data-baseweb="menu"], [data-baseweb="menu"] *,
[role="listbox"], [role="listbox"] *, [role="option"] {
    background-color:#ffffff !important;
    color:#404040 !important;
    -webkit-text-fill-color:#404040 !important;
}
[data-baseweb="tag"] { background:#E8F4F4 !important; }
[data-baseweb="tag"] span { color:#09375F !important;-webkit-text-fill-color:#09375F !important; }

/* Metrics, alerts, tables and segmented controls. */
[data-testid="stMetric"] *, [data-testid="stMetricValue"], [data-testid="stMetricLabel"] { color:#09375F !important; }
[data-testid="stAlert"] { background:#E8F4F4 !important;border:1px solid #E5E5E5 !important;border-left:4px solid #44B0B1 !important; }
[data-testid="stAlert"] * { color:#09375F !important; }
[data-testid="stDataEditor"], [data-testid="stDataFrame"] { color-scheme:light !important;background:#ffffff !important; }
[data-testid="stDataEditor"] *, [data-testid="stDataFrame"] * { color:#404040; }
[data-testid="stSegmentedControl"] { background:#E8F4F4 !important;border-radius:3px; }
[data-testid="stSegmentedControl"] label { color:#09375F !important; }
[data-testid="stSegmentedControl"] label:has(input:checked) { background:#09375F !important; }
[data-testid="stSegmentedControl"] label:has(input:checked) * { color:#ffffff !important; }

/* Sidebar is deliberately dark, but its form fields remain white and legible. */
[data-testid="stSidebar"] { background:#09375F !important; }
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] label span { color:#f7faf8 !important; }
[data-testid="stSidebar"] input,
[data-testid="stSidebar"] textarea,
[data-testid="stSidebar"] [data-baseweb="select"] > div {
    background:#ffffff !important;
    color:#404040 !important;
    -webkit-text-fill-color:#404040 !important;
}

/* Buttons retain white labels on green, including hover/focus states. */
.stButton > button, .stButton > button *,
.stDownloadButton > button, .stDownloadButton > button * { color:#ffffff !important; }
.stButton > button:focus, .stDownloadButton > button:focus { box-shadow:0 0 0 3px rgba(68,176,177,.35) !important; }
.stDownloadButton > button,
.stDownloadButton > button:hover,
.stDownloadButton > button:focus,
.stDownloadButton > button:active,
[data-testid="stDownloadButton"] > button,
[data-testid="stDownloadButton"] > button:hover {
    background:#09375F !important;
    border:1px solid #09375F !important;
    color:#ffffff !important;
    -webkit-text-fill-color:#ffffff !important;
}
.stDownloadButton > button p,
.stDownloadButton > button span,
.stDownloadButton > button svg,
[data-testid="stDownloadButton"] button p,
[data-testid="stDownloadButton"] button span {
    color:#ffffff !important;
    fill:#ffffff !important;
    -webkit-text-fill-color:#ffffff !important;
    opacity:1 !important;
}
/* Aberdeen table treatment: blue header, white text, teal-tinted body. */
[data-testid="stDataFrame"] [role="columnheader"],
[data-testid="stDataEditor"] [role="columnheader"] { background:#09375F !important;color:#FFFFFF !important; }
[data-testid="stDataFrame"] [role="columnheader"] *,
[data-testid="stDataEditor"] [role="columnheader"] * { color:#FFFFFF !important;-webkit-text-fill-color:#FFFFFF !important; }
[data-testid="stDataFrame"] [role="gridcell"],
[data-testid="stDataEditor"] [role="gridcell"] { border-color:#E5E5E5 !important; }
a { color:#0072AD !important;text-decoration:underline !important; }
</style>
""", unsafe_allow_html=True)


def init_state():
    defaults = {
        "stage": "1 · Setup", "goal": SAMPLE["goal"], "participants": SAMPLE["participants"],
        "constraints": SAMPLE["constraints"], "duration": 90, "transcript": SAMPLE["transcript"],
        "client_name": SAMPLE["client_name"], "workshop_type": SAMPLE["workshop_type"],
        "healthcare_setting": SAMPLE["healthcare_setting"], "success_criteria": SAMPLE["success_criteria"],
        "ai_focus": SAMPLE["ai_focus"], "ai_exclusions": SAMPLE["ai_exclusions"],
        "live_objective": SAMPLE["live_objective"], "live_view": "Control tower", "activity": None,
        "roles": DEFAULT_ROLES, "agenda": None, "analysis": None, "readout": None,
        "agenda_item": "Design the future state", "minutes_remaining": 18,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def confidence_badge(score):
    """Render the demo confidence convention consistently across all outputs."""
    score = max(0, min(100, int(score)))
    if score >= 85:
        level, css = "High", "confidence-high"
    elif score >= 70:
        level, css = "Medium", "confidence-medium"
    else:
        level, css = "Low", "confidence-low"
    return f'<span class="confidence {css}">{level} confidence · {score}%</span>'


def list_html(items, css="", score=90):
    return "".join(f'<div class="card {css}">{escape(str(item))}<br>{confidence_badge(score)}</div>' for item in items)


def table_confidence(rows, score=90):
    level = "High" if score >= 85 else ("Medium" if score >= 70 else "Low")
    return [{**row, "confidence": f"{level} · {score}%"} for row in rows]


def readout_markdown(data):
    actions = "\n".join(f"- **{a['action']}** — {a['owner']} · {a['due']} · {a.get('status', 'Not started')}" for a in data["actions"])
    return f"""# {data['title']}
_Prepared {date.today().strftime('%B %d, %Y')}_

## Executive summary
{data['executive_summary']}

## Decisions
{chr(10).join('- ' + x for x in data['decisions'])}

## Recommended future state
{chr(10).join('- ' + x for x in data['recommendations'])}

## Action plan
{actions}

## Parking lot
{chr(10).join('- **' + x['topic'] + ':** ' + x['reason'] + ' — Revisit: ' + x['revisit'] for x in data.get('parking_lot', []))}

## Full transcript summary
{data.get('transcript_summary', '')}

## Risks and mitigations
{chr(10).join('- ' + x for x in data['risks'])}

## Success measures
{chr(10).join('- ' + x for x in data['success_measures'])}
"""


init_state()
with st.sidebar:
    st.markdown("## ORBIT")
    st.caption("by Aberdeen Advisors")
    st.markdown("AI workshop facilitation, from preparation to aligned action.")
    st.divider()
    api_available = bool(os.getenv("OPENAI_API_KEY"))
    mode = st.radio("Intelligence mode", ["Demo mode", "OpenAI API"],
                    index=0, help="Demo mode is deterministic and needs no API key.")
    if mode == "OpenAI API" and not api_available:
        st.warning("Add OPENAI_API_KEY to .env, then restart the app.")
    st.caption("Demo content uses a fictional health-system scenario. Do not enter protected health information.")
    st.markdown("**Confidence thresholds**")
    st.markdown('<span class="confidence confidence-high">High · 85–100%</span><br><span class="confidence confidence-medium">Medium · 70–84%</span><br><span class="confidence confidence-low">Low · below 70%</span>', unsafe_allow_html=True)
    st.caption("Indicative demo scores only; they are not calibrated probabilities.")
    st.divider()
    if st.button("Reset demo", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

use_api = mode == "OpenAI API" and api_available
ai = WorkshopAI(use_api=use_api, model=os.getenv("OPENAI_MODEL", "gpt-5.6-terra"))

st.markdown(f"""<div class="hero"><div class="eyebrow">ORBIT · AI WORKSHOP FACILITATION</div>
<h1>Turn conversation into momentum.</h1><p>Prepare with intent, guide the room in real time, and turn discussion into decisions people can act on.</p>
<span class="mode">{'LIVE AI' if use_api else 'DEMO MODE · NO API KEY'}</span></div>""", unsafe_allow_html=True)

stage = st.segmented_control("Workflow stage", ["1 · Setup", "2 · Live Workshop", "3 · Readout"],
                             default=st.session_state.stage, label_visibility="collapsed")
if stage:
    st.session_state.stage = stage

if st.session_state.stage == "1 · Setup":
    st.subheader("Workshop setup")
    st.write("Start with the outcome, the voices in the room, and the boundaries the group must respect.")
    with st.form("setup"):
        context1, context2, context3 = st.columns(3)
        with context1:
            st.text_input("Client / organization", key="client_name")
        with context2:
            st.selectbox("Workshop intent", ["Future-state design", "Strategic alignment", "Operating-model design", "Implementation planning", "Current-state assessment"], key="workshop_type")
        with context3:
            st.text_input("Healthcare setting", key="healthcare_setting")
        st.text_area("Workshop goal", key="goal", height=90)
        c1, c2 = st.columns(2)
        with c1:
            st.text_area("Participants & perspectives", key="participants", height=150)
        with c2:
            st.text_area("Constraints", key="constraints", height=150)
        st.text_area("Success criteria", key="success_criteria", height=100, help="Enter one criterion per line.")
        instruction1, instruction2 = st.columns(2)
        with instruction1:
            st.text_area("AI focus areas", key="ai_focus", height=110)
        with instruction2:
            st.text_area("AI guardrails & exclusions", key="ai_exclusions", height=110)
        st.markdown("#### Facilitation team roles")
        st.caption("Select the AI jobs that should support the human facilitation team. Each role produces a different workshop output.")
        st.multiselect("Activate roles", options=list(ROLES), key="roles")
        st.slider("Session length (minutes)", 45, 180, key="duration", step=15)
        submitted = st.form_submit_button("Generate workshop plan", use_container_width=True)
    if submitted:
        with st.spinner("Designing the session…"):
            try:
                st.session_state.agenda = ai.generate_agenda(st.session_state.goal, st.session_state.participants,
                                                             st.session_state.constraints + "\nSuccess criteria:\n" + st.session_state.success_criteria + "\nAI focus:\n" + st.session_state.ai_focus + "\nExclusions:\n" + st.session_state.ai_exclusions,
                                                             st.session_state.duration, st.session_state.roles)
            except Exception as exc:
                st.error(f"API request failed: {exc}. Switch to Demo mode to continue.")
    if st.session_state.agenda:
        a = st.session_state.agenda
        if st.session_state.roles:
            st.markdown("### Your facilitation team")
            role_cols = st.columns(min(len(st.session_state.roles), 4))
            for i, name in enumerate(st.session_state.roles):
                role = ROLES[name]
                with role_cols[i % len(role_cols)]:
                    st.markdown(f'<div class="card role"><span class="role-icon">{role["icon"]}</span><br><b>{name}</b><br><span class="label">{role["phase"]}</span><br><br>{role["job"]}<br><br><span class="label">Produces</span><br>{role["output"]}</div>', unsafe_allow_html=True)
        st.markdown("### Recommended agenda")
        for item in a["agenda"]:
            st.markdown(f'<div class="card"><span class="agenda-time">{item["minutes"]} min</span> · <b>{escape(item["title"])}</b><br>{escape(item["purpose"])}<br><br><span class="label">Lead role</span> {escape(item.get("owner_role", "Workshop Planner"))}<br>{confidence_badge(94)}</div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### Opening questions")
            st.markdown(list_html(a["opening_questions"]), unsafe_allow_html=True)
        with c2:
            st.markdown("#### Interactive exercise")
            ex = a["exercise"]
            st.markdown(f'<div class="card"><b>{escape(ex["name"])}</b><br>{escape(ex["instructions"])}<br><br><span class="label">Output</span><br>{escape(ex["output"])}<br>{confidence_badge(88)}</div>', unsafe_allow_html=True)
        plan1, plan2 = st.columns(2)
        with plan1:
            st.markdown("#### Pre-work & inputs needed")
            st.markdown(list_html(a.get("pre_work", [])), unsafe_allow_html=True)
            st.markdown("#### Materials to prepare")
            st.markdown(list_html(a.get("materials", [])), unsafe_allow_html=True)
        with plan2:
            st.markdown("#### Expected decisions")
            st.markdown(list_html(a.get("expected_decisions", []), "decision"), unsafe_allow_html=True)
            st.markdown("#### Output checklist")
            st.markdown(list_html(a.get("output_checklist", [])), unsafe_allow_html=True)
        if st.button("Continue to live workshop →"):
            st.session_state.stage = "2 · Live Workshop"; st.rerun()

elif st.session_state.stage == "2 · Live Workshop":
    st.subheader("Live control tower")
    st.write("Monitor pace, alignment, decisions, actions, and topics that should not derail the current objective.")
    st.text_input("Live facilitation objective", key="live_objective")
    st.segmented_control("Live mode", ["Control tower", "Diverge → converge activity"], key="live_view", label_visibility="collapsed")
    top1, top2 = st.columns([2, 1])
    with top1:
        agenda_titles = [x["title"] for x in st.session_state.agenda["agenda"]] if st.session_state.agenda else ["Frame the outcome", "Map today’s journey", "Hear every perspective", "Design the future state", "Stress-test the concept", "Decide and mobilize"]
        st.selectbox("Current agenda item", agenda_titles, key="agenda_item")
    with top2:
        st.number_input("Minutes remaining", min_value=0, max_value=180, key="minutes_remaining")
    with st.expander("Simulated live transcript feed", expanded=True):
        st.caption("Hackathon demo: paste or edit a pre-generated transcript. Future state: receive text from a Teams, Zoom, or transcription-service API.")
        st.text_area("Discussion notes / transcript", key="transcript", height=220, label_visibility="collapsed")
    if st.session_state.live_view == "Diverge → converge activity":
        st.markdown("### Transcript-driven activity")
        st.caption("Demo workflow: extract ideas → cluster themes → propose solutions → prioritize. Confidence and vote values are illustrative placeholders.")
        if st.button("Generate sticky-note activity", use_container_width=True):
            with st.spinner("Turning discussion into an activity…"):
                try:
                    st.session_state.activity = ai.generate_activity(st.session_state.transcript, st.session_state.goal)
                except Exception as exc:
                    st.error(f"API request failed: {exc}. Switch to Demo mode to continue.")
        if st.session_state.activity:
            activity = st.session_state.activity
            st.markdown(f'<div class="card"><b>Activity prompt:</b> {escape(activity["prompt"])}<br>{confidence_badge(91)}</div>', unsafe_allow_html=True)
            st.markdown("#### 1 · Diverge — ideas from the discussion")
            sticky_cols = st.columns(3)
            for i, note in enumerate(activity["ideas"]):
                with sticky_cols[i % 3]:
                    st.markdown(f'<div class="sticky"><b>{escape(note["idea"])}</b><br><br><span class="label">{escape(note["source"])} · {escape(note["theme"])}</span><br>{confidence_badge(89)}</div>', unsafe_allow_html=True)
            st.markdown("#### 2 · Converge — clustered themes")
            st.dataframe(table_confidence(activity["themes"], 86), use_container_width=True, hide_index=True)
            st.markdown("#### 3 · Deep dive and prioritize")
            ranked = st.data_editor(table_confidence(activity["solutions"], 78), use_container_width=True, hide_index=True,
                                    column_config={"votes": st.column_config.NumberColumn("Demo votes", min_value=0, max_value=20, step=1)})
            st.caption("Votes are editable demo placeholders—not measured confidence or actual participant votes.")
        st.stop()
    if st.button("Analyze discussion", use_container_width=True):
        with st.spinner("Listening across perspectives…"):
            try:
                st.session_state.analysis = ai.analyze_discussion(st.session_state.transcript, st.session_state.goal, st.session_state.roles)
            except Exception as exc:
                st.error(f"API request failed: {exc}. Switch to Demo mode to continue.")
    if st.session_state.analysis:
        d = st.session_state.analysis
        m1, m2, m3, m4 = st.columns(4)
        pace = "On track" if st.session_state.minutes_remaining > 10 else ("Watch time" if st.session_state.minutes_remaining > 5 else "Time risk")
        status_css = "status-good" if st.session_state.minutes_remaining > 10 else ("status-watch" if st.session_state.minutes_remaining > 5 else "status-risk")
        m1.metric("Session", pace)
        m2.metric("Time left", f"{st.session_state.minutes_remaining} min")
        m3.metric("Decisions", len(d["decisions"])); m4.metric("Open tensions", len(d["tensions"]))
        st.markdown(f'<div class="card {status_css}"><span class="label">Orchestrator signal · {escape(st.session_state.agenda_item)}</span><br><br><b>{escape(d["session_status"]["status_note"])}</b><br>{confidence_badge(98)}</div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### What the room is saying")
            st.markdown(list_html(d["key_points"], score=92), unsafe_allow_html=True)
            st.markdown("#### Decisions captured")
            st.markdown(list_html(d["decisions"], "decision", 96), unsafe_allow_html=True)
        with c2:
            st.markdown("#### Tensions to work through")
            for t in d["tensions"]:
                st.markdown(f'<div class="card tension"><b>{escape(t["topic"])}</b><br>{escape(t["perspectives"])}<br><br><span class="label">Facilitator move</span><br>{escape(t["facilitator_move"])}<br>{confidence_badge(84)}</div>', unsafe_allow_html=True)
            st.markdown("#### Follow-up questions")
            st.markdown(list_html(d["follow_up_questions"], score=82), unsafe_allow_html=True)
        ex = d["exercise"]
        st.markdown(f'<div class="card"><b>Suggested exercise: {escape(ex["name"])}</b><br>{escape(ex["instructions"])}<br><br><span class="label">Expected output</span><br>{escape(ex["output"])}<br>{confidence_badge(80)}</div>', unsafe_allow_html=True)
        if d.get("role_insights"):
            with st.expander("Role-specific guidance"):
                for insight in d["role_insights"]:
                    st.markdown(f'<div class="card role"><b>{escape(insight["role"])}</b><br>{escape(insight["insight"])}<br>{confidence_badge(87)}</div>', unsafe_allow_html=True)
        track1, track2 = st.columns(2)
        with track1:
            st.markdown("#### Action tracker")
            edited = st.data_editor(table_confidence(d["actions"], 95), num_rows="dynamic", use_container_width=True,
                                column_config={"status": st.column_config.SelectboxColumn(options=["Not started", "In progress", "Done"])})
            st.session_state.analysis["actions"] = edited.to_dict("records") if hasattr(edited, "to_dict") else edited
        with track2:
            st.markdown("#### Parking lot")
            parked = st.data_editor(table_confidence(d["parking_lot"], 77), num_rows="dynamic", use_container_width=True)
            st.session_state.analysis["parking_lot"] = parked.to_dict("records") if hasattr(parked, "to_dict") else parked
        if d.get("proposed_decisions"):
            st.markdown("#### Decisions needing confirmation")
            for item in d["proposed_decisions"]:
                st.markdown(f'<div class="card status-watch"><b>{escape(item["proposal"])}</b><br>{escape(item["confirmation_needed"])}<br><br><span class="label">Facilitator prompt</span><br>{escape(item["prompt"])}<br>{confidence_badge(68)}</div>', unsafe_allow_html=True)
        if d.get("dependencies"):
            st.markdown("#### Dependencies")
            st.dataframe(table_confidence(d["dependencies"], 91), use_container_width=True, hide_index=True)
        if st.button("Build client-ready readout →"):
            with st.spinner("Turning workshop outputs into a narrative…"):
                try:
                    st.session_state.readout = ai.generate_readout(st.session_state.goal, st.session_state.analysis, st.session_state.roles)
                    st.session_state.stage = "3 · Readout"; st.rerun()
                except Exception as exc:
                    st.error(f"API request failed: {exc}. Switch to Demo mode to continue.")

else:
    st.subheader("Readout & action plan")
    if not st.session_state.analysis:
        st.info("Analyze a discussion first, then return here for the final readout.")
    else:
        if not st.session_state.readout:
            if st.button("Generate final readout", use_container_width=True):
                with st.spinner("Preparing the readout…"):
                    try:
                        st.session_state.readout = ai.generate_readout(st.session_state.goal, st.session_state.analysis, st.session_state.roles)
                        st.rerun()
                    except Exception as exc:
                        st.error(f"API request failed: {exc}. Switch to Demo mode to continue.")
        if st.session_state.readout:
            r = st.session_state.readout
            st.markdown(f'<h2>{escape(r["title"])}</h2>{confidence_badge(92)}', unsafe_allow_html=True)
            st.markdown(f'<div class="card"><span class="label">Executive summary</span><br><br>{escape(r["executive_summary"])}<br>{confidence_badge(93)}</div>', unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("#### Decisions"); st.markdown(list_html(r["decisions"], "decision", 96), unsafe_allow_html=True)
                st.markdown("#### Recommended future state"); st.markdown(list_html(r["recommendations"], score=86), unsafe_allow_html=True)
            with c2:
                st.markdown("#### Risks & mitigations"); st.markdown(list_html(r["risks"], "tension", 81), unsafe_allow_html=True)
                st.markdown("#### Success measures"); st.markdown(list_html(r["success_measures"], score=74), unsafe_allow_html=True)
            st.markdown("#### Action plan")
            st.dataframe(table_confidence(r["actions"], 95), use_container_width=True, hide_index=True)
            if r.get("parking_lot"):
                st.markdown("#### Parking lot")
                st.dataframe(table_confidence(r["parking_lot"], 77), use_container_width=True, hide_index=True)
            st.markdown("#### Full transcript summary")
            st.markdown(f'<div class="card">{escape(r.get("transcript_summary", ""))}<br>{confidence_badge(90)}</div>', unsafe_allow_html=True)
            st.download_button("Download client readout (.md)", readout_markdown(r),
                               file_name="patient-intake-workshop-readout.md", mime="text/markdown", use_container_width=True)
