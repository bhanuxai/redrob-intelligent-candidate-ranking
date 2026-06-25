import re
from pathlib import Path

import spacy
from rapidfuzz import process

from config import VALID_DEGREES

class JDParser:
    """
    Parses Job Description into structured information.
    """

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def load_jd(self):
        pass

    def clean_text(self):
        pass

    def extract_skills(self):
        pass

    def extract_experience(self):
        pass

    def extract_education(self):
        pass

    def extract_location(self):
        pass

    def extract_work_mode(self):
        pass

    def parse(self):
        pass