# image_recognition.py

import tensorflow as tf
import numpy as np
from PIL import Image

# Load your trained model
model = tf.keras.models.load_model('path/to/your/trained/model')

# Function to preprocess an image for prediction
def preprocess_image(image_path):
    img = Image.open(image_path)
    img = img.resize((224, 224))  # Resize image to fit model input
    img_array = np.array(img) / 255.0  # Normalize pixel values
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

# Function to perform image recognition
def predict_image(image_path):
    preprocessed_img = preprocess_image(image_path)
    prediction = model.predict(preprocessed_img)
    return prediction

# Example usage
if __name__ == "__main__":
    image_path = 'path/to/your/test/image.jpg'
    prediction = predict_image(image_path)
    print(prediction)
