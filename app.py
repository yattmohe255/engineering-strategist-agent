import streamlit as st
from modules import ideation

st.set_page_config(page_title="Engineering Strategist Agent", layout="wide")
st.title("🤖 Engineering Strategist Agent")
st.markdown("Support your automation projects from idea to startup with structured guidance, clear deliverables, and stakeholder awareness.")

st.sidebar.header("🛠️ Select Workflow")
workflow = st.sidebar.radio("Choose a focus area:", [
    "🔍 Ideation & Opportunity Framing",
])

if workflow == "🔍 Ideation & Opportunity Framing":
    st.header("Early-Stage Brainstorming")

    if "idea_history" not in st.session_state:
        st.session_state.idea_history = []
    if "selected_idea" not in st.session_state:
        st.session_state.selected_idea = ""
    if "idea_text" not in st.session_state:
        st.session_state.idea_text = ""

    user_input = st.text_area("🔍 Describe the project opportunity or pain point", height=150)
    area = st.text_input("🏭 Plant Area or Context", value="General")
    constraints = st.text_input("⚠️ Known Constraints", value="")

    if st.button("💡 Generate Ideas"):
        with st.spinner("Thinking..."):
            output = ideation.generate_ideas(user_input, area, constraints)
            st.session_state.idea_text = output
            st.session_state.idea_history = [output]
            st.success("Done!")

    if st.session_state.idea_text:
        st.subheader("🧠 Initial AGV/AMR Suggestions")
        st.markdown(st.session_state.idea_text)

        options = ideation.parse_options(st.session_state.idea_text)
        selected = st.multiselect("💡 Select one or more ideas to refine:", options=options)

        if selected:
            selected_text = "\n\n".join(selected)
            st.session_state.selected_idea = selected_text

            followup = st.text_area("🔧 Ask a follow-up question or refinement", key="refine_input")

            if st.button("🔁 Refine Selection"):
                with st.spinner("Refining..."):
                    refined = ideation.refine_ideas(st.session_state.selected_idea, followup)
                    st.session_state.idea_history.append(refined)
                    st.session_state.idea_text = refined
                    st.success("Refined!")

        with st.expander("📜 View All Idea Iterations", expanded=False):
            for i, idea in enumerate(st.session_state.idea_history):
                st.markdown(f"### Round {i+1}")
                st.markdown(idea)
