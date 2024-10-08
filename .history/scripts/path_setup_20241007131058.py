# scripts/path_setup.py
import sys
import scripts

print("Current sys.path after path setup:")
for path in sys.path:
    print(path)
from pathlib import Path

# Determine the project root directory dynamically
project_root = Path(__file__).resolve().parent.parent  # Gets the root folder (CNN_BINARY)

# Add the project root to sys.path if it's not already included
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))
    print(f"Added {project_root} to sys.path")

# Make project_root available for imports in other scripts
print("Project root set to:", project_root)
