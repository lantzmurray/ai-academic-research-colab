"""Literature review agent for Project 25."""

from agents.base import run_agent_task


def review_literature(session_id: str, context_data: dict) -> str:
    """Synthesize the supplied research framing into an initial literature map."""
    return run_agent_task(
        session_id=session_id,
        agent_name="Literature Review Agent",
        context_data=context_data,
        objective=(
            "Summarize the likely literature landscape around the user's research "
            "question, citations, and notes."
        ),
        sections=[
            "Themes in the literature",
            "Consensus vs open debate",
            "Gaps worth exploring",
        ],
        extra_guidance=(
            "Only treat supplied citations as concrete sources. If you infer a "
            "theme, label it as an informed assumption."
        ),
    )
