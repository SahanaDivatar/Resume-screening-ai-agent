import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

from src.ranking_engine import rank_resumes
from src.output_generator import (
    save_results_to_csv,
    save_results_to_json
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


save_results_to_csv(
    results,
    "output/ranked_candidates.csv"
)

save_results_to_json(
    results,
    "output/ranked_candidates.json"
)


csv_exists = Path(
    "output/ranked_candidates.csv"
).exists()

json_exists = Path(
    "output/ranked_candidates.json"
).exists()


print("\n===== OUTPUT TEST =====")

print(
    f"CSV created: {csv_exists}"
)

print(
    f"JSON created: {json_exists}"
)


if csv_exists and json_exists:
    print(
        "\nPASS: CSV and JSON outputs "
        "created successfully."
    )
else:
    print(
        "\nFAIL: Output files were not created."
    )