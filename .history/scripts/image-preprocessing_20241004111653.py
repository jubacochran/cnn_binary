import json
import shutil
import os
from pathlib import Path

# Optional: Use python-dotenv to load environment variables from a .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Resolve the root directory dynamically based on the script's location
project_root = Path(__file__).resolve().parent.parent  # Adjust as per the script location in your structure

# Define paths using environment variables relative to the project root
train_images_dir = project_root / os.environ.get("TRAIN_IMAGES_DIR")
val_images_dir = project_root / os.environ.get("VAL_IMAGES_DIR")
train_annotations_file = project_root / os.environ.get("TRAIN_ANNOTATIONS_FILE")
valid_annotations_file = project_root / os.environ.get("VALID_ANNOTATIONS_FILE")

# Define the base output directory using an environment variable
output_base_dir = project_root / os.environ.get("OUTPUT_BASE_DIR", "dataset")
train_output_dir = output_base_dir / "train"
val_output_dir = output_base_dir / "val"

# Create necessary directories for training and validation data
os.makedirs(train_output_dir, exist_ok=True)
os.makedirs(val_output_dir, exist_ok=True)

# Define category mapping
category_mapping = {1: "penguin", 2: "turtle"}

# Create necessary subdirectories in the training output directory
for category in category_mapping.values():
    os.makedirs(train_output_dir / category, exist_ok=True)

# Load the training and validation annotations
train_annotations = json.load(open(train_annotations_file, "r"))
valid_annotations = json.load(open(valid_annotations_file, "r"))

# Function to move files for the training set
def move_train_files(annotations, source_dir, dest_dir, category_mapping):
    for annotation in annotations:
        image_filename = f"image_id_{annotation['image_id']:03}.jpg"
        category = category_mapping.get(annotation["category_id"], "unknown")

        src_path = source_dir / image_filename
        dest_path = dest_dir / category / image_filename

        if src_path.exists():
            shutil.copy(src_path, dest_path)
        else:
            print(f"Training file not found: {src_path}")

# Function to move files for the validation set
def move_valid_files(annotations, source_dir, dest_dir):
    for annotation in annotations:
        image_filename = f"image_id_{annotation['image_id']:03}.jpg"
        src_path = source_dir / image_filename
        dest_path = dest_dir / image_filename

        if src_path.exists():
            shutil.copy(src_path, dest_path)
        else:
            print(f"Validation file not found: {src_path}")

# Move training images based on training annotations
print("Organizing training images...")
move_train_files(train_annotations, train_images_dir, train_output_dir, category_mapping)

# Move validation images based on validation annotations
print("Organizing validation images...")
move_valid_files(valid_annotations, val_images_dir, val_output_dir)

print("Dataset has been organized successfully.")