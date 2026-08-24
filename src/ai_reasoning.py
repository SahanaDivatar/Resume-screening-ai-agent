import os
from typing import Dict

from dotenv import load_dotenv
from groq import Groq


# Load variables from .env
load_dotenv()


# Get Groq API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY is not configured. "
        "Please add it to the .env file."
    )


# Create Groq client
client = Groq(api_key=api_key)


def generate_candidate_reasoning(
    candidate: Dict,
    job_description: str
) -> str:
    """
    Generate an AI explanation for a candidate's
    existing screening score.

    The AI does NOT calculate or change the score.
    It only explains the existing result.
    """

    prompt = f"""
You are an AI recruitment screening assistant.

Your task is to explain why a candidate received
their existing screening score.

IMPORTANT RULES:

1. Do NOT change the numerical score.
2. Do NOT invent skills, experience, education,
   or projects.
3. Use only the information provided.
4. Identify skills that match the job description.
5. Identify important missing skills when relevant.
6. Keep the explanation concise and professional.
7. Do not make decisions based on protected
   characteristics.
8. Do not claim that the candidate is definitely
   qualified or unqualified.

JOB DESCRIPTION:

{job_description}

CANDIDATE:

Name:
{candidate["candidate"]}

Skills:
{candidate["skills"]}

NLP Similarity Score:
{candidate["similarity_score"]}/100

Skill Match Score:
{candidate["skill_score"]}/100

Education Match Score:
{candidate["education_score"]}/100

Experience Match Score:
{candidate["experience_score"]}/100

Final Screening Score:
{candidate["final_score"]}/100

Provide a short explanation containing:

- Overall alignment
- Strong matching skills
- Important gaps, if any
- Why the candidate received this score

Do not calculate a new score.
Do not change the existing score.
"""


    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a careful and factual "
                    "recruitment screening assistant."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=300
    )


    return response.choices[0].message.content.strip()