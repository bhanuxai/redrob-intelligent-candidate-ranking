"""
Global configuration for the Candidate Ranking System.
Modify weights here instead of changing scorer.py.
"""

# -----------------------------
# Embedding Model
# -----------------------------
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# -----------------------------
# Ranking
# -----------------------------
TOP_K = 100

# -----------------------------
# Technical Score Weights
# -----------------------------
SEMANTIC_WEIGHT = 0.35
SKILL_WEIGHT = 0.25
EXPERIENCE_WEIGHT = 0.15
CAREER_WEIGHT = 0.10
EDUCATION_WEIGHT = 0.05

# -----------------------------
# Behaviour Score
# -----------------------------
BEHAVIOUR_WEIGHT = 0.10

# -----------------------------
# Behaviour Signal Weights
# -----------------------------
RESPONSE_RATE_WEIGHT = 0.25
INTERVIEW_COMPLETION_WEIGHT = 0.20
LAST_ACTIVE_WEIGHT = 0.15
OPEN_TO_WORK_WEIGHT = 0.15
GITHUB_ACTIVITY_WEIGHT = 0.10
NOTICE_PERIOD_WEIGHT = 0.10
PROFILE_COMPLETENESS_WEIGHT = 0.05

# -----------------------------
# Penalties
# -----------------------------
ROLE_MISMATCH_PENALTY = 0.25
INACTIVE_PROFILE_PENALTY = 0.15
LONG_NOTICE_PERIOD_PENALTY = 0.10

# -----------------------------
# Work Modes
# -----------------------------
VALID_WORK_MODES = [
    "remote",
    "hybrid",
    "onsite",
    "flexible"
]

# -----------------------------
# Common Degrees
# -----------------------------
VALID_DEGREES = [
    "B.Tech",
    "BE",
    "BSc",
    "M.Tech",
    "ME",
    "MSc",
    "PhD",
    "MBA"
]