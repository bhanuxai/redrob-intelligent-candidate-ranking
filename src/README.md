#  Data & Feature Engineering Pipeline

**👤 Role:** Data & Feature Engineer  
**🙋 Member:** Yendeti Yashashwini

## 📌 Overview
This module handles the complete data preprocessing and feature extraction pipeline for the Redrob Intelligent Candidate Ranking System. It loads 100K+ candidate profiles, cleans the data, extracts meaningful features, and builds a fast-access candidate index.

## 📁 Files

### ⚙️ `preprocess.py`
Loads and cleans raw candidate data from `candidates.jsonl`.
- 🔄 Streams 100K candidates efficiently using a generator
- 🛡️ Handles missing fields with safe defaults
- ⏭️ Skips bad JSON lines without crashing
- 📦 Extracts skills, education, career history, and Redrob signals

### 🧠 `feature_builder.py`
Builds scoring features for each candidate.
- 📅 **Experience Score** — Rewards candidates with 5–9 years of experience
- 🎓 **Education Score** — Scores based on college tier (Tier 1 to Tier 4)
- 💡 **AI Skill Score** — Counts AI-relevant skills with synonym mapping ("dl" = "deep learning")
- 📊 **Behavior Score** — Combines GitHub activity, recruiter response rate, interview completion, offer acceptance, and profile completeness
- 🍯 **Honeypot Score** — Detects and penalizes fake or suspicious profiles
- 🕐 **Career Gap Score** — Handles gaps fairly; legitimate reasons (UPSC, health, family) are not penalized

### 🗂️ `candidate_index.py`
Processes all candidates and saves a fast-access index.
- 🔑 Builds a dictionary of candidate ID → features
- ✅ Skips problematic candidates gracefully
- 💾 Saves output as `candidate_index.pkl`
- ⏱️ Displays total processing time

## 🚀 How to Run
```bash
pip install tqdm
cd src
python candidate_index.py
```

## 📤 Output
```
Loading candidates: 100%|████| 100000/100000 [00:07]
Candidate index saved to data/candidate_index.pkl
Total Candidates: 100000
Time taken: 8.41 seconds
```

## 🛠️ Tech Stack
- 🐍 Python 3.10+
- 📊 tqdm
- 🥒 pickle
- 📂 pathlib