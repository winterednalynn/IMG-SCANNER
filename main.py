import tensorflow as tf
import numpy as np
import cv2

import Dicegame
import GuessTheWord as guesstheWord
import Quiz

# Load the pre-trained MobileNetV2 model
model = tf.keras.applications.MobileNetV2(weights='imagenet')


# Function to PREPARE the image
def preImage(image_path):
    image = cv2.imread(image_path) #Load image in PARTICULAR path file
    print(f"OG IMAGE SHAPE : {image.shape}")  # TEST PRINT LINE
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # TRANSITIONING PICTURE FROM BGR to RGB ; on stack oflow says that image are based on BGR as default for openCVs
    image = cv2.resize(image, (224, 224)) # ReSize this img to a size 224x224 pixels
    print(f"MODIFIED IMG SHAPE: {image.shape}") # TEST PRINT LINE
    image = np.expand_dims(image, axis=0)  # This add DIMENSION to the image
    print(f"EXPANDED IMG SHAPE: {image.shape}")  # TEST PRINT LINE
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image) #Prepare image to FIT input requirements for MOBILNETV2 - ref https://ar5iv.labs.arxiv.org/html/1409.0575>
    return image # once the img is PROCESSED , it will return it's final modification.


# Function to get the class label
def getThatImage(image_path):
    image = preImage(image_path) # reeling in the pre processed img
    predictions = model.predict(image) # using model.predict  this will guess what in the picture basically.
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1) # then it decrypts the image to determine what the MODEL thinks the picture show.
    return decoded_predictions[0][0][1] # this is most likely the prediction!


def main(image_path):

    try:
        label = getThatImage(image_path) #Queuing the image method which is the final process for the image
        print(f"Detected label: {label}")  # PRINT for testing

        if label == "cardigan": # DEFINED BHBE.JPG # Processed images with model name per tensorflow ; mobilenet
            print("Imaged scanned'- BHBE. Starting Wordle game.")
            guesstheWord.GuessTheWord()
        elif label == "jersey": # DEFINED AS BHBRE.JPG
            print("Imaged scanned - for BHBRE. Starting Dice game.")
            Dicegame.starDice()
        elif label =="window_shade":
            print("Image scanned - for MBLHBE. Starting Quiz game")
            Quiz.pregnancyQuiz()
        else:
            print(f"No specific game associated with this model '{label}'.")

    except Exception as e:
        print(f"Uhoh error: {e}")


#main scanner.
if __name__ == "__main__":
    image_path = r"C:\School\Programming VI\TestF\Image\BHBRE.jpg"  # Change to your specific image path
    main(image_path) # function main w/ img
