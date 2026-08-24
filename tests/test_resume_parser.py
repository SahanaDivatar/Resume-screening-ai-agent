import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.resume_parser import extract_resume_text


resume_path = "data/resumes/sample_resume.txt"

text = extract_resume_text(resume_path)

print("\n===== EXTRACTED RESUME TEXT =====\n")
print(text)

print("\n===== TEST RESULT =====")

if "Sahana Divatar" in text:
    print("PASS: Resume text extracted successfully.")
else:
    print("FAIL: Resume text extraction failed.")