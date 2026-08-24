from pathlib import Path
from typing import List, Dict

from src.resume_parser import extract_resume_text
from src.candidate_extractor import extract_candidate_profile
from src.scoring_engine import score_candidate


def process_resume(
    resume_path: str,
    job_description: str,
    required_skills: List[str]
) -> Dict:
    """Process and score one resume."""

    resume_text = extract_resume_text(resume_path)

    profile = extract_candidate_profile(resume_text)

    scores = score_candidate(
        resume_text=resume_text,
        job_description=job_description,
        candidate_profile=profile,
        required_skills=required_skills
    )

    return {
        "candidate": profile["name"],
        "resume": Path(resume_path).name,
        "skills": ", ".join(profile["skills"]),
        "final_score": scores["final_score"],
        "similarity_score": scores["similarity_score"],
        "skill_score": scores["skill_score"],
        "education_score": scores["education_score"],
        "experience_score": scores["experience_score"],
    }


def rank_resumes(
    resume_directory: str,
    job_description: str,
    required_skills: List[str]
) -> List[Dict]:
    """Process all supported resumes and rank them."""

    directory = Path(resume_directory)

    results = []

    supported_extensions = {
        ".pdf",
        ".docx",
        ".txt"
    }

    for resume_path in directory.iterdir():

        if resume_path.suffix.lower() not in supported_extensions:
            continue

        try:
            result = process_resume(
                str(resume_path),
                job_description,
                required_skills
            )

            results.append(result)

        except Exception as error:
            print(
                f"Could not process "
                f"{resume_path.name}: {error}"
            )

    results.sort(
        key=lambda candidate: candidate["final_score"],
        reverse=True
    )

    for rank, candidate in enumerate(
        results,
        start=1
    ):
        candidate["rank"] = rank

    return results