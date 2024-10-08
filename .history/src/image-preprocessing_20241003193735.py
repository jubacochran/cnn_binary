import json
import shutil
import os

# Define paths to directories
train_images_dir = "archive/train/train"
val_images_dir = "archive/valid/valid"

# Define paths to annotation files
train_annotations_file = "archive/train_annotations"
valid_annotations_file = "archive/valid_annotations"

train_annotations = json.load(open(train_annotations_file[0], "r"))
valid_annotations = json.load(open(valid_annotations_file[0], "r"))



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
train_annotations = [train_annotations]

valid_annotations = [valid_annotations]

# Function to move files for the training set
def move_train_files(annotations, source_dir, dest_dir, category_mapping):
    for annotation in annotations:
        image_filename = f"image_id_{annotation['image_id']:03}.jpg"
        category = category_mapping.get(annotation["category_id"], "unknown")
        
        src_path = os.path.join(source_dir, image_filename)
        dest_path = os.path.join(dest_dir, category, image_filename)
        
        if os.path.exists(src_path):
            shutil.copy(src_path, dest_path)
        else:
            print(f"Training file not found: {src_path}")

# Function to move files for the validation set
def move_valid_files(annotations, source_dir, dest_dir):
    for annotation in annotations:
        image_filename = f"image_id_{annotation['image_id']:03}.jpg"
        src_path = os.path.join(source_dir, image_filename)
        dest_path = os.path.join(dest_dir, image_filename)

        if os.path.exists(src_path):
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