In this excercise I'll explore imgages of turtle and penguin in hopes to classify them accurately. I'll also explore some methods to imporve model performance and also have a look at feature maps learned by the covenet. 




Getting setup:

Download the Dataset from Kaggle:(make sure you have your API creds)

kaggle datasets files abbymorgan/penguins-vs-turtles


## Environment Variables
To configure the dataset paths and other settings, create a `.env` file in the root directory with the following values:

```plaintext
MODEL_DIR=models
TRAIN_IMAGES_DIR=archive/train/train
VAL_IMAGES_DIR=archive/valid/valid
TRAIN_ANNOTATIONS_FILE=archive/train_annotations
VALID_ANNOTATIONS_FILE=archive/valid_annotations
OUTPUT_BASE_DIR=dataset
CLASS_TRAIN_IMAGES_DIR=dataset/train
TEST_IMAGES_DIR=dataset/val