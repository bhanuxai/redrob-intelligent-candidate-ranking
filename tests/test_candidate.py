import json

with open("data/raw/candidates.jsonl", "r", encoding="utf-8") as f:

    candidate = json.loads(next(f))

print(candidate)