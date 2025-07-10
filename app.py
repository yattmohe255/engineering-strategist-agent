from modules import ideation, feasibility, planner, stakeholders, memory
import streamlit as st
from dotenv import load_dotenv
load_dotenv()


st.set_page_config(page_title="Engineering Strategist Agent", layout="wide")
st.title("🤖 Engineering Strategist Agent")
st.markdown("Support your automation projects from idea to startup with structured guidance, clear deliverables, and stakeholder awareness.")

st.sidebar.header("🛠️ Select Workflow")
workflow = st.sidebar.radio("Choose a focus area:", [
    "🔍 Ideation & Opportunity Framing",
    "📊 Feasibility & FEL Prep",
    "🗂️ Task Planning",
    "🤝 Stakeholder & Communication Prep",
    "🧠 Project Memory"
])

# --- IDEATION ---
if workflow == "🔍 Ideation & Opportunity Framing":
    st.header("Early-Stage Brainstorming")

    if "ideation_history" not in st.session_state:
        st.session_state.ideation_history = []
    if "selected_idea" not in st.session_state:
        st.session_state.selected_idea = None

    user_input = st.text_area("🔍 Describe the project opportunity or pain point", height=150)
    area = st.text_input("🏭 Plant Area or Context", value="General")
    constraints = st.text_input("⚠️ Known Constraints", value="")

    if st.button("💡 Generate Ideas"):
        with st.spinner("Thinking..."):
            output = ideation.generate_ideas(user_input, area, constraints)
            st.session_state.ideation_output = output
            ideas = ideation.parse_options(output)
            st.session_state.ideation_history = ideas
            st.success("Done!")

    if "ideation_output" in st.session_state:
        st.subheader("🧠 Initial AGV/AMR Suggestions")
        st.markdown(st.session_state.ideation_output)

        ideas = st.session_state.ideation_history
        selected = st.multiselect("💡 Select one or more ideas to refine:", options=ideas)

        if selected:
            st.session_state.selected_idea = "\n\n".join(selected)
            followup = st.text_area("🔧 Ask a follow-up question or request refinement", key="refine_input")

            if st.button("🔁 Refine Selected Ideas"):
                with st.spinner("Refining..."):
                    refined_output = ideation.refine_ideas(st.session_state.selected_idea, followup)
                    st.markdown("### 🔄 Refined Output")
                    st.markdown(refined_output)

# --- FEASIBILITY ---
elif workflow == "📊 Feasibility & FEL Prep":
    st.header("Feasibility / FEL Builder")
    name = st.text_input("📛 Project Name")
    opp = st.text_area("📈 Opportunity Summary")
    risks = st.text_area("⚠️ Risks or Barriers")
    roi = st.text_input("💰 Estimated ROI or Payback Period")
    if st.button("📝 Generate FEL Summary"):
        doc = feasibility.fill_fel_template(name, opp, risks, roi)
        st.text_area("📄 FEL Output", doc, height=300)

# --- TASK PLANNING ---
elif workflow == "🗂️ Task Planning":
    st.header("Task Breakdown Generator")
    goal = st.text_area("🎯 Describe your near-term project goal or milestone")
    phase = st.selectbox("📍 Select Project Phase", [
        "Ideation", "Feasibility", "Design", "Execution", "Startup"
    ])
    if st.button("✅ Generate Task Plan"):
        plan = planner.generate_tasks(goal, phase)
        st.markdown(plan)

# --- STAKEHOLDER SWOT ---
elif workflow == "🤝 Stakeholder & Communication Prep":
    st.header("Stakeholder SWOT + Messaging Guidance")
    topic = st.text_area("🧾 Brief summary of the project topic or recommendation")
    if st.button("📣 Generate SWOT + Messaging Strategy"):
        with st.spinner("Analyzing..."):
            result = stakeholders.generate_stakeholder_analysis(topic)
            st.success("Done!")
            st.markdown(result)

# --- PROJECT MEMORY ---
elif workflow == "🧠 Project Memory":
    st.header("📘 Project Memory Log")
    subtask = st.radio("What would you like to do?", ["View Project Log", "Add New Entry"])

    if subtask == "View Project Log":
        project_log = memory.load_memory()
        if project_log["projects"]:
            for p in project_log["projects"]:
                st.markdown(f"### 📌 {p['name']}")
                st.markdown(f"- **Date**: {p['date_added']}")
                st.markdown(f"- **Description**: {p['description']}")
                st.markdown(f"- **Technologies**: {p['technologies']}")
                st.markdown(f"- **Stakeholders**: {p['stakeholders']}")
                st.markdown(f"- **Lessons Learned**: {p['lessons']}")
                st.markdown("---")
        else:
            st.info("No projects logged yet.")

    elif subtask == "Add New Entry":
        st.subheader("📝 Add a New Project Snapshot")
        name = st.tex
