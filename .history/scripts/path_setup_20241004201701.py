import sys
from pathlib import Path

# Determine the project root directory based on the current working directory (cwd)
# Modify this path strategy as necessary for your setup.
current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent

# Add the project root to `sys.path` to ensure it is available globally
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

# Print for confirmation
print(f"Project root set to: {project_root}")
print(f"Current sys.path:\n{sys.path[:5]}")
