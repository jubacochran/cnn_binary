import os
from pathlib import Path
current_dir = Path(os.getcwd())


#print(project_root)
project_root = next(p for p in current_dir.resolve().parents if p.name == "cnn_binary")
os.chdir(project_root)
print("Current Working Directory: ", os.getcwd())