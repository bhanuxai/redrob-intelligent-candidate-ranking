"""
JD Understanding

Converts parsed JD into a normalized requirement object
used by the ranking engine.
"""

from typing import Dict


class JDUnderstanding:

    def __init__(self, jd: Dict):
        self.jd = jd

    def get_requirements(self) -> Dict:

        return {

            "role": self.jd.get("role"),

            "experience": self.jd.get("experience"),

            "mandatory_skills": self.jd.get(
                "mandatory_skills", []
            ),

            "preferred_skills": self.jd.get(
                "preferred_skills", []
            ),

            "preferred_locations": self.jd.get(
                "preferred_locations", []
            ),

            "work_mode": self.jd.get(
                "work_mode"
            ),

            "company_stage": self.jd.get(
                "company_stage"
            ),

            "preferred_notice_days": self.jd.get(
                "preferred_notice_days"
            ),

            "disqualifiers": self.jd.get(
                "disqualifiers", []
            ),

            "behavior_requirements": self.jd.get(
                "behavior_requirements", []
            ),

            "requires_production_ml": self.jd.get(
                "requires_production_ml", False
            ),

            "requires_product_engineering": self.jd.get(
                "requires_product_engineering", False
            )

        }