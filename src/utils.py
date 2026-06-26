"""
Utility functions for the Redrob Candidate Ranking System.
"""

import re
from datetime import datetime
from typing import List


def clean_text(text: str) -> str:
    """
    Lowercase, remove extra spaces.
    """

    if text is None:
        return ""

    text = text.lower()

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def normalize_skill(skill: str) -> str:
    """
    Normalize skill names.
    """

    return clean_text(skill)


def safe_divide(a: float, b: float) -> float:
    """
    Division without ZeroDivisionError.
    """

    if b == 0:
        return 0.0

    return a / b


def years_between(start_year: int, end_year: int) -> int:
    """
    Difference between two years.
    """

    return max(0, end_year - start_year)


def months_between(start_date: str, end_date: str | None) -> int:
    """
    Returns number of months between dates.
    """

    start = datetime.strptime(start_date, "%Y-%m-%d")

    if end_date is None:
        end = datetime.today()

    else:
        end = datetime.strptime(end_date, "%Y-%m-%d")

    months = (end.year - start.year) * 12

    months += end.month - start.month

    return max(0, months)


def average(values: List[float]) -> float:

    if len(values) == 0:
        return 0.0

    return sum(values) / len(values)


def clamp(value: float,
          minimum: float,
          maximum: float):

    return max(minimum, min(value, maximum))


def normalize_score(score: float,
                    maximum: float):

    if maximum == 0:
        return 0.0

    return score / maximum


def bool_to_score(flag: bool):

    return 1.0 if flag else 0.0