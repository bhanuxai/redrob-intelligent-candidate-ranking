"""
Scoring Schema

Defines the standardized feature format expected by scorer.py.
Every module in the project should produce data matching this schema.
"""

from dataclasses import dataclass, field
from typing import Dict


@dataclass
class TechnicalFeatures:
    semantic_score: float = 0.0
    mandatory_skill_match: float = 0.0
    preferred_skill_match: float = 0.0
    experience_match: float = 0.0
    career_score: float = 0.0
    education_score: float = 0.0


@dataclass
class BehavioralFeatures:
    recruiter_response_rate: float = 0.0
    interview_completion_rate: float = 0.0
    last_active_score: float = 0.0
    open_to_work_score: float = 0.0
    github_activity_score: float = 0.0
    notice_period_score: float = 0.0


@dataclass
class RecruiterFeatures:
    saved_by_recruiters_score: float = 0.0
    search_appearance_score: float = 0.0
    profile_views_score: float = 0.0
    endorsements_score: float = 0.0


@dataclass
class RiskFeatures:
    role_mismatch_penalty: float = 0.0
    consulting_penalty: float = 0.0
    inactive_penalty: float = 0.0
    honeypot_penalty: float = 0.0


@dataclass
class CandidateFeatures:

    candidate_id: str

    technical: TechnicalFeatures = field(
        default_factory=TechnicalFeatures
    )

    behavioral: BehavioralFeatures = field(
        default_factory=BehavioralFeatures
    )

    recruiter: RecruiterFeatures = field(
        default_factory=RecruiterFeatures
    )

    risk: RiskFeatures = field(
        default_factory=RiskFeatures
    )

    metadata: Dict = field(
        default_factory=dict
    )