"""
Global configuration for the Redrob Candidate Ranking System.
"""

from pathlib import Path

# =====================================================
# Project Paths
# =====================================================

BASE_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = BASE_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

CACHE_DIR = BASE_DIR / "cache"

OUTPUT_DIR = BASE_DIR / "outputs"

MODEL_DIR = BASE_DIR / "models"

TEST_DIR = BASE_DIR / "tests"

# =====================================================
# Dataset Files
# =====================================================

JOB_DESCRIPTION_PATH = RAW_DATA_DIR / "job_description.docx"

CANDIDATE_FILE = RAW_DATA_DIR / "candidates.jsonl"

SAMPLE_CANDIDATE_FILE = RAW_DATA_DIR / "sample_candidates.json"

SCHEMA_FILE = RAW_DATA_DIR / "candidate_schema.json"

# =====================================================
# Embedding Model
# =====================================================

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# =====================================================
# Ranking
# =====================================================

TOP_K = 100

# =====================================================
# Technical Weights
# =====================================================

SEMANTIC_WEIGHT = 0.35
SKILL_WEIGHT = 0.25
EXPERIENCE_WEIGHT = 0.15
CAREER_WEIGHT = 0.10
EDUCATION_WEIGHT = 0.05

# =====================================================
# Behaviour
# =====================================================

BEHAVIOUR_WEIGHT = 0.10

RESPONSE_RATE_WEIGHT = 0.25
INTERVIEW_COMPLETION_WEIGHT = 0.20
LAST_ACTIVE_WEIGHT = 0.15
OPEN_TO_WORK_WEIGHT = 0.15
GITHUB_ACTIVITY_WEIGHT = 0.10
NOTICE_PERIOD_WEIGHT = 0.10
PROFILE_COMPLETENESS_WEIGHT = 0.05

# =====================================================
# Penalties
# =====================================================

ROLE_MISMATCH_PENALTY = 0.25

INACTIVE_PROFILE_PENALTY = 0.15

LONG_NOTICE_PERIOD_PENALTY = 0.10

# =====================================================
# Supported Work Modes
# =====================================================

VALID_WORK_MODES = [
    "remote",
    "hybrid",
    "onsite",
    "flexible",
]