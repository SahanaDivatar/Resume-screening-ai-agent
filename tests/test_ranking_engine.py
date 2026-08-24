import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

from src.ranking_engine import rank_resumes


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


print("\n===== RANKED CANDIDATES =====\n")

for candidate in results:

    print(
        f"#{candidate['rank']} "
        f"{candidate['candidate']} "
        f"→ "
        f"{candidate['final_score']}/100"
    )


print("\n===== TEST RESULT =====")

if len(results) >= 10:

    scores = [
        candidate["final_score"]
        for candidate in results
    ]

    if scores == sorted(
        scores,
        reverse=True
    ):
        print(
            "PASS: 10+ resumes processed "
            "and correctly ranked."
        )
    else:
        print(
            "FAIL: Candidates are not "
            "properly sorted."
        )

else:

    print(
        f"FAIL: Only {len(results)} "
        "resumes were processed."
    )