# """
# Evidence Based Candidate Scorer
# --------------------------------

# This scorer ranks candidates based on evidence,
# not keyword stuffing.

# Author: Team Redrob
# """

# from __future__ import annotations

# from typing import Dict, List

# from src.utils import clean_text


# class CandidateScorer:

#     def __init__(self, jd: Dict):

#         self.jd = jd

#         # -----------------------------
#         # Strong AI Evidence
#         # -----------------------------

#         self.ai_keywords = {

#             "embedding",
#             "embeddings",
#             "retrieval",
#             "ranking",
#             "recommendation",
#             "vector",
#             "vector database",
#             "faiss",
#             "pinecone",
#             "qdrant",
#             "milvus",
#             "weaviate",
#             "rag",
#             "semantic search",
#             "hybrid search",
#             "sentence-transformers",
#             "llm",
#             "transformer",
#             "evaluation",
#             "ndcg",
#             "mrr",
#             "map",

#         }

#         # -----------------------------
#         # Product Engineering Evidence
#         # -----------------------------

#         self.product_keywords = {

#             "production",
#             "deployed",
#             "designed",
#             "implemented",
#             "scaled",
#             "optimized",
#             "architecture",
#             "real-time",
#             "pipeline",
#             "latency",
#             "users",
#             "customer",

#         }

#         # -----------------------------
#         # Weak / Negative Evidence
#         # -----------------------------

#         self.negative_keywords = {

#             "learning",

#             "beginner",

#             "transitioning",

#             "interested in",

#             "exploring",

#             "academic",

#             "research only",

#             "intern",

#         }

#     # =====================================================
#     # Utility Functions
#     # =====================================================

#     def keyword_score(
#         self,
#         text: str,
#         keywords: set
#     ) -> float:

#         text = clean_text(text)

#         if not keywords:
#             return 0.0

#         matches = 0

#         for keyword in keywords:

#             if keyword in text:

#                 matches += 1

#         return matches / len(keywords)

#     # -----------------------------------------------------

#     def collect_candidate_text(
#         self,
#         candidate: Dict
#     ) -> str:

#         sections: List[str] = []

#         profile = candidate["profile"]

#         sections.append(
#             profile.get("headline", "")
#         )

#         sections.append(
#             profile.get("summary", "")
#         )

#         sections.append(
#             profile.get("current_title", "")
#         )

#         for job in candidate["career_history"]:

#             sections.append(
#                 job.get("title", "")
#             )

#             sections.append(
#                 job.get("description", "")
#             )

#         for skill in candidate["skills"]:

#             sections.append(
#                 skill.get("name", "")
#             )

#         return "\n".join(sections)
    
#         # =====================================================
#     # Technical Evidence Scoring
#     # =====================================================

#     def score_career_evidence(
#         self,
#         candidate: Dict
#     ) -> float:
#         """
#         Score based on real production work
#         mentioned in career history.
#         """

#         descriptions = []

#         for job in candidate["career_history"]:
#             descriptions.append(
#                 job.get("description", "")
#             )

#         text = "\n".join(descriptions)

#         ai_score = self.keyword_score(
#             text,
#             self.ai_keywords
#         )

#         product_score = self.keyword_score(
#             text,
#             self.product_keywords
#         )

#         return round(
#             (0.7 * ai_score) +
#             (0.3 * product_score),
#             4
#         )

#     # -----------------------------------------------------

#     def score_summary(
#         self,
#         candidate: Dict
#     ) -> float:
#         """
#         Penalize candidates who are
#         'learning' or 'transitioning'
#         into AI.
#         """

#         summary = candidate["profile"].get(
#             "summary",
#             ""
#         )

#         positive = self.keyword_score(
#             summary,
#             self.ai_keywords
#         )

#         negative = self.keyword_score(
#             summary,
#             self.negative_keywords
#         )

#         score = positive - negative

#         return round(
#             max(score, 0),
#             4
#         )

#     # -----------------------------------------------------

#     def score_current_title(
#         self,
#         candidate: Dict
#     ) -> float:

#         title = candidate["profile"].get(
#             "current_title",
#             ""
#         ).lower()

#         strong_titles = [

#             "ai engineer",

#             "machine learning engineer",

#             "ml engineer",

#             "nlp engineer",

#             "search engineer",

#             "ranking engineer",

#             "recommendation engineer",

#         ]

#         adjacent_titles = [

#             "backend engineer",

#             "software engineer",

#             "data engineer",

#             "analytics engineer",

#             "platform engineer",

#         ]

#         weak_titles = [

#             "marketing",

#             "sales",

#             "graphic designer",

#             "content writer",

#             "hr",

#             "accountant",

#             "customer support",

#         ]

#         for t in strong_titles:

#             if t in title:
#                 return 1.0

#         for t in adjacent_titles:

#             if t in title:
#                 return 0.60

#         for t in weak_titles:

#             if t in title:
#                 return 0.10

#         return 0.30

#     # -----------------------------------------------------

#     def score_experience(
#         self,
#         candidate: Dict
#     ) -> float:

