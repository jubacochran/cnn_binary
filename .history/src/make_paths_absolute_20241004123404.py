from os import chdir
from pathlib import Path

def make_paths_relative_to_root():
    """Always use the same, absolute (relative to root) paths

    which makes moving the notebooks around easier.
    """
    # Set the root to the top-level directory of your project
    top_level = Path(__file__).parent.parent

    # Change the current working directory to the project root
    chdir(top_level)

make_paths_relative_to_root()