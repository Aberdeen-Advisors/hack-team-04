import json

from sample_data import ROLES, mock_activity, mock_agenda, mock_analysis, mock_readout


class WorkshopAI:
    def __init__(self, use_api=False, model="gpt-5.6-terra"):
        self.use_api = use_api
        self.model = model

    @staticmethod
    def _role_context(roles):
        return [{"name": name, **ROLES[name]} for name in (roles or []) if name in ROLES]

    def _ask(self, instructions, payload):
        from openai import OpenAI
        response = OpenAI().responses.create(
            model=self.model,
            instructions=instructions + " Return only valid JSON, with no markdown fences.",
            input=json.dumps(payload),
        )
        return json.loads(response.output_text)

    def generate_agenda(self, goal, participants, constraints, duration, roles=None):
        if not self.use_api:
            return mock_agenda(duration, roles)
        return self._ask(
            "Act as the selected facilitation-team roles. Create a pragmatic workshop plan. Return keys: agenda "
            "(list of title, minutes integer, purpose, owner_role), opening_questions (list), exercise "
            "(name, instructions, output), role_outputs (list of role, output), pre_work (list), materials (list), "
            "expected_decisions (list), output_checklist (list). Agenda minutes must sum to the duration.",
            {"goal": goal, "participants": participants, "constraints": constraints,
             "duration_minutes": duration, "facilitation_roles": self._role_context(roles)},
        )

    def analyze_discussion(self, transcript, goal, roles=None):
        if not self.use_api:
            return mock_analysis(roles)
        return self._ask(
            "Act as an impartial workshop control tower. Use only transcript evidence. Separate decisions from proposals. "
            "Return keys: session_status (on_track, status_note, current_topic), key_points (list), decisions (list), "
            "tensions (list of topic, perspectives, facilitator_move), open_questions (list), proposed_decisions "
            "(list of proposal, confirmation_needed, prompt), follow_up_questions (list), "
            "exercise (name, instructions, output), actions (list of action, owner, due, status), parking_lot "
            "(list of topic, reason, revisit), dependencies (list of dependency, impact, owner), role_insights "
            "(list of role, insight), transcript_summary (string). Never invent decisions, owners, dates, or agreement.",
            {"workshop_goal": goal, "transcript": transcript,
             "facilitation_roles": self._role_context(roles)},
        )

    def generate_readout(self, goal, analysis, roles=None):
        if not self.use_api:
            return mock_readout(analysis, roles)
        return self._ask(
            "Create a concise client-ready workshop readout using only supplied evidence. Return keys: title, "
            "executive_summary, transcript_summary, decisions (list), recommendations (list), actions "
            "(list of action, owner, due, status), parking_lot (list of topic, reason, revisit), risks (list), "
            "success_measures (list).",
            {"workshop_goal": goal, "workshop_analysis": analysis,
             "facilitation_roles": self._role_context(roles)},
        )

    def generate_activity(self, transcript, goal):
        if not self.use_api:
            return mock_activity()
        return self._ask(
            "Convert the transcript into a diverge-converge workshop activity. Return keys: prompt, ideas "
            "(list of idea, source, theme), themes (list of theme, count, insight), solutions "
            "(list of solution, theme, votes). Use only transcript evidence; votes must be 0 because no real vote occurred.",
            {"workshop_goal": goal, "transcript": transcript},
        )
