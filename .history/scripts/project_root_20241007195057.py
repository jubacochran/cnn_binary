import os
from pathlib import Path

# Function to locate and set project root
def project_root():
    current_dir = Path(os.getcwd())  # Move `current_dir` inside the function
    # Find the project root directory named 'cnn_binary'
    project_root = next(p for p in current_dir.resolve().parents if p.name == "cnn_binary")
    os.chdir(project_root)  # Change directory to the project root
    print("Current Working Directory: ", os.getcwd())
    return project_root
