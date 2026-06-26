import sys
from pathlib import Path
import json

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

from src.behavior import BehaviorScorer

with open(
    "data/raw/candidates.jsonl",
    encoding="utf-8"
) as f:
    candidate = json.loads(next(f))

scorer = BehaviorScorer()

print()

print(
    scorer.score(candidate)
)