#         years = candidate["profile"].get(
#             "years_of_experience",
#             0
#         )

#         minimum = self.jd["experience"]["minimum"]
#         maximum = self.jd["experience"]["maximum"]

#         if minimum <= years <= maximum:
#             return 1.0

#         if years < minimum:

#             gap = minimum - years

#             return max(
#                 0,
#                 1 - gap * 0.20
#             )

#         extra = years - maximum

#         return max(
#             0.60,
#             1 - extra * 0.03
#         )
#         # =====================================================
#     # Skills
#     # =====================================================

#     # def score_candidate(self, candidate):

#     # career = self.score_career_evidence(candidate)
#     # summary = self.score_summary(candidate)
#     # title = self.score_current_title(candidate)
#     # experience = self.score_experience(candidate)
#     # skills = self.score_skills(candidate)

#     # behaviour = self.score_behavior(candidate)
#     # recruiter = self.score_recruiter_signals(candidate)
#     # risk = self.score_risk(candidate)

#     # technical = (
#     #     career * 0.35 +
#     #     summary * 0.10 +
#     #     title * 0.15 +
#     #     experience * 0.20 +
#     #     skills * 0.20
#     # )

#     # business = (
#     #     behaviour * 0.70 +
#     #     recruiter * 0.30
#     # )

#     # final = (
#     #     technical * 0.75 +
#     #     business * 0.25
#     # )

#     # final = max(0, final - risk)

#     # return {
#     #     "career": round(career, 4),
#     #     "summary": round(summary, 4),
#     #     "title": round(title, 4),
#     #     "experience": round(experience, 4),
#     #     "skills": round(skills, 4),
#     #     "behaviour": round(behaviour, 4),
#     #     "recruiter": round(recruiter, 4),
#     #     "risk": round(risk, 4),
#     #     "technical_score": round(technical, 4),
#     #     "business_score": round(business, 4),
#     #     "final_score": round(final, 4)
#     # }

#     # =====================================================
#     # Behaviour
#     # =====================================================

#     def score_behavior(self, candidate: Dict) -> float:

#         signals = candidate["redrob_signals"]

#         score = 0

#         score += (
#             signals["recruiter_response_rate"]
#             * 0.30
#         )

#         score += (
#             signals["interview_completion_rate"]
#             * 0.25
#         )

#         score += (
#             signals["github_activity_score"] / 100
#             * 0.15
#         )

#         score += (
#             signals["profile_completeness_score"] / 100
#             * 0.15
#         )

#         score += (
#             0.15
#             if signals["open_to_work_flag"]
#             else 0
#         )

#         return round(min(score, 1.0), 4)

#     # =====================================================
#     # Recruiter Signals
#     # =====================================================

#     def score_recruiter_signals(
#         self,
#         candidate: Dict
#     ) -> float:

#         s = candidate["redrob_signals"]

#         score = 0

#         score += min(
#             s["saved_by_recruiters_30d"] / 25,
#             1
#         ) * 0.40

#         score += min(
#             s["search_appearance_30d"] / 500,
#             1
#         ) * 0.30

#         score += min(
#             s["profile_views_received_30d"] / 100,
#             1
#         ) * 0.30

#         return round(score, 4)

#     # =====================================================
#     # Risk
#     # =====================================================

#     def score_risk(
#         self,
#         candidate: Dict
#     ) -> float:

#         penalty = 0

#         profile = candidate["profile"]
#         signals = candidate["redrob_signals"]

#         title = profile[
#             "current_title"
#         ].lower()

#         weak_titles = [

#             "marketing",

#             "sales",

#             "graphic",

#             "writer",

#             "accountant",

#             "hr",

#             "customer support",

#         ]

#         if any(
#             t in title
#             for t in weak_titles
#         ):
#             penalty += 0.30

#         if not signals[
#             "willing_to_relocate"
#         ]:
#             penalty += 0.10

#         if (
#             signals[
#                 "notice_period_days"
#             ] > 90
#         ):
#             penalty += 0.10

#         return round(
#             min(penalty, 1),
#             4
#         )
#         # =====================================================
#     # Final Score
#     # =====================================================

#     def score_candidate(
#         self,
#         candidate: Dict
#     ) -> Dict:

#         career = self.score_career_evidence(candidate)
#         summary = self.score_summary(candidate)
#         title = self.score_current_title(candidate)
#         experience = self.score_experience(candidate)
#         skills = self.score_skills(candidate)

#         behaviour = self.score_behavior(candidate)
#         recruiter = self.score_recruiter_signals(candidate)
#         risk = self.score_risk(candidate)

#         technical = (
#             career * 0.35 +
#             summary * 0.10 +
#             title * 0.15 +
#             experience * 0.20 +
#             skills * 0.20
#         )

#         business = (
#             behaviour * 0.70 +
#             recruiter * 0.30
#         )

#         final = (
#             technical * 0.75 +
#             business * 0.25
#         )

#         final = max(
#             0,
#             final - risk
#         )

#         return {

#             "career": round(career, 4),

#             "summary": round(summary, 4),

#             "title": round(title, 4),

