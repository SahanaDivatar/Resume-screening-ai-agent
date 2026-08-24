import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

from src.ranking_engine import rank_resumes
from src.ai_reasoning import (
    generate_candidate_reasoning
)


resume_directory = "data/resumes"

jd_path = (
    "data/job_description/"
    "junior_ai_research_associate.txt"
)

job_description = Path(jd_path).read_text(
    encoding="utf-8"
)

required_skills = [
    "Python",
    "Artificial Intelligence",
    "Machine Learning",
    "NLP",
    "SQL",
    "REST APIs",
    "Git",
    "Problem Solving",
    "Data Processing"
]


results = rank_resumes(
    resume_directory=resume_directory,
    job_description=job_description,
    required_skills=required_skills
)


top_candidate = results[0]


print("\n===== AI REASONING TEST =====\n")

print(
    f"Candidate: "
    f"{top_candidate['candidate']}"
)

print(
    f"Score: "
    f"{top_candidate['final_score']}/100"
)

print("\nAI Explanation:\n")


reasoning = generate_candidate_reasoning(
    top_candidate,
    job_description
)

print(reasoning)


print("\n===== TEST RESULT =====")

if reasoning.strip():
    print(
        "PASS: AI reasoning generated successfully."
    )
else:
    print(
        "FAIL: AI reasoning was empty."
    )