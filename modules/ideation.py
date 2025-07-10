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

Provide a list of 3–5 distinct automation concepts. Each idea should be clearly titled (e.g., '1. Fork AMR for Slip Sheet Delivery'), with a brief explanation, key benefits, and any risks. Avoid generic answers. These ideas should reflect real engineering considerations like space limits, hygiene zones, load handling types, etc.
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
\"{question}\"

Please refine, expand, or iterate on the selected ideas based on the user’s input. Respond in markdown with clear headers.
"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def parse_options(response_text):
    """
    Extract only the top-level idea headers from the markdown-formatted response.
    Returns a list like: '1. Fork AMR for Slip Sheet Delivery'
    """
    pattern = re.compile(r"^\\d+\\.\\s+.+")  # Match numbered headers only
    options = [line.strip() for line in response_text.splitlines() if pattern.match(line)]
    return options
