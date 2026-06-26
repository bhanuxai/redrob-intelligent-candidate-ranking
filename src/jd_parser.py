"""
JD Parser

Converts a Job Description into structured metadata
used by the ranking engine.
"""

import re
from pathlib import Path
from typing import Dict

from src.utils import clean_text
from src.loader import DocumentLoader


class JDParser:

    def __init__(self):
        self.raw_text = ""
        self.text = ""

    def load(self, file_path):

        self.raw_text = DocumentLoader.load(file_path)

        self.text = clean_text(self.raw_text)

    # --------------------------------------------------

    # --------------------------------------------------

    def extract_role(self):

        patterns = [

            r"job description:\s*(.+)",

            r"role:\s*(.+)",

            r"position:\s*(.+)",

            r"title:\s*(.+)"

        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                self.raw_text,
                flags=re.IGNORECASE
            )

            if match:
                return match.group(1).strip()

        return ""
    # --------------------------------------------------

    def extract_experience(self):

        match = re.search(
            r"experience required:\s*(\d+)\s*(?:-|–|to)\s*(\d+)",
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

        locations = set()

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

                locations.add(city)

        return sorted(locations)

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

    def extract_notice_period(self):

        if "30 days" in self.text:
            return 30

        if "60 days" in self.text:
            return 60

        if "90 days" in self.text:
            return 90

        return None
    
    # --------------------------------------------------

    def extract_company_stage(self):

        stages = [

            "seed",

            "series a",

            "series b",

            "series c"

        ]

        for stage in stages:

            if stage in self.text:

                return stage.title()

        return None
    
    # --------------------------------------------------

    def requires_production_ml(self):

        keywords = [

            "production",

            "deployed",

            "real-world",

            "customers",

            "latency",

            "pipeline"

        ]

        return any(

            word in self.text

            for word in keywords

        )
# --------------------------------------------------

    def requires_product_engineering(self):

        keywords = [

            "product",

            "startup",

            "ship",

            "iterate",

            "ownership",

            "production"

        ]

        return any(

            word in self.text

            for word in keywords

        )
    # --------------------------------------------------

    def extract_mandatory_skills(self):

        skills = [

            "python",

            "embeddings",

            "retrieval",

            "ranking",

            "vector database",
            "vector databases",
            "vector db",
            "vector search",

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
            "learning to rank",

            "xgboost",

            "distributed systems",

            "hr-tech",
            "hr tech",

            "marketplace",

            "open-source"

        ]

        found = []

        for skill in skills:

            if skill in self.text:

                found.append(skill)

        return found

    # --------------------------------------------------

    def extract_disqualifiers(self):

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

            "experience": {
                "minimum": minimum,
                "maximum": maximum
            },

            "preferred_locations": self.extract_locations(),

            "work_mode": self.extract_work_mode(),

            "mandatory_skills": self.extract_mandatory_skills(),

            "preferred_skills": self.extract_preferred_skills(),

            "disqualifiers": self.extract_disqualifiers(),

            "behavior_requirements": self.extract_behavior_requirements(),

            "preferred_notice_days": self.extract_notice_period(),

            "company_stage": self.extract_company_stage(),

            "requires_production_ml": self.requires_production_ml(),

            "requires_product_engineering": self.requires_product_engineering()

        }
    
