# Import necessary libraries
import cv2  # OpenCV library for image processing
import numpy as np  # NumPy for numerical operations
import streamlit as st  # Streamlit for building the web interface
from keras.src.applications.mobilenet_v2 import MobileNetV2  # MobileNetV2 model
from tensorflow.keras.applications.mobilenet_v2 import (
    preprocess_input,  # Preprocessing utility for MobileNetV2
    decode_predictions  # Utility to decode model predictions
)
from PIL import Image  # PIL for image loading and manipulation


# Function to load the pretrained MobileNetV2 model
def load_model():
    """
    Load the MobileNetV2 model with pretrained weights from ImageNet.
    Returns:
        model: A Keras model instance of MobileNetV2.
    """
    model = MobileNetV2(weights="imagenet")
    return model


# Function to preprocess the uploaded image for model input
def preprocess_image(image):
    """
    Preprocesses the input image to make it compatible with the model.
    Steps:
    1. Convert the image to a NumPy array.
    2. Resize the image to the target size (224x224).
    3. Apply MobileNetV2-specific preprocessing.
    4. Expand dimensions to simulate a batch of size 1.

    Args:
        image: PIL Image object uploaded by the user.
    Returns:
        img: Preprocessed NumPy array ready for model prediction.
    """
    img = np.array(image)  # Convert the image to a NumPy array
    img = cv2.resize(img, (224, 224))  # Resize the image to 224x224 pixels
    img = preprocess_input(img)  # Apply MobileNetV2 preprocessing
    img = np.expand_dims(img, axis=0)  # Add a batch dimension
    return img


# Function to classify the uploaded image
def classify_image(model, image):
    """
    Classifies the input image using the MobileNetV2 model.
    Args:
        model: The loaded MobileNetV2 model.
        image: PIL Image object uploaded by the user.
    Returns:
        decoded_predictions: Top-3 predicted classes with their probabilities.
    """
    try:
        process_image = preprocess_image(image)  # Preprocess the image
        predictions = model.predict(process_image)  # Make predictions
        decoded_predictions = decode_predictions(predictions, top=3)[0]  # Decode top-3 predictions
        st.success("🖼️ Success classifying 😍👨🏽‍💻")  # Display success message
        return decoded_predictions
    except Exception as e:
        st.error(f"Error classifying image: {str(e)}.")  # Display error message
        return None


# Main function for the Streamlit app
def main():
    """
    Entry point for the Streamlit app.
    Handles the UI, image upload, and classification workflow.
    """
    # Set Streamlit page configuration
    st.set_page_config(
        page_title="AI Image Classifier",  # Title of the app
        page_icon="🖼️",  # Favicon for the app
        layout="centered"  # Layout configuration
    )
    # App title and description
    st.title("AI Image Classifier")
    st.write("Upload an image and let AI tell you what is in it!")

    # Cache the model to avoid reloading it multiple times
    @st.cache_resource
    def load_cached_model():
        """
        Loads the MobileNetV2 model and caches it for faster access.
        Returns:
            model: Cached MobileNetV2 model.
        """
        return load_model()

    # Load the cached model
    model = load_cached_model()

    # File uploader for image upload
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Display the uploaded image
        image = st.image(
            uploaded_file, caption="Uploaded Image", use_container_width=True
        )

        # Classify button
        btn = st.button("Classify Image")

        if btn:  # If the classify button is clicked
            with st.spinner("Analyzing Image..."):  # Show loading spinner
                image = Image.open(uploaded_file)  # Open the uploaded image
                predictions = classify_image(model, image)  # Classify the image

                # Display predictions if available
                if predictions:
                    st.subheader("Predictions")  # Section header
                    # Iterate over top-3 predictions
                    for _, label, score in predictions:
                        # Display label and confidence score
                        st.write(f"**{label}**: {score: .2%}")


# Run the app
if __name__ == "__main__":
    main()