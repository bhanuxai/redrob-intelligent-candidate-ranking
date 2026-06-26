"""
JD Parser

Converts a Job Description into structured metadata
used by the ranking engine.
"""

import re
from pathlib import Path
from typing import Dict

from src.utils import clean_text


class JDParser:

    def __init__(self):
        self.raw_text = ""
        self.text = ""

    def load(self, file_path):

        self.raw_text = Path(file_path).read_text(
            encoding="utf-8"
        )

        self.text = clean_text(self.raw_text)

    # --------------------------------------------------

    def extract_role(self):

        match = re.search(
            r"job description:\s*(.+)",
            self.raw_text,
            flags=re.IGNORECASE
        )

        if match:
            return match.group(1).strip()

        return ""

    # --------------------------------------------------

    def extract_experience(self):

        match = re.search(
            r"experience required:\s*(\d+)\s*[-–]\s*(\d+)",
            self.text
        )

        if match:

            return (
                int(match.group(1)),
                int(match.group(2))
            )

        return (None, None)

    # --------------------------------------------------

    def extract_locations(self):

        locations = []

        for city in [
            "Pune",
            "Noida",
            "Hyderabad",
            "Mumbai",
            "Delhi NCR",
            "Bangalore",
            "Bengaluru",
            "Chennai"
        ]:

            if city.lower() in self.text:

                locations.append(city)

        return locations

    # --------------------------------------------------

    def extract_work_mode(self):

        for mode in [

            "remote",

            "hybrid",

            "onsite",

            "flexible"

        ]:

            if mode in self.text:

                return mode.title()

        return None

    # --------------------------------------------------

    def extract_mandatory_skills(self):

        skills = [

            "python",

            "embeddings",

            "retrieval",

            "ranking",

            "vector databases",

            "pinecone",

            "weaviate",

            "qdrant",

            "faiss",

            "elasticsearch",

            "opensearch",

            "sentence-transformers",

            "evaluation",

            "ndcg",

            "mrr",

            "map"

        ]

        found = []

        for skill in skills:

            if skill in self.text:

                found.append(skill)

        return found

    # --------------------------------------------------

    def extract_preferred_skills(self):

        skills = [

            "lora",

            "qlora",

            "peft",

            "learning-to-rank",

            "xgboost",

            "distributed systems",

            "hr-tech",

            "marketplace",

            "open-source"

        ]

        found = []

        for skill in skills:

            if skill in self.text:

                found.append(skill)

        return found

    # --------------------------------------------------

    def extract_negative_signals(self):

        negatives = [

            "pure research",

            "academic",

            "langchain",

            "consulting",

            "computer vision",

            "speech",

            "robotics"

        ]

        found = []

        for signal in negatives:

            if signal in self.text:

                found.append(signal)

        return found

    # --------------------------------------------------

    def extract_behavior_requirements(self):

        keywords = [

            "product",

            "ship",

            "production",

            "write",

            "async",

            "mentor",

            "collaborative",

            "fast"

        ]

        found = []

        for word in keywords:

            if word in self.text:

                found.append(word)

        return found

    # --------------------------------------------------

    def parse(self, file_path) -> Dict:

        self.load(file_path)

        minimum, maximum = self.extract_experience()

        return {

            "role": self.extract_role(),

            "minimum_experience": minimum,

            "maximum_experience": maximum,

            "locations": self.extract_locations(),

            "work_mode": self.extract_work_mode(),

            "mandatory_skills": self.extract_mandatory_skills(),

            "preferred_skills": self.extract_preferred_skills(),

            "negative_signals": self.extract_negative_signals(),

            "behavior_requirements": self.extract_behavior_requirements(),

        }