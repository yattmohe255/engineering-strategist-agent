import os
from openai import OpenAI
from dotenv import load_dotenv
import re

load_dotenv()
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def generate_ideas(description, area, constraints):
    prompt = f"""
You are an expert in industrial automation and warehouse systems. The user is an engineer designing a new automation solution using AGVs or AMRs. Given the following details:

Project Description:
{description}

Plant Area or Context:
{area}

Constraints:
{constraints}

Provide a list of 3–5 distinct automation concepts. Format each as:
1. Idea Title  
Explanation (2–4 sentences)  
**Benefits:** ...  
**Risks:** ...
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def refine_ideas(selected_ideas, question):
    prompt = f"""
The user has selected these ideas for refinement:

{selected_ideas}

They also asked this follow-up question or clarification:
"{question}"

Please refine, expand, or iterate on the selected ideas based on the user’s input. Respond in markdown with clear headers.
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def parse_options(response_text):
    pattern = re.compile(r"^\d+\.\s+.+")
    options = [line.strip() for line in response_text.splitlines() if pattern.match(line)]
    return options
