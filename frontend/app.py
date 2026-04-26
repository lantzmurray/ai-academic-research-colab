import streamlit as st
import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PACKAGE_ROOT = os.path.dirname(os.path.dirname(PROJECT_ROOT))
sys.path.insert(0, PROJECT_ROOT)
if PACKAGE_ROOT not in sys.path:
    sys.path.insert(0, PACKAGE_ROOT)

from agents.base import get_session_history
from orchestrator import Orchestrator
from components import render_app_footer, run_with_status_updates

st.set_page_config(page_title="Academic Research Collaborator", layout="wide")


def render_session_log(session_id: str) -> None:
    """Show the collaboration log so research outputs can be audited later."""
    history = get_session_history(session_id)
    if not history:
        return

    st.subheader("Collaboration Log")
    for entry in history:
        timestamp = entry["timestamp"].replace("T", " ")
        with st.expander(f"{entry['agent']} · {timestamp}", expanded=False):
            st.markdown(entry["content"])


def main():
    st.title("Academic Research Collaborator")
    st.caption("Act as a research assistant for scholars writing papers.")

    st.sidebar.title("Research Inputs")
    research_question = st.sidebar.text_input(
        "Research Question",
        placeholder="How do small AI tutoring loops affect study retention?",
    )
    citations = st.text_area(
        "Citations",
        height=140,
        placeholder="Paste citations, paper titles, or notes from sources you already trust.",
    )
    notes = st.text_area(
        "Notes",
        height=180,
        placeholder="Add hypotheses, constraints, or draft fragments here.",
    )

    if st.button("Run Research Team", type="primary"):
        if not research_question.strip():
            st.warning("Add a research question so the agents have a clear focus.")
            return

        inputs = {
            "research_question": research_question.strip(),
            "citations": citations.strip(),
            "notes": notes.strip(),
        }
        orch = Orchestrator()
        output = run_with_status_updates(
            lambda: orch.run_workflow(inputs),
            start_message="Agents are collaborating on the research brief..."
        )

        st.success(f"Workflow Complete! Session ID: {output['session_id']}")

        for agent, response in output["results"].items():
            with st.expander(f"{agent} Response", expanded=True):
                st.markdown(response)

        render_session_log(output["session_id"])


    render_app_footer()

if __name__ == "__main__":
    main()
