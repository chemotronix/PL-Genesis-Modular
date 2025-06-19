import logging
from ai_models import object_detection, population_density
from data_processing import geojson_handler
from utils import config
import utils.logging

logger = utils.logging.setup_logging()  # Initialize logging

def main():
    """Main function to orchestrate the digital twin project."""

    logger.info("Starting digital twin project...")

    # Example: Load GeoJSON data
    geojson_file = config.GEOJSON_FILE_PATH
    gdf = geojson_handler.load_geojson(geojson_file)

    if gdf is not None:
        logger.info("GeoJSON data loaded successfully.")
        # Perform further processing with the GeoDataFrame

    # Example: Object detection
    object_detection_model = object_detection.load_object_detection_model()
    if object_detection_model:
        image_path = "slum_image.jpg"
        detections = object_detection.detect_objects(object_detection_model, image_path)
        if detections:
            logger.info("Object detection completed.")
            object_detection.visualize_detections(image_path, detections)

    # Example: Population density estimation
    population_data = population_density.load_population_data()
    if population_data is not None:
        population_model = population_density.train_population_density_model(population_data)
        if population_model:
            building_area = 1000
            road_density = 500
            predicted_density = population_density.predict_population_density(population_model, building_area, road_density)
            if predicted_density is not None:
                logger.info(f"Predicted population density: {predicted_density:.2f}")

    logger.info("Digital twin project completed.")

if __name__ == "__main__":
    main()