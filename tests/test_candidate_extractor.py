import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.resume_parser import extract_resume_text
from src.candidate_extractor import extract_candidate_profile


resume_path = "data/resumes/sample_resume.txt"

resume_text = extract_resume_text(resume_path)

profile = extract_candidate_profile(resume_text)

print("\n===== CANDIDATE PROFILE =====\n")

print("Name:")
print(profile["name"])

print("\nSkills:")
print(", ".join(profile["skills"]))

print("\nEducation:")
print(profile["education"])

print("\nExperience:")
print(profile["experience"])

print("\nProjects:")
print(profile["projects"])

print("\n===== TEST RESULT =====")

if profile["name"] != "Unknown" and len(profile["skills"]) > 0:
    print("PASS: Candidate information extracted successfully.")
else:
    print("FAIL: Candidate information extraction failed.")