import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.jd_parser import JDParser
from src.jd_understanding import JDUnderstanding
from src.config import JOB_DESCRIPTION_PATH

parser = JDParser()

parsed_jd = parser.parse(JOB_DESCRIPTION_PATH)

understanding = JDUnderstanding(parsed_jd)

requirements = understanding.get_requirements()

print(requirements)