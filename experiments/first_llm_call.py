import os
from openai import OpenAI

client = OpenAI()

context = """
Employees receive 25 vacation days annually.
Vacation requests of 5 or more consecutive days require manager approval.
"""

question = """
How many vacation days do employees receive annually?
"""

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="""
    You are an HR policy assistant.

    Answer the user's question using only the supplied policy context.

    If the context does not contain enough information,
    clearly state that there is insufficient information.
    """,
    input=f"""
    POLICY CONTEXT:
    {context}

    USER QUESTION:
    {question}
    """
)

print(response.output_text)