import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def generate_ideas(problem_description, area="General", constraints="None"):
    prompt = f"""
You are a senior automation engineer in a food manufacturing environment.

Given this opportunity:
"{problem_description}"
Area: {area}
Constraints: {constraints}

Generate:
1. A list of both traditional and advanced automation solutions (minimum 3)
2. Label each as:
  - 🟢 Quick Win
  - 🟡 Strategic Bet
  - 🔴 Long-Term Investment
3. Include a 2–3 sentence justification for each
4. Return a stakeholder SWOT table for:
  - Plant Leadership
  - Operations
  - QA / Food Safety
  - Maintenance / Engineering
  - Safety / EHS
  - Business / Finance
5. End with 2–3 key next steps or unknowns to validate

Structure clearly in markdown format.
"""
    chat_completion = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return chat_completion.choices[0].message.content
