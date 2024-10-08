from pathlib import Path
import os

def make_paths_relative_to_root():
    """
    Set the project root directory and return its path.
    """
    # Set the project root to the parent of this script's location
    top_level = Path(__file__).resolve().parent.parent

    # Change the current working directory to the root of the project
    os.chdir(top_level)

    print(f"Project root set to: {top_level}")
    return top_level


