"""
Project Configuration
"""

# Embedding Model
MODEL_NAME = "all-MiniLM-L6-v2"

# Ranking
TOP_K = 100

# Scoring Weights (Total = 100)
SEMANTIC_WEIGHT = 40
SKILL_WEIGHT = 20
EXPERIENCE_WEIGHT = 15
EDUCATION_WEIGHT = 10
SIGNAL_WEIGHT = 10
CERTIFICATION_WEIGHT = 5

# Supported Degrees
VALID_DEGREES = [
    "B.Tech",
    "BE",
    "M.Tech",
    "ME",
    "B.Sc",
    "M.Sc",
    "MBA",
    "PhD"
]