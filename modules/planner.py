import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def generate_tasks(goal, phase):
    prompt = f"""
You are a senior project engineer managing an automation initiative in food manufacturing.

Project goal: "{goal}"
Project phase: {phase}

Break this down into clear tasks/subtasks under the following sections:
- Engineering
- Business / Financial
- Stakeholder Engagement
- Vendor / Equipment Activities
- Safety / Compliance
- IT / Integration
- Timeline Management

Format in markdown. Be concise but specific.
"""

    chat_completion = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return chat_completion.choices[0].message.content
