from typing import Dict, List

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_tfidf_similarity(
    resume_text: str,
    job_description: str
) -> float:
    """
    Calculate semantic similarity between a resume
    and a job description using TF-IDF and cosine similarity.

    Returns:
        Similarity score from 0 to 100.
    """

    if not resume_text.strip() or not job_description.strip():
        return 0.0

    documents = [
        resume_text,
        job_description
    ]

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0]

    return round(similarity * 100, 2)


def calculate_skill_match(
    candidate_skills: List[str],
    required_skills: List[str]
) -> float:
    """
    Calculate percentage of required skills
    found in the candidate's skills.
    """

    if not required_skills:
        return 0.0

    candidate_skills_lower = {
        skill.lower()
        for skill in candidate_skills
    }

    required_skills_lower = {
        skill.lower()
        for skill in required_skills
    }

    matched_skills = (
        candidate_skills_lower
        & required_skills_lower
    )

    score = (
        len(matched_skills)
        / len(required_skills_lower)
    ) * 100

    return round(score, 2)


def calculate_education_match(
    education: str,
    job_description: str
) -> float:
    """
    Check whether the candidate's education
    appears relevant to the job description.
    """

    education_keywords = [
        "computer science",
        "information technology",
        "artificial intelligence",
        "data science",
        "computer engineering"
    ]

    education_lower = education.lower()

    job_lower = job_description.lower()

    candidate_has_relevant_education = any(
        keyword in education_lower
        for keyword in education_keywords
    )

    job_requires_relevant_education = any(
        keyword in job_lower
        for keyword in education_keywords
    )

    if (
        candidate_has_relevant_education
        and job_requires_relevant_education
    ):
        return 100.0

    return 0.0


def calculate_experience_match(
    experience: str
) -> float:
    """
    Basic experience scoring.

    Fresh graduates / 0-1 year candidates are
    considered suitable for the target role.
    """

    if not experience.strip():
        return 50.0

    experience_lower = experience.lower()

    internship_keywords = [
        "intern",
        "internship",
        "trainee"
    ]

    if any(
        keyword in experience_lower
        for keyword in internship_keywords
    ):
        return 100.0

    return 100.0


def calculate_final_score(
    similarity_score: float,
    skill_score: float,
    education_score: float,
    experience_score: float
) -> float:
    """
    Calculate weighted final candidate score.

    Weights:
        TF-IDF similarity = 50%
        Skill match       = 30%
        Education match   = 10%
        Experience match  = 10%
    """

    final_score = (
        similarity_score * 0.50
        + skill_score * 0.30
        + education_score * 0.10
        + experience_score * 0.10
    )

    return round(final_score, 2)


def score_candidate(
    resume_text: str,
    job_description: str,
    candidate_profile: Dict,
    required_skills: List[str]
) -> Dict:
    """
    Calculate all scoring components for one candidate.
    """

    similarity_score = calculate_tfidf_similarity(
        resume_text,
        job_description
    )

    skill_score = calculate_skill_match(
        candidate_profile["skills"],
        required_skills
    )

    education_score = calculate_education_match(
        candidate_profile["education"],
        job_description
    )

    experience_score = calculate_experience_match(
        candidate_profile["experience"]
    )

    final_score = calculate_final_score(
        similarity_score,
        skill_score,
        education_score,
        experience_score
    )

    return {
        "similarity_score": similarity_score,
        "skill_score": skill_score,
        "education_score": education_score,
        "experience_score": experience_score,
        "final_score": final_score
    }