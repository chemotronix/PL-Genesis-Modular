# Configuration settings

# File paths
POPULATION_DATA_PATH = "population_data.csv"
GEOJSON_FILE_PATH = "slum_area.geojson"
OBJECT_DETECTION_MODEL_PATH = "resnet50_imagenet.h5"  # Or None if using the default

# Image parameters
IMAGE_SIZE = 224 #Image size for the Object Detection Model

# Logging settings
LOG_FILE_PATH = "digital_twin.log"
LOG_LEVEL = "INFO" #Can be DEBUG, INFO, WARNING, ERROR, CRITICAL

#Simulation parameters (Example)
SOLAR_PANEL_EFFICIENCY = 0.15 #Example of project configs.