import json
import shutil

# Define paths to directories
train_images_dir = "archive/train/train"
val_images_dir = "archive/valid/valid"

# Define the base output directory
output_base_dir = "dataset"
train_output_dir = os.path.join(output_base_dir, "train")
val_output_dir = os.path.join(output_base_dir, "val")  # Single directory for validation images

# Create necessary directories for training and validation data
os.makedirs(train_output_dir, exist_ok=True)
os.makedirs(val_output_dir, exist_ok=True)

# Define category mapping
category_mapping = {1: "penguin", 2: "turtle"}

# Create necessary subdirectories in the training output directory
for category in category_mapping.values():
    os.makedirs(os.path.join(train_output_dir, category), exist_ok=True)

# Load the training and validation annotations (these can be read from files)
train_annotations = []