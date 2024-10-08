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

# Base directory (optional, if you want to make paths relative to this script)
#base_dir = Path(__file__).resolve().parent

# Define paths using environment variables (with default values)
train_images_dir = Path(os.environ.get("TRAIN_IMAGES_DIR", "archive/train/train")).resolve()
val_images_dir = Path(os.environ.get("VAL_IMAGES_DIR", "archive/valid/valid")).resolve()
train_annotations_file = Path(os.environ.get("TRAIN_ANNOTATIONS_FILE", "archive/train_annotations")).resolve()
valid_annotations_file = Path(os.environ.get("VALID_ANNOTATIONS_FILE", "archive/valid_annotations")).resolve()

# Define the base output directory using an environment variable
output_base_dir = Path(os.environ.get("OUTPUT_BASE_DIR", "dataset")).resolve()
train_output_dir = output_base_dir / "train"
val_output_dir = output_base_dir / "val"

# Create necessary directories for training and validation data
train_output_dir.mkdir(parents=True, exist_ok=True)
val_output_dir.mkdir(parents=True, exist_ok=True)

# Define category mapping
category_mapping = {1: "penguin", 2: "turtle"}

# Create necessary subdirectories in the training output directory
for category in category_mapping.values():
    (train_output_dir / category).mkdir(parents=True, exist_ok=True)

# Load the training and validation annotations
with open(train_annotations_file, "r") as f:
    train_annotations = json.load(f)

with open(valid_annotations_file, "r") as f:
    valid_annotations = json.load(f)

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