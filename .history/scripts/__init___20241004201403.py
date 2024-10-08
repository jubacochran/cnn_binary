# Create an empty __init__.py file in the scripts directory
open('scripts/__init__.py', 'w').close()

# Verify that the file was created
import os
print("__init__.py created:", os.path.isfile('scripts/__init__.py'))
