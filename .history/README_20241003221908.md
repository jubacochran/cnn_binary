Getting setup:

Download the Dataset from Kaggle:(make sure you have your API creds)

kaggle datasets files abbymorgan/penguins-vs-turtles


## Environment Variables
To configure the dataset paths and other settings, create a `.env` file in the root directory with the following values:

```plaintext
TRAIN_IMAGES_DIR=archive/train/train
VAL_IMAGES_DIR=archive/valid/valid
TRAIN_ANNOTATIONS_FILE=archive/train_annotations
VALID_ANNOTATIONS_FILE=archive/valid_annotations
OUTPUT_BASE_DIR=dataset




### Set Environment Variables Manually (For Testing)
If you prefer not to use `.env` files, you can manually set environment variables in your terminal:

- On **Linux/Mac**:

  ```bash
  export TRAIN_IMAGES_DIR=archive/train/train
  export VAL_IMAGES_DIR=archive/valid/valid
  export TRAIN_ANNOTATIONS_FILE=archive/train_annotations
  export VALID_ANNOTATIONS_FILE=archive/valid_annotations
  export OUTPUT_BASE_DIR=dataset

    ```powershell
- On **Windows**:
    set TRAIN_IMAGES_DIR=archive/train/train
    set VAL_IMAGES_DIR=archive/valid/valid
    set TRAIN_ANNOTATIONS_FILE=archive/train_annotations
    set VALID_ANNOTATIONS_FILE=archive/valid_annotations
    set OUTPUT_BASE_DIR=dataset


