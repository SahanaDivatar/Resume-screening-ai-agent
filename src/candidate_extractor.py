import re
from typing import Dict, List


COMMON_SKILLS = [
    "Python",
    "Java",
    "C++",
    "C",
    "JavaScript",
    "TypeScript",
    "React",
    "React.js",
    "Next.js",
    "HTML",
    "CSS",
    "SQL",
    "MySQL",
    "PostgreSQL",
    "Oracle",
    "MongoDB",
    "Spring Boot",
    "Spring",
    "Hibernate",
    "Django",
    "Flask",
    "FastAPI",
    "REST API",
    "REST APIs",
    "Git",
    "GitHub",
    "Docker",
    "AWS",
    "Azure",
    "Machine Learning",
    "Artificial Intelligence",
    "AI",
    "NLP",
    "Pandas",
    "NumPy",
    "Scikit-learn",
    "TensorFlow",
    "PyTorch",
]


def extract_name(text: str) -> str:
    """Extract the likely candidate name from the beginning of the resume."""

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    if not lines:
        return "Unknown"

    # Usually the candidate name is near the beginning.
    for line in lines[:5]:
        if len(line.split()) <= 5 and not any(
            keyword in line.lower()
            for keyword in [
                "resume",
                "curriculum vitae",
                "email",
                "phone",
                "linkedin",
                "github",
            ]
        ):
            return line

    return "Unknown"


def extract_skills(text: str) -> List[str]:
    """Find known technical skills mentioned in the resume."""

    text_lower = text.lower()

    found_skills = []

    for skill in COMMON_SKILLS:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    return found_skills


def extract_section(text: str, section_names: List[str]) -> str:
    """
    Extract text belonging to a resume section.

    Stops when another common section heading is found.
    """

    lines = text.splitlines()

    start_index = None

    for i, line in enumerate(lines):
        normalized = line.strip().lower()

        if normalized in [name.lower() for name in section_names]:
            start_index = i + 1
            break

    if start_index is None:
        return ""

    common_sections = [
        "education",
        "skills",
        "experience",
        "work experience",
        "projects",
        "certifications",
        "summary",
        "objective",
        "contact",
        "achievements",
    ]

    collected = []

    for line in lines[start_index:]:
        normalized = line.strip().lower()

        if normalized in common_sections:
            break

        if line.strip():
            collected.append(line.strip())

    return "\n".join(collected).strip()


def extract_candidate_profile(text: str) -> Dict:
    """Extract structured candidate information from resume text."""

    profile = {
        "name": extract_name(text),
        "skills": extract_skills(text),
        "education": extract_section(
            text,
            ["Education"]
        ),
        "experience": extract_section(
            text,
            ["Experience", "Work Experience"]
        ),
        "projects": extract_section(
            text,
            ["Projects"]
        ),
    }

    return profile