import json
from pathlib import Path
from tqdm import tqdm

AI_KEYWORDS = {
    "llm",
    "llms",
    "fine-tuning",
    "lora",
    "nlp",
    "transformers",
    "embedding",
    "embeddings",
    "rag",
    "retrieval",
    "ranking",
    "vector",
    "faiss",
    "pinecone",
    "qdrant",
    "milvus",
    "weaviate",
    "machine learning",
    "deep learning",
    "computer vision",
    "speech recognition",
    "tts",
    "asr"
}

DATA_FILE = Path(__file__).parent.parent / "data" / "candidates.jsonl"

def load_candidates(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    skipped = 0
    for line in tqdm(lines, desc="Loading candidates"):
        try:
            yield json.loads(line)
        except json.JSONDecodeError:
            skipped += 1
            continue
    if skipped > 0:
        print(f"Skipped {skipped} bad lines")

def clean_candidate(candidate):
    candidate.setdefault("skills", [])
    candidate.setdefault("education", [])
    candidate.setdefault("career_history", [])
    candidate.setdefault("certifications", [])
    candidate.setdefault("languages", [])
    candidate.setdefault("redrob_signals", {})
    return candidate

def get_years_of_experience(candidate):
    profile = candidate.get("profile", {})
    years = profile.get("years_of_experience", 0)
    if years is None:
        return 0.0
    return float(years)

def get_skill_names(candidate):
    skills = candidate.get("skills", [])
    skill_names = []
    for skill in skills:
        name = skill.get("name")
        if name:
            skill_names.append(name.lower())
    return skill_names

def count_ai_skills(skill_names):
    count = 0
    for skill in skill_names:
        skill = skill.lower()
        for keyword in AI_KEYWORDS:
            if keyword in skill:
                count += 1
                break
    return count

def get_career_history(candidate):
    return candidate.get("career_history", [])

def get_total_career_months(candidate):
    jobs = get_career_history(candidate)
    total_months = 0
    for job in jobs:
        total_months += job.get("duration_months", 0)
    return total_months

def experience_consistency(candidate):
    profile_years = get_years_of_experience(candidate)
    career_years = (get_total_career_months(candidate) / 12)
    difference = abs(profile_years - career_years)
    return difference

def is_experience_suspicious(candidate):
    difference = experience_consistency(candidate)
    if difference > 3:
        return True
    return False

def get_best_education_tier(candidate):
    education = candidate.get("education", [])
    if not education:
        return "unknown"
    tiers = []
    for edu in education:
        tier = edu.get("tier")
        if tier:
            tiers.append(tier.lower())
    if not tiers:
        return "unknown"
    priority = ["tier_1", "tier_2", "tier_3", "tier_4"]
    for tier in priority:
        if tier in tiers:
            return tier
    return "unknown"

def get_redrob_signals(candidate):
    return candidate.get("redrob_signals", {})

def get_signal(candidate, signal_name, default=None):
    signals = get_redrob_signals(candidate)
    return signals.get(signal_name, default)

if __name__ == "__main__":
    for candidate in load_candidates(DATA_FILE):
        pass