"""
Candidate Ranker

Loads candidates, scores them and returns Top-K.
"""

from __future__ import annotations

import json
from typing import Dict, List

from src.scorer import CandidateScorer
from src.behavior import BehaviorScorer
from src.semantic_matcher import SemanticMatcher


class CandidateRanker:

    def __init__(self, jd: Dict):

        self.jd = jd
        self.scorer = CandidateScorer(jd)
        self.behavior = BehaviorScorer()
        self.semantic = SemanticMatcher()

    # --------------------------------------------------

    def load_candidates(
        self,
        file_path: str
    ):

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

            for line in f:

                line = line.strip()

                if line:
                    yield json.loads(line)

    # --------------------------------------------------

    def score_candidate(
        self,
        candidate: Dict
    ) -> float:
        semantic = self.semantic.score(candidate)
        technical = (
            semantic*0.40 +

            self.scorer.score_title(candidate) * 0.15 +

            self.scorer.score_experience(candidate) * 0.10 +

            self.scorer.score_career(candidate) * 0.20 +

            self.scorer.score_skills(candidate) * 0.15

        )

        behavior = self.behavior.score(candidate)

        final = (

            technical * 0.75 +

            behavior * 0.25

        )

        return round(final, 4)

    # --------------------------------------------------

    def rank_candidates(
        self,
        file_path: str,
        top_k: int = 100
    ) -> List[Dict]:

        ranked = []

        for candidate in self.load_candidates(file_path):

            score = self.score_candidate(candidate)

            ranked.append({

                "candidate_id": candidate["candidate_id"],

                "score": score

            })

        ranked.sort(

            key=lambda x: x["score"],

            reverse=True

        )

        return ranked[:top_k]