#             "experience": round(experience, 4),

#             "skills": round(skills, 4),

#             "behaviour": round(behaviour, 4),

#             "recruiter": round(recruiter, 4),

#             "risk": round(risk, 4),

#             "technical_score": round(technical, 4),

#             "business_score": round(business, 4),

#             "final_score": round(final, 4)

#         }

"""
Evidence Based Candidate Scorer
Redrob Hackathon
"""

from __future__ import annotations

from typing import Dict, List

from src.utils import clean_text


class CandidateScorer:
    """
    Evidence-based scorer.

    This class scores candidates based on:
    - Career evidence
    - Skills
    - Behaviour
    - Recruiter signals
    - Risk factors
    """

    def __init__(self, jd: Dict):

        self.jd = jd

        # AI / ML evidence keywords
        self.ai_keywords = {
            "embedding",
            "embeddings",
            "retrieval",
            "ranking",
            "recommendation",
            "recommendation system",
            "vector",
            "vector database",
            "pinecone",
            "milvus",
            "qdrant",
            "faiss",
            "weaviate",
            "rag",
            "llm",
            "transformer",
            "sentence-transformers",
            "semantic search",
            "hybrid search",
            "evaluation",
            "ndcg",
            "mrr",
            "map",
        }

        # Product engineering keywords
        self.product_keywords = {
            "production",
            "deployed",
            "implemented",
            "built",
            "designed",
            "optimized",
            "scaled",
            "pipeline",
            "architecture",
            "real-time",
            "customer",
            "users",
        }

        # Negative evidence
        self.negative_keywords = {
            "learning",
            "transitioning",
            "interested in",
            "exploring",
            "academic",
            "research only",
            "intern",
            "beginner",
        }

    # =====================================================
    # Utility Methods
    # =====================================================

    def keyword_score(
        self,
        text: str,
        keywords: set
    ) -> float:

        text = clean_text(text)

        if not keywords:
            return 0.0

        matches = 0

        for keyword in keywords:
            if keyword in text:
                matches += 1

        return matches / len(keywords)

    # -----------------------------------------------------

    def collect_candidate_text(
        self,
        candidate: Dict
    ) -> str:

        parts: List[str] = []

        profile = candidate["profile"]

        parts.append(profile.get("headline", ""))
        parts.append(profile.get("summary", ""))
        parts.append(profile.get("current_title", ""))

        for job in candidate.get("career_history", []):

            parts.append(job.get("title", ""))
            parts.append(job.get("description", ""))

        for skill in candidate.get("skills", []):

            parts.append(skill.get("name", ""))

        return "\n".join(parts)
    
        # =====================================================
    # Technical Scoring
    # =====================================================

    def score_title(self, candidate: Dict) -> float:

        title = candidate["profile"].get(
            "current_title",
            ""
        ).lower()

        strong_titles = {
            "ai engineer",
            "machine learning engineer",
            "ml engineer",
            "nlp engineer",
            "search engineer",
            "ranking engineer",
            "recommendation engineer",
            "data scientist"
        }

        adjacent_titles = {
            "backend engineer",
            "software engineer",
            "data engineer",
            "analytics engineer",
            "platform engineer"
        }

        for t in strong_titles:
            if t in title:
                return 1.0

        for t in adjacent_titles:
            if t in title:
                return 0.6

        return 0.2

    # -----------------------------------------------------

    def score_summary(self, candidate: Dict) -> float:

        summary = candidate["profile"].get("summary", "")

        positive = self.keyword_score(
            summary,
            self.ai_keywords
        )

        negative = self.keyword_score(
            summary,
            self.negative_keywords
        )

        return max(0.0, positive - negative)

    # -----------------------------------------------------

    def score_experience(self, candidate: Dict) -> float:

        years = candidate["profile"].get(
            "years_of_experience",
            0
        )

        experience = self.jd.get(
            "experience",
            {}
        )

        minimum = experience.get("minimum", 0)
        maximum = experience.get("maximum", 50)

        if minimum <= years <= maximum:
            return 1.0

        if years < minimum:

            return max(
                0,
                1 - ((minimum - years) * 0.20)
            )

        return max(
            0.60,
            1 - ((years - maximum) * 0.03)
        )

    # -----------------------------------------------------

    def score_career(self, candidate: Dict) -> float:

        descriptions = []

        for job in candidate.get(
            "career_history",
            []
        ):
            descriptions.append(
                job.get("description", "")
            )

        text = "\n".join(descriptions)

        ai = self.keyword_score(
            text,
            self.ai_keywords
        )

        product = self.keyword_score(
            text,
            self.product_keywords
        )

        return (
            ai * 0.70 +
            product * 0.30
        )

    # -----------------------------------------------------

    def score_skills(self, candidate: Dict) -> float:

        skills = candidate.get(
            "skills",
            []
        )

        if not skills:
            return 0

        matched = 0

        for skill in skills:

            name = clean_text(
                skill["name"]
            )

            for keyword in self.ai_keywords:

                if keyword in name:
                    matched += 1
                    break

        return min(
            matched / len(skills),
            1.0
        )