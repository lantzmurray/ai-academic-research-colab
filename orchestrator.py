"""Orchestrator for Project 25."""

import os
import sys
from typing import Any, Dict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from agents.base import generate_session_id, log_agent_response
from agents.literature_review_agent import review_literature
from agents.hypothesis_validator_agent import validate_hypothesis
from agents.draft_polisher_agent import polish_draft

AGENT_SEQUENCE = (
    ("Literature Review Agent", review_literature),
    ("Hypothesis Validator Agent", validate_hypothesis),
    ("Draft Polisher Agent", polish_draft),
)


class Orchestrator:
    """Run the research collaboration workflow using a fixed sequence."""

    def generate_session_id(self) -> str:
        return generate_session_id()

    def run_workflow(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        session_id = self.generate_session_id()
        results = {}

        log_agent_response(
            session_id,
            "Workflow Input",
            "\n".join(
                f"- {key.replace('_', ' ').title()}: {value or 'Not provided'}"
                for key, value in inputs.items()
            ),
            {"kind": "input"},
        )

        for agent_name, agent_runner in AGENT_SEQUENCE:
            results[agent_name] = agent_runner(session_id, inputs)

        return {"session_id": session_id, "results": results}
