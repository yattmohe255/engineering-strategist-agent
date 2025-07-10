import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def fill_fel_template(name, opportunity, risks, roi):
    prompt = f"""
Create a concise FEL (Front-End Loading) style project summary for a food manufacturing automation initiative.

Project Name: {name}
Opportunity: {opportunity}
Risks/Barriers: {risks}
Estimated ROI or Payback: {roi}

Output format:
1. Executive Summary
2. Problem Statement
3. Proposed Solution (both traditional and advanced automation ideas)
4. Risk Mitigation
5. Estimated ROI / Financial Justification
6. Strategic Fit
7. Open Questions

Format in markdown.
"""

    chat_completion = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return chat_completion.choices[0].message.content
