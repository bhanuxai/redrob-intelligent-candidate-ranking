"""
Job Description Parser

Converts a raw Job Description into structured metadata
used by the ranking engine.
"""

from pathlib import Path

from src.utils import clean_text


class JDParser:

    def __init__(self):
        self.raw_text = ""
        self.cleaned_text = ""

    def load(self, file_path: str):

        path = Path(file_path)

        self.raw_text = path.read_text(
            encoding="utf-8"
        )

        self.cleaned_text = clean_text(
            self.raw_text
        )

        return self.cleaned_text

    def parse(self, file_path: str):

        self.load(file_path)

        return {
            "role": None,
            "mandatory_skills": [],
            "preferred_skills": [],
            "negative_signals": [],
            "behavior_requirements": [],
            "minimum_experience": None,
            "maximum_experience": None,
            "locations": [],
            "work_mode": None,
        }