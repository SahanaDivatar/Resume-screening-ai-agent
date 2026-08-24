import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.resume_parser import extract_resume_text
from src.candidate_extractor import extract_candidate_profile
from src.scoring_engine import score_candidate


resume_path = "data/resumes/sample_resume.txt"

jd_path = "data/job_description/junior_ai_research_associate.txt"


resume_text = extract_resume_text(resume_path)

job_description = Path(jd_path).read_text(
    encoding="utf-8"
)

candidate_profile = extract_candidate_profile(
    resume_text
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


scores = score_candidate(
    resume_text=resume_text,
    job_description=job_description,
    candidate_profile=candidate_profile,
    required_skills=required_skills
)


print("\n===== RESUME SCREENING SCORE =====\n")

print(
    f"TF-IDF Similarity: "
    f"{scores['similarity_score']}/100"
)

print(
    f"Skill Match: "
    f"{scores['skill_score']}/100"
)

print(
    f"Education Match: "
    f"{scores['education_score']}/100"
)

print(
    f"Experience Match: "
    f"{scores['experience_score']}/100"
)

print(
    f"\nFINAL SCORE: "
    f"{scores['final_score']}/100"
)


print("\n===== TEST RESULT =====")

if 0 <= scores["final_score"] <= 100:
    print("PASS: Candidate scoring works correctly.")
else:
    print("FAIL: Invalid score.")