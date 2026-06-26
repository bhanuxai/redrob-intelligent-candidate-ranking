import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.scoring_schema import CandidateFeatures

candidate = CandidateFeatures(
    candidate_id="CAND_0000001"
)

print(candidate)