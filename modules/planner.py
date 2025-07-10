def generate_tasks(goal, phase):
    base_tasks = {
        "Ideation": [
            "Document current-state pain points",
            "Brainstorm automation options",
            "Map early stakeholders",
            "Estimate high-level cost & impact"
        ],
        "Feasibility": [
            "Collect supporting data (volume, space, labor)",
            "Draft FEL summary",
            "Develop ROI assumptions",
            "Engage vendor(s) for rough input"
        ],
        "Design": [
            "Create user requirement spec (URS)",
            "Review plant constraints",
            "Draft layout & mission maps",
            "Develop budget and schedule"
        ],
        "Execution": [
            "Confirm vendor PO and milestone dates",
            "Track open issues / RFIs",
            "Prepare site for install",
            "Review testing and validation plan"
        ],
        "Startup": [
            "Conduct startup testing",
            "Review with QA, Ops, Maintenance",
            "Document changes and results",
            "Capture lessons learned"
        ]
    }

    tasks = base_tasks.get(phase, [])
    output = f"### Task Breakdown – Phase: {phase}\n\n**Goal:** {goal}\n\n"
    for i, task in enumerate(tasks, 1):
        output += f"{i}. {task}\n"
    return output
