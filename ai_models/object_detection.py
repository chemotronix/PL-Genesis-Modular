
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
import numpy as np
import cv2
from utils.config import OBJECT_DETECTION_MODEL_PATH, IMAGE_SIZE
import logging

logger = logging.getLogger(__name__)

def load_object_detection_model(model_path=OBJECT_DETECTION_MODEL_PATH):
    """Loads the object detection model."""
    try:
        model = ResNet50(weights='imagenet')
        logger.info(f"Object detection model loaded from {model_path}")
        return model
    except Exception as e:
        logger.error(f"Error loading object detection model: {e}")
        return None

def detect_objects(model, image_path):
    """Detects objects in an image using the provided model."""
    try:
        img = image.load_img(image_path, target_size=(IMAGE_SIZE, IMAGE_SIZE))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)

        predictions = model.predict(img_array)
        decoded_predictions = decode_predictions(predictions, top=5)[0]

        return decoded_predictions
    except Exception as e:
        logger.error(f"Error detecting objects: {e}")
        return None

def visualize_detections(image_path, detections):
    """Visualizes detections on the image."""
    try:
        img = cv2.imread(image_path)
        height, width, _ = img.shape

        for i, (object_id, object_name, probability) in enumerate(detections):
            label = f"{object_name}: {probability:.2f}"
            print(label)

        cv2.imshow('Object Detections', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except Exception as e:
        logger.error(f"Error visualizing detections: {e}")

if __name__ == '__main__':
    # Example usage (only for testing)
    logging.basicConfig(level=logging.INFO)  # Set logging level
    model = load_object_detection_model()
    if model:
        detections = detect_objects(model, "slum_image.jpg")
        if detections:
            visualize_detections("slum_image.jpg", detections)