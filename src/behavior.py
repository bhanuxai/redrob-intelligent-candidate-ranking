"""
Behavior Scorer

Computes candidate availability and recruiter engagement score.
"""

from __future__ import annotations

from datetime import datetime
from typing import Dict


class BehaviorScorer:

    def __init__(self):
        pass

    # --------------------------------------------------

    def recency_score(self, last_active_date: str) -> float:

        try:
            last = datetime.strptime(
                last_active_date,
                "%Y-%m-%d"
            )

            days = (datetime.now() - last).days

            if days <= 7:
                return 1.0

            if days <= 30:
                return 0.8

            if days <= 90:
                return 0.5

            return 0.2

        except Exception:
            return 0.3

    # --------------------------------------------------

    def score(self, candidate: Dict) -> float:

        s = candidate["redrob_signals"]

        score = 0

        # Recruiter response
        score += (
            s["recruiter_response_rate"]
            * 0.25
        )

        # Interview completion
        score += (
            s["interview_completion_rate"]
            * 0.20
        )

        # GitHub activity
        github = max(
            0,
            s["github_activity_score"]
        )

        score += (
            github / 100
        ) * 0.15

        # Recent activity
        score += (
            self.recency_score(
                s["last_active_date"]
            )
        ) * 0.15

        # Open to work
        if s["open_to_work_flag"]:
            score += 0.10

        # Notice period
        notice = s["notice_period_days"]

        if notice <= 30:
            score += 0.10

        elif notice <= 60:
            score += 0.05

        # Recruiter interest
        score += min(
            s["saved_by_recruiters_30d"] / 20,
            1
        ) * 0.05

        return round(
            min(score, 1.0),
            4
        )