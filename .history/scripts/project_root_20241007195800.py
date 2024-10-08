import os
from pathlib import Path


import os
import sys
from pathlib import Path

def project_root():
    # Locate the root directory of the project (cnn_binary)
    current_dir = Path(os.getcwd())
    root_dir = next(p for p in current_dir.resolve().parents if p.name == "CNN_BINARY")
    
    # Change the current working directory to the project root
    os.chdir(root_dir)
    print(f"Current Working Directory Set to: {os.getcwd()}")

    # Add the root directory to `sys.path` for module imports
    if str(root_dir) not in sys.path:
        sys.path.insert(0, str(root_dir))
        print(f"Added {root_dir} to sys.path")

    return root_dir

# Automatically set up project root and `sys.path` when the module is imported
project_root()
