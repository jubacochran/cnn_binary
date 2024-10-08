import os
from pathlib import Path


def project_root():
    current_dir = Path(os.getcwd())  
    # Find the project root directory named 'cnn_binary'
    project_root = next(p for p in current_dir.resolve().parents if p.name == "cnn_binary")
    os.chdir(project_root) 
    print("Current Working Directory: ", os.getcwd())
    return project_root
