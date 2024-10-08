import json
import os




# Define paths to directories
train_images_dir = "archive/train/train"
val_images_dir = "archive/valid/valid"

# Define paths to annotation files
train_annotations_file = "archive/train_annotations"
val_annotations_file = "archive/valid_annotations"
train_annotations = json.load(open(train_annotations_file, "r"))

print(train_annotations[0])


