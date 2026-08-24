import csv
import json
from pathlib import Path
from typing import List, Dict


def save_results_to_csv(
    results: List[Dict],
    output_path: str
) -> None:
    """Save ranked candidates to a CSV file."""

    if not results:
        return

    output_file = Path(output_path)
    output_file.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    fieldnames = [
        "rank",
        "candidate",
        "resume",
        "final_score",
        "similarity_score",
        "skill_score",
        "education_score",
        "experience_score",
        "skills",
        "ai_reasoning",
    ]

    with output_file.open(
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for result in results:
            writer.writerow({
                field: result.get(field, "")
                for field in fieldnames
            })


def save_results_to_json(
    results: List[Dict],
    output_path: str
) -> None:
    """Save ranked candidates to a JSON file."""

    output_file = Path(output_path)
    output_file.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with output_file.open(
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            results,
            file,
            indent=4
        )