import sys
from pathlib import Path
import json

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

from src.semantic_matcher import SemanticMatcher

with open(
    "data/raw/candidates.jsonl",
    encoding="utf-8"
) as f:

    candidate = json.loads(next(f))

matcher = SemanticMatcher()

print()

print(
    matcher.score(candidate)
)