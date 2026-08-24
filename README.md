# AI Resume Screening Agent

An end-to-end AI-powered Resume Screening Agent built for the ROOMAN Technologies Junior AI Research Associate 24-Hour AI Agent Challenge.

The system takes a Job Description and a collection of resumes, extracts candidate information, calculates relevance scores, ranks candidates, and uses an LLM to generate explanations for the screening results.

## 1. Problem Statement

Recruiters may need to screen a large number of resumes against a single Job Description.

This project automates the first stage of recruitment by:

- Parsing resumes
- Extracting candidate information
- Comparing resumes against a Job Description
- Calculating NLP similarity
- Matching required skills
- Ranking candidates
- Generating AI explanations
- Exporting results as CSV and JSON

## 2. Agent Objective

The agent takes:

> A Job Description + a folder containing candidate resumes

and produces:

> A scored and ranked shortlist of candidates with AI-generated explanations.

## 3. Architecture

```text
                 Job Description
                       |
                       v
                Resume Collection
                       |
                       v
                  Resume Parser
                       |
                       v
            Candidate Information
                  Extraction
                       |
                       v
          ---------------------------
          |                         |
          v                         v
     TF-IDF Similarity         Skill Matching
          |                         |
          -----------+--------------
                     |
                     v
              Scoring Engine
                     |
                     v
              Ranking Engine
                     |
                     v
                  Groq LLM
                     |
                     v
              AI Explanation
                     |
                     v
              ----------------
              |              |
              v              v
             CSV            JSON

4. Features
Resume Parsing

Supports:

PDF
DOCX
TXT
Candidate Information Extraction

The system extracts:

Candidate name
Skills
Education
Experience
Projects
NLP Similarity

TF-IDF vectorization and cosine similarity are used to measure textual relevance between the resume and Job Description.

Skill Matching

Required skills from the Job Description are compared against candidate skills.

Candidate Ranking

Candidates receive a final score and are sorted from highest to lowest.

AI Reasoning

An LLM generates explanations covering:

Overall alignment
Matching skills
Important gaps
Reasoning behind the screening result

The LLM does not modify the numerical screening score.

Batch Processing

The system can process 10+ resumes in a single run.

Structured Output

Results are exported to:

output/ranked_candidates.csv
output/ranked_candidates.json

5. Technology Stack
Technology	Purpose
Python	Core implementation
scikit-learn	TF-IDF and cosine similarity
Groq	LLM inference
python-dotenv	Environment variable management
PyPDF2	PDF parsing
python-docx	DOCX parsing
Pandas	Data processing
CSV	Structured output
JSON	Structured output
Git/GitHub	Version control

6. Project Structure

Resume-screening-ai-agent/
│
├── data/
│   ├── resumes/
│   │   ├── candidate1.pdf
│   │   ├── candidate2.pdf
│   │   └── ...
│   │
│   └── job_description/
│       └── junior_ai_research_associate.txt
│
├── output/
│   ├── ranked_candidates.csv
│   └── ranked_candidates.json
│
├── src/
│   ├── resume_parser.py
│   ├── candidate_extractor.py
│   ├── scoring_engine.py
│   ├── ranking_engine.py
│   ├── output_generator.py
│   └── ai_reasoning.py
│
├── tests/
│   ├── test_candidate_extractor.py
│   ├── test_scoring_engine.py
│   ├── test_ranking_engine.py
│   ├── test_output_generator.py
│   └── test_ai_reasoning.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md

7. Requirements

Python 3.10 or newer is recommended.

Install the dependencies:
pip install -r requirements.txt

8. API Key Configuration

This project uses Groq for AI reasoning.
Create a .env file in the project root:

GROQ_API_KEY=your_groq_api_key

Do not commit the .env file to GitHub.
The .gitignore file excludes:

.env

9. Running the Agent

Activate the virtual environment:

.\venv\Scripts\Activate.ps1

Run the complete agent:

python main.py

The agent will:

Load the Job Description
Find candidate resumes
Parse resumes
Extract candidate information
Calculate screening scores
Rank candidates
Generate AI reasoning
Save CSV and JSON results
10. Example Output

Example ranking:

============================================================
              SCREENING RESULTS
============================================================

Rank | Candidate              | Score
------------------------------------------------------------
   1 | Sneha Rao              | 60.23/100
   2 | Ananya Patel           | 55.14/100
   3 | Rahul Sharma           | 51.92/100
   4 | Arjun Reddy            | 51.81/100
   5 | Vikram Rao             | 47.27/100

The exact results depend on the provided resumes and Job Description.

11. Scoring Method

The agent uses a transparent weighted scoring approach.

Each candidate receives four component scores between 0 and 100.

1. TF-IDF Similarity — 50%

The resume and Job Description are converted into TF-IDF vectors.

Cosine similarity is calculated between the two vectors.

This measures how closely the candidate's resume text matches the Job Description.

Formula:

TF-IDF Score = Cosine Similarity × 100
2. Skill Match — 30%

The system compares the required skills with the skills extracted from the candidate's resume.

Formula:

Skill Match =
(Number of matched required skills /
 Number of required skills) × 100

Skill comparison is case-insensitive.

3. Education Match — 10%

The system checks whether the candidate's education contains relevant fields such as:

Computer Science
Information Technology
Artificial Intelligence
Data Science
Computer Engineering
4. Experience Match — 10%

The experience component is designed for the target junior/0–1 year role.

Candidates with internship, trainee, or other extracted experience currently receive a score of 100.

Candidates with no extracted experience receive a neutral score of 50.

This is a deliberately simple baseline and could be improved in a future version using more detailed experience matching.

Final Score

The final score is calculated as:

Final Score =
(TF-IDF × 0.50)
+ (Skill Match × 0.30)
+ (Education × 0.10)
+ (Experience × 0.10)

Example:

TF-IDF Similarity = 13.04
Skill Match       = 55.56
Education Match   = 100
Experience Match  = 100

Final Score =
(13.04 × 0.50)
+ (55.56 × 0.30)
+ (100 × 0.10)
+ (100 × 0.10)

= 43.19 / 100

The numerical score is calculated deterministically by the scoring engine.

The LLM is not responsible for calculating or modifying the numerical score.

12. AI Reasoning

After numerical screening and ranking, the system sends the candidate's extracted information and scoring details to the LLM.

The LLM generates a concise explanation containing:

Overall alignment
Matching skills
Missing or weaker areas
Explanation of the existing score

This separation keeps numerical screening deterministic while using the LLM for natural-language interpretation.

13. Sample Candidate Screening

Example:

Candidate: Sneha Rao

Final Score: 60.23/100

AI Explanation:

The candidate demonstrates strong alignment with the role
through relevant programming, machine learning and API
development skills. The profile shows several skills that
match the requirements of the Job Description, while some
required areas have weaker or limited evidence.
14. Testing

Individual components can be tested separately.

Candidate extraction
python tests/test_candidate_extractor.py
Scoring
python tests/test_scoring_engine.py
Ranking
python tests/test_ranking_engine.py
Output generation
python tests/test_output_generator.py
AI reasoning
python tests/test_ai_reasoning.py
Complete end-to-end agent
python main.py
15. Design Decisions
Why Python?

Python provides strong support for:

NLP
Machine Learning
Document processing
LLM APIs

It also allowed the project to remain small and easy to run within the 24-hour challenge.

Why TF-IDF?

TF-IDF provides a simple and interpretable baseline for measuring textual similarity.

It is lightweight and deterministic.

Why Skill Matching?

Pure text similarity may not adequately identify whether a candidate possesses specific required skills.

Skill matching provides an additional signal.

Why Use an LLM?

Traditional scoring produces numerical results but does not explain them naturally.

The LLM is therefore used after scoring to generate human-readable reasoning.

16. Tradeoffs and Limitations
TF-IDF Limitations

TF-IDF is keyword-based and does not fully understand semantic meaning.

For example, two phrases with similar meaning may receive a lower similarity score if their wording differs.

A future version could use sentence embeddings or a dedicated semantic similarity model.

Skill Extraction Limitations

Resume formatting and wording vary between candidates.

Some skills may therefore be missed during extraction.

A future version could use an LLM or NER model specifically for structured skill extraction.

LLM Dependency

AI reasoning requires access to the Groq API.

If the API is unavailable, numerical screening can still be performed, but AI explanations cannot be generated.

No Final Hiring Decision

This system is intended as a screening assistance tool.

It should not make autonomous hiring decisions.

Human review remains necessary.

17. Responsible AI Considerations

The system focuses on job-relevant information such as:

Skills
Education
Experience
Resume/JD relevance

It does not intentionally use protected personal characteristics for ranking.

The generated result should be treated as decision support, not as a final hiring decision.

## 18. Sample Data

The repository contains 12 synthetic sample resumes for demonstrating
batch screening across multiple resume formats.

The sample dataset includes:

- 10 TXT resumes
- 1 PDF resume
- 1 DOCX resume

The agent processes all supported formats in a single run.

Running:

python main.py

processes the complete sample dataset and generates the ranked
CSV and JSON outputs.
19. Future Improvements

With additional development time, the system could be extended with:

Sentence-transformer embeddings
Better semantic matching
Advanced resume section detection
Improved skill normalization
Interactive web dashboard
Recruiter filters
Explainable score breakdown
Human review workflow
Database storage
Evaluation against a labelled recruitment dataset
20. Challenge Deliverables

This repository contains:

Job Description
10+ sample resumes
Resume parsing
Candidate information extraction
NLP similarity scoring
Skill matching
Candidate ranking
AI-generated reasoning
CSV output
JSON output
Test scripts
Setup instructions
Tradeoff and limitation notes
Author

Sahana Divatar

Built for the ROOMAN Technologies Junior AI Research Associate — 24-Hour AI Agent Challenge.
