from pathlib import Path
import os

def make_paths_relative_to_root():
    """
    Always use the same, absolute (relative to root) paths
    which makes moving the notebooks around easier.
    """
    # Set the project root directory based on this script's location
    top_level = Path(__file__).parent.parent

    # Change the current working directory to the root of the project
    os.chdir(top_level)

    print(f"Project root set to: {top_level}")

