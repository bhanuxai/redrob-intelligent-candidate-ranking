from preprocess import (
    load_candidates,
    clean_candidate,
    DATA_FILE,
    get_years_of_experience,
    get_skill_names,
    count_ai_skills,
    get_best_education_tier,
    get_signal,
    is_experience_suspicious
)

SKILL_SYNONYMS = {
    "deep learning": ["dl", "deep-learning", "neural networks", "nn", "dnn"],
    "machine learning": ["ml", "machine-learning"],
    "natural language processing": ["nlp", "natural-language-processing"],
    "large language models": ["llm", "llms", "large language model"],
    "retrieval augmented generation": ["rag"],
    "fine tuning": ["fine-tuning", "finetuning", "lora", "qlora"],
    "computer vision": ["cv", "image recognition", "image classification"],
    "speech recognition": ["asr", "speech-to-text", "stt"],
    "text to speech": ["tts", "speech synthesis"],
    "vector database": ["vector db", "faiss", "pinecone", "qdrant", "milvus", "weaviate"],
    "transformers": ["bert", "gpt", "attention mechanism"],
}

def normalize_skill(skill):
    skill = skill.lower().strip()
    for canonical, synonyms in SKILL_SYNONYMS.items():
        if skill in synonyms or skill == canonical:
            return canonical
    return skill

def experience_score(candidate):
    years = get_years_of_experience(candidate)
    if 5 <= years <= 9:
        return 1.0
    elif 3 <= years < 5:
        return 0.8
    elif 10 <= years <= 12:
        return 0.7
    elif years > 12:
        return 0.5
    else:
        return 0.3
    
def education_score(candidate):
    tier = get_best_education_tier(candidate)
    if tier == "tier_1":
        return 1.0
    elif tier == "tier_2":
        return 0.8
    elif tier == "tier_3":
        return 0.6
    elif tier == "tier_4":
        return 0.4
    return 0.2

def career_gap_score(candidate):
    career_history = candidate.get("career_history", [])
    if not career_history:
        return 0.5
    legitimate_reasons = [
        "upsc", "family", "health", "higher education",
        "maternity", "study", "personal", "sabbatical"
    ]
    total_gap_months = 0
    for job in career_history:
        gap = job.get("gap_after_months", 0) or 0
        reason = job.get("gap_reason", "").lower()
        if any(r in reason for r in legitimate_reasons):
            continue
        total_gap_months += gap
    if total_gap_months == 0:
        return 1.0
    elif total_gap_months <= 3:
        return 0.9
    elif total_gap_months <= 6:
        return 0.8
    elif total_gap_months <= 12:
        return 0.7
    else:
        return 0.5

def ai_skill_score(candidate):
    skills = get_skill_names(candidate)
    normalized_skills = [normalize_skill(s) for s in skills]
    ai_count = count_ai_skills(normalized_skills)
    if ai_count >= 10:
        return 1.0
    elif ai_count >= 8:
        return 0.9
    elif ai_count >= 6:
        return 0.8
    elif ai_count >= 4:
        return 0.6
    elif ai_count >= 2:
        return 0.4
    return 0.2

def behavior_score(candidate):
    github = get_signal(candidate, "github_activity_score", -1)
    response_rate = get_signal(candidate, "recruiter_response_rate", 0)
    interview_rate = get_signal(candidate, "interview_completion_rate", 0)
    offer_rate = get_signal(candidate, "offer_acceptance_rate", -1)
    profile_score = get_signal(candidate, "profile_completeness_score", 0)
    github = 0 if github == -1 else github / 100
    offer_rate = 0 if offer_rate == -1 else offer_rate
    profile_score = profile_score / 100
    score = (github * 0.20 + response_rate * 0.25 + interview_rate * 0.25 + offer_rate * 0.15 + profile_score * 0.15)
    return round(score, 3)

def honeypot_score(candidate):
    score = 1.0
    if is_experience_suspicious(candidate):
        score -= 0.5
    github = get_signal(candidate, "github_activity_score", -1)
    if github == -1:
        score -= 0.2
    profile = get_signal(candidate, "profile_completeness_score", 0)
    if profile < 40:
        score -= 0.2
    return max(score, 0.0)

def build_features(candidate):
    return {
        "candidate_id": candidate["candidate_id"],
        "experience_score": experience_score(candidate),
        "education_score": education_score(candidate),
        "ai_skill_score": ai_skill_score(candidate),
        "behavior_score": behavior_score(candidate),
        "honeypot_score": honeypot_score(candidate),
        "career_gap_score": career_gap_score(candidate),  # ← new!
        "years_of_experience": get_years_of_experience(candidate),
        "education_tier": get_best_education_tier(candidate),
        "skills": get_skill_names(candidate)
    }

if __name__ == "__main__":
    for candidate in load_candidates(DATA_FILE):
        candidate = clean_candidate(candidate)
        features = build_features(candidate)
        print(features)
        break