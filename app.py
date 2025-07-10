import streamlit as st
from modules import ideation

st.set_page_config(page_title="Engineering Strategist Agent", layout="wide")

st.title("🤖 Engineering Strategist Agent")
st.markdown("Support your automation projects from idea to startup with structured guidance, clear deliverables, and stakeholder awareness.")

st.sidebar.header("🛠️ Select Workflow")
workflow = st.sidebar.radio("Choose a focus area:", [
    "🔍 Ideation & Opportunity Framing",
])

# --- IDEATION MODULE ---
if workflow == "🔍 Ideation & Opportunity Framing":
    st.header("Early-Stage Brainstorming")

    if "idea_history" not in st.session_state:
        st.session_state.idea_history = []

    user_input = st.text_area("🔍 Describe the project opportunity or pain point", height=150)
    area = st.text_input("🏭 Plant Area or Context", value="General")
    constraints = st.text_input("⚠️ Known Constraints", value="")

    if st.button("💡 Generate Ideas"):
        with st.spinner("Thinking..."):
            output = ideation.generate_ideas(user_input, area, constraints)
            st.session_state.idea_text = output
            st.session_state.idea_history = [output]
        st.success("Initial ideas generated!")

    if "idea_text" in st.session_state:
        st.markdown("### 🧠 Current Ideas")
        st.markdown(st.session_state.idea_text)

        options = ideation.parse_options(st.session_state.idea_text)

        if not options:
            st.warning("⚠️ Could not parse individual ideas. Please check the response format.")
        else:
            selected = st.multiselect("💡 Select one or more ideas to refine:", options=options)
            question = st.text_area("🗣️ Add clarifications or follow-up questions")

            if st.button("🔁 Refine Selected Ideas"):
                if selected:
                    with st.spinner("Refining ideas..."):
                        selected_text = "\n".join(selected)
                        refined = ideation.refine_ideas(selected_text, question)
                        st.session_state.idea_text = refined
                        st.session_state.idea_history.append(refined)
                    st.success("Refinement complete!")
                else:
                    st.warning("Please select at least one idea to refine.")

    if st.session_state.idea_history:
        with st.expander("📜 View All Idea Iterations", expanded=False):
            for i, idea in enumerate(st.session_state.idea_history):
                st.markdown(f"### 💡 Round {i+1}")
                st.markdown(idea)
                st.markdown("---")