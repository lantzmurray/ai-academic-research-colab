"""Draft polisher agent for Project 25."""

from agents.base import run_agent_task


def polish_draft(session_id: str, context_data: dict) -> str:
    """Suggest the edits that would make the draft read more like a paper."""
    return run_agent_task(
        session_id=session_id,
        agent_name="Draft Polisher Agent",
        context_data=context_data,
        objective=(
            "Turn the current research notes into a cleaner paper direction by "
            "calling out structure, clarity, and polish improvements."
        ),
        sections=[
            "Structural edits",
            "Clarity edits",
            "Final polish checklist",
        ],
        extra_guidance=(
            "Write like an academic writing coach. Focus on argument flow, "
            "evidence placement, and paragraph-level clarity."
        ),
    )
