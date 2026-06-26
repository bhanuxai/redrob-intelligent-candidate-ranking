import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.loader import DocumentLoader
from src.config import RAW_DATA_DIR

jd = RAW_DATA_DIR / "job_description.docx"

text = DocumentLoader.load(jd)

print(text[:500])