import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def generate_stakeholder_analysis(summary):
    prompt = f"""
You are preparing for a stakeholder meeting regarding this initiative:
"{summary}"

Return a SWOT table for each of these groups:
- Plant Leadership
- Operations
- QA / Food Safety
- Maintenance / Engineering
- Safety / EHS
- Business / Finance

For each, include:
- Strengths (how the idea aligns with their goals)
- Weaknesses (what they might resist or question)
- Opportunities (how it benefits them or the plant long-term)
- Threats (what might cause them concern or delay)

Output in markdown format.
"""
    chat_completion = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return chat_completion.choices[0].message.content
