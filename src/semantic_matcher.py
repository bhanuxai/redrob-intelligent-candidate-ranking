"""
Semantic Matcher

Measures conceptual similarity between a candidate profile
and the job description using lightweight keyword groups.
"""

from __future__ import annotations

from typing import Dict, List

from src.utils import clean_text


class SemanticMatcher:

    def __init__(self):

        self.semantic_groups = {

            "retrieval": {
                "retrieval",
                "search",
                "information retrieval",
                "hybrid search",
                "semantic search",
                "vector search",
                "dense retrieval",
                "bm25",
            },

            "ranking": {
                "ranking",
                "reranking",
                "recommendation",
                "recommendation system",
                "matching",
                "candidate ranking",
                "learning to rank",
            },

            "embeddings": {
                "embedding",
                "embeddings",
                "sentence-transformers",
                "bge",
                "e5",
                "openai embeddings",
            },

            "vector_db": {
                "pinecone",
                "faiss",
                "milvus",
                "weaviate",
                "qdrant",
                "elasticsearch",
                "opensearch",
            },

            "llm": {
                "llm",
                "transformer",
                "rag",
                "fine tuning",
                "lora",
                "qlora",
                "peft",
                "prompt engineering",
            },

            "production": {
                "production",
                "deployed",
                "architecture",
                "pipeline",
                "real time",
                "scalable",
                "latency",
                "monitoring",
            }

        }

    # --------------------------------------------------

    def collect_text(
        self,
        candidate: Dict
    ) -> str:

        sections: List[str] = []

        profile = candidate["profile"]

        sections.append(profile.get("headline", ""))

        sections.append(profile.get("summary", ""))

        sections.append(profile.get("current_title", ""))

        for job in candidate["career_history"]:

            sections.append(job.get("title", ""))

            sections.append(job.get("description", ""))

        for skill in candidate["skills"]:

            sections.append(skill.get("name", ""))

        return clean_text("\n".join(sections))

    # --------------------------------------------------

    def score(
        self,
        candidate: Dict
    ) -> float:

        text = self.collect_text(candidate)

        matched_groups = 0

        for keywords in self.semantic_groups.values():

            if any(
                keyword in text
                for keyword in keywords
            ):
                matched_groups += 1

        return round(
            matched_groups /
            len(self.semantic_groups),
            4
        )