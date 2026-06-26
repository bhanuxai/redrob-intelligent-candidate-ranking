import sys
from pathlib import Path
import json

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.scorer import CandidateScorer

with open(
    "data/raw/candidates.jsonl",
    encoding="utf-8"
) as f:
    candidate = json.loads(next(f))

jd = {
    "experience": {
        "minimum": 5,
        "maximum": 9
    }
}

scorer = CandidateScorer(jd)

text = scorer.collect_candidate_text(candidate)

print(text[:700])

print()

print(
    scorer.keyword_score(
        text,
        scorer.ai_keywords
    )
)
print()

print("Title      :", scorer.score_title(candidate))
print("Summary    :", scorer.score_summary(candidate))
print("Experience :", scorer.score_experience(candidate))
print("Career     :", scorer.score_career(candidate))
print("Skills     :", scorer.score_skills(candidate))