"""
Document Loader

Loads DOCX or TXT files and returns plain text.
"""

from pathlib import Path
from docx import Document


class DocumentLoader:

    @staticmethod
    def load(file_path):

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(path)

        suffix = path.suffix.lower()

        if suffix == ".txt":
            return path.read_text(
                encoding="utf-8"
            )

        if suffix == ".docx":

            document = Document(path)

            paragraphs = [
                p.text
                for p in document.paragraphs
                if p.text.strip()
            ]

            return "\n".join(paragraphs)

        raise ValueError(
            f"Unsupported file type: {suffix}"
        )