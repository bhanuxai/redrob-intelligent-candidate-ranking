"""
Utility functions used across the project.
"""

import re


def clean_text(text: str) -> str:
    """
    Lowercase and remove unnecessary spaces.
    """
    if not text:
        return ""

    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def normalize_skill(skill: str) -> str:
    """
    Normalize skill names.
    """
    return clean_text(skill)


def safe_divide(a, b):
    """
    Prevent division by zero.
    """
    if b == 0:
        return 0

    return a / b