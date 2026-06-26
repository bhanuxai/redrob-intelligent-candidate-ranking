import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.jd_understanding import JDUnderstanding
from src.config import RAW_DATA_DIR

jd = RAW_DATA_DIR / "job_description.docx"

engine = JDUnderstanding()

result = engine.understand(jd)

print(result)