import sys
from pathlib import Path

# Add project root to Python path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.utils import *

print(clean_text("   Hello     World "))
print(safe_divide(10, 2))
print(safe_divide(10, 0))