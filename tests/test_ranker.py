import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

from src.ranker import CandidateRanker

jd = {

    "experience": {

        "minimum": 5,

        "maximum": 9

    }

}

ranker = CandidateRanker(jd)

top = ranker.rank_candidates(

    "data/raw/candidates.jsonl",

    top_k=5

)

print()

for row in top:

    print(row)