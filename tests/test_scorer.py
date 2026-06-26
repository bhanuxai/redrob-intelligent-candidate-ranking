import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.scorer import CandidateScorer

jd = {}

scorer = CandidateScorer(jd)

signals = {

    "recruiter_response_rate": 0.90,

    "interview_completion_rate": 0.95,

    "last_active_score": 1.0,

    "open_to_work_score": 1.0,

    "github_activity_score": 0.80,

    "notice_period_score": 0.90,

    "profile_completeness_score": 1.0,
}

risk = {

    "role_mismatch": False,

    "inactive_profile": False,

    "long_notice_period": False,
}

result = scorer.score_candidate(

    semantic_score=0.90,

    skill_score=0.85,

    experience_score=0.95,

    career_score=0.90,

    education_score=0.80,

    signals=signals,

    risk=risk

)

print(result)