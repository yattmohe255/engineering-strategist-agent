from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def generate_ideas(user_input, area, constraints):
    prompt = f"""
You are a highly experienced automation design engineer focused on warehouse and logistics systems in food manufacturing.

Given the following opportunity:
{user_input}

Plant Area: {area}  
Known Constraints: {constraints}

Only consider **AGVs or AMRs** for this application. Do not include conveyors, ASRS, or other general automation technologies.

Return:
- A list of 4–6 realistic AGV/AMR implementation options
- Each should include:
  - Description of the use case
  - Handling method (pallet vs slip sheet)
  - Notes on ceiling height & floor load feasibility
  - Compatible vendors (E80, JBT, GrayOrange)
  - Estimated complexity (Low/Medium/High)

Respond in markdown format.
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
