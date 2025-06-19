import cv2
import logging

logger = logging.getLogger(__name__)

def load_image(image_path):
    """Loads an image using OpenCV."""
    try:
        img = cv2.imread(image_path)
        if img is None:
            logger.error(f"Could not load image from {image_path}")
            return None
        logger.info(f"Image loaded from {image_path}")
        return img
    except Exception as e:
        logger.error(f"Error loading image: {e}")
        return None

def resize_image(img, width, height):
    """Resizes an image using OpenCV."""
    try:
        resized_img = cv2.resize(img, (width, height))
        logger.info(f"Image resized to {width}x{height}")
        return resized_img
    except Exception as e:
        logger.error(f"Error resizing image: {e}")
        return None

def display_image(img, window_name="Image"):
    """Displays an image using OpenCV."""
    try:
        cv2.imshow(window_name, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        logger.info(f"Image displayed in window: {window_name}")
    except Exception as e:
        logger.error(f"Error displaying image: {e}")

if __name__ == "__main__":
  #Example use
  logging.basicConfig(level=logging.INFO)
  image_path = "slum_image.jpg"
  img = load_image(image_path)
  if img is not None:
    resized_img = resize_image(img, 200, 200)
    display_image(resized_img, "Resized Image")