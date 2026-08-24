from pathlib import Path

from src.ranking_engine import rank_resumes
from src.ai_reasoning import generate_candidate_reasoning
from src.output_generator import (
    save_results_to_csv,
    save_results_to_json
)


# ============================================================
# CONFIGURATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

RESUME_DIRECTORY = BASE_DIR / "data" / "resumes"

JOB_DESCRIPTION_FILE = (
    BASE_DIR
    / "data"
    / "job_description"
    / "junior_ai_research_associate.txt"
)

OUTPUT_DIRECTORY = BASE_DIR / "output"


REQUIRED_SKILLS = [
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


# ============================================================
# MAIN AGENT
# ============================================================

def main():

    print("\n" + "=" * 60)
    print("        AI RESUME SCREENING AGENT")
    print("=" * 60)

    # --------------------------------------------------------
    # 1. Load Job Description
    # --------------------------------------------------------

    print("\n[1/5] Loading Job Description...")

    if not JOB_DESCRIPTION_FILE.exists():

        print(
            f"ERROR: Job description not found:\n"
            f"{JOB_DESCRIPTION_FILE}"
        )

        return

    job_description = JOB_DESCRIPTION_FILE.read_text(
        encoding="utf-8"
    )

    print("Job Description loaded successfully.")


    # --------------------------------------------------------
    # 2. Find Resumes
    # --------------------------------------------------------

    print("\n[2/5] Searching for resumes...")

    if not RESUME_DIRECTORY.exists():

        print(
            f"ERROR: Resume directory not found:\n"
            f"{RESUME_DIRECTORY}"
        )

        return

    resume_files = [
        file
        for file in RESUME_DIRECTORY.iterdir()
        if file.suffix.lower() in {
            ".pdf",
            ".docx",
            ".txt"
        }
    ]

    print(
        f"Found {len(resume_files)} resume(s)."
    )

    if not resume_files:

        print("ERROR: No resumes found.")

        return


    # --------------------------------------------------------
    # 3. Score and Rank Candidates
    # --------------------------------------------------------

    print("\n[3/5] Screening and ranking candidates...")

    results = rank_resumes(
        resume_directory=str(RESUME_DIRECTORY),
        job_description=job_description,
        required_skills=REQUIRED_SKILLS
    )

    print(
        f"Successfully processed "
        f"{len(results)} candidate(s)."
    )


    # --------------------------------------------------------
    # 4. Generate AI Reasoning
    # --------------------------------------------------------

    print("\n[4/5] Generating AI reasoning...")

    for index, candidate in enumerate(
        results,
        start=1
    ):

        print(
            f"  Analyzing "
            f"{candidate['candidate']} "
            f"({index}/{len(results)})..."
        )

        try:

            reasoning = generate_candidate_reasoning(
                candidate,
                job_description
            )

            candidate["ai_reasoning"] = reasoning

        except Exception as error:

            candidate["ai_reasoning"] = (
                "AI reasoning unavailable: "
                f"{error}"
            )


    # --------------------------------------------------------
    # 5. Save Results
    # --------------------------------------------------------

    print("\n[5/5] Saving screening results...")

    OUTPUT_DIRECTORY.mkdir(
        parents=True,
        exist_ok=True
    )

    csv_path = (
        OUTPUT_DIRECTORY
        / "ranked_candidates.csv"
    )

    json_path = (
        OUTPUT_DIRECTORY
        / "ranked_candidates.json"
    )


    save_results_to_csv(
        results,
        str(csv_path)
    )

    save_results_to_json(
        results,
        str(json_path)
    )


    # --------------------------------------------------------
    # Final Results
    # --------------------------------------------------------

    print("\n" + "=" * 60)
    print("              SCREENING RESULTS")
    print("=" * 60)

    print(
        "\nRank | Candidate              | Score"
    )

    print("-" * 60)

    for candidate in results:

        print(
            f"{candidate['rank']:>4} | "
            f"{candidate['candidate']:<22} | "
            f"{candidate['final_score']:.2f}/100"
        )


    print("\n" + "=" * 60)

    print(
        f"CSV output : {csv_path}"
    )

    print(
        f"JSON output: {json_path}"
    )

    print("=" * 60)

    print(
        "\nAI Resume Screening Agent completed successfully."
    )


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()