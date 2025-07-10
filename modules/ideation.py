import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def generate_ideas(problem_description, area="General", constraints="None"):
    prompt = f"""
You are a highly experienced automation design engineer focused on warehouse and logistics systems in food manufacturing.

Given the following opportunity:
"{description}"

Plant Area: {area}
Known Constraints: {constraints}

Only consider **AGVs or AMRs** for this application. No conveyors, shuttles, or ASRS.

Return:
- A list of 4–6 **realistic AGV/AMR implementation options**
- Each idea should include:
  - Description of the use case
  - Note on slip sheet vs pallet handling
  - Required ceiling height and floor load consideration
  - Compatibility with known vendors (E80, JBT, GrayOrange)
  - Rough feasibility / complexity level (Low/Med/High)

Return this in markdown format.
"""
    chat_completion = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return chat_completion.choices[0].message.content
