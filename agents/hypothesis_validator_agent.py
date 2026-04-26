"""Hypothesis validator agent for Project 25."""

from agents.base import run_agent_task


def validate_hypothesis(session_id: str, context_data: dict) -> str:
    """Pressure-test the current hypothesis and the evidence it would need."""
    return run_agent_task(
        session_id=session_id,
        agent_name="Hypothesis Validator Agent",
        context_data=context_data,
        objective=(
            "Evaluate whether the current research idea is testable, where the "
            "logic is strong, and what evidence would make it more rigorous."
        ),
        sections=[
            "Hypothesis check",
            "Evidence needed",
            "Research design considerations",
        ],
        extra_guidance=(
            "Call out confounds, missing variables, and ambiguous causal claims "
            "without sounding dismissive."
        ),
    )
