"""
JD Understanding Engine

Converts raw JD text into structured information.
"""

import re

from src.loader import DocumentLoader


class JDUnderstanding:

    def __init__(self):
        self.text = ""

    def load(self, file_path):

        self.text = DocumentLoader.load(file_path)

    # -------------------------------------------------

    def extract_role(self):

        match = re.search(
            r"Job Description:\s*(.+)",
            self.text,
            flags=re.IGNORECASE,
        )

        if match:
            return match.group(1).strip()

        return ""

    # -------------------------------------------------

    def extract_experience(self):

        match = re.search(
            r"Experience Required:\s*(\d+)\s*[–-]\s*(\d+)",
            self.text,
            flags=re.IGNORECASE,
        )

        if match:
            return (
                int(match.group(1)),
                int(match.group(2))
            )

        return (None, None)

    # -------------------------------------------------

    def extract_work_mode(self):

        text = self.text.lower()

        if "hybrid" in text:
            return "Hybrid"

        if "remote" in text:
            return "Remote"

        if "onsite" in text:
            return "Onsite"

        return None

    # -------------------------------------------------

    def extract_locations(self):

        cities = [
            "Pune",
            "Noida",
            "Hyderabad",
            "Mumbai",
            "Delhi NCR",
            "Bangalore",
            "Bengaluru",
            "Chennai",
        ]

        found = []

        for city in cities:

            if city.lower() in self.text.lower():
                found.append(city)

        return found

    # -------------------------------------------------

    def understand(self, file_path):

        self.load(file_path)

        exp_min, exp_max = self.extract_experience()

        return {

            "role": self.extract_role(),

            "experience": {
                "minimum": exp_min,
                "maximum": exp_max,
            },

            "locations": self.extract_locations(),

            "work_mode": self.extract_work_mode(),

        }