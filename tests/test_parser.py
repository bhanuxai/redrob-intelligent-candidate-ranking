import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.jd_parser import JDParser
from src.config import JOB_DESCRIPTION_PATH

parser = JDParser()

result = parser.parse(JOB_DESCRIPTION_PATH)

print()

for key, value in result.items():

    print(f"{key}: {value}")