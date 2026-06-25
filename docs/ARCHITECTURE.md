# Redrob Intelligent Candidate Ranking System

## Overview

The system ranks candidates for a given Job Description using a hybrid AI pipeline that combines semantic matching, structured feature engineering, behavioral signals, and explainable scoring.

---

# System Pipeline

Job Description
        │
        ▼
JD Parser
        │
        ▼
Structured Job Profile
        │
        ▼
Candidate Feature Builder
        │
        ▼
Embedding Engine
        │
        ▼
Weighted Scoring Engine
        │
        ▼
Candidate Ranker
        │
        ▼
Explanation Generator
        │
        ▼
submission.csv

---

# Module Responsibilities

## preprocess.py

- Load candidate dataset
- Clean missing values
- Normalize text
- Prepare candidate objects

---

## feature_builder.py

Extract structured candidate features.

Examples:

- Career Gap
- Career Progression
- Skill Synonyms
- College Tier
- Honeypot Signals

---

## embedding_engine.py

Generate semantic embeddings for:

- Job Description
- Candidate Profile

Compute semantic similarity.

---

## jd_parser.py

Convert Job Description into structured information.

Extract:

- Role
- Experience
- Mandatory Skills
- Preferred Skills
- Negative Signals
- Behaviour Requirements
- Location
- Work Mode

---

## scorer.py

Calculate candidate score using multiple components.

Technical Score

- Semantic Similarity
- Skills
- Experience
- Career
- Education

Behaviour Score

- Response Rate
- Interview Completion
- Last Active
- Open To Work
- GitHub Activity
- Notice Period

Penalty

- Role mismatch
- Inactive profile
- Long notice period
- Negative JD signals

---

## ranker.py

- Sort candidates
- Generate Top 100
- Assign ranks
- Export ranking

---

## explanation_engine.py

Generate human-readable reasoning using candidate profile facts.

---

# Final Scoring Formula

Final Score

=

Technical Score

+

Behaviour Score

-

Risk Penalty

---

# Design Principles

- Explainable
- Deterministic
- CPU Efficient
- Offline
- Modular
- Reproducible