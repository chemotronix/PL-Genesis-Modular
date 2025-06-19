import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from utils.config import POPULATION_DATA_PATH
import logging

logger = logging.getLogger(__name__)

def load_population_data(data_path=POPULATION_DATA_PATH):
    """Loads population data from a CSV file."""
    try:
        data = pd.read_csv(data_path)
        logger.info(f"Population data loaded from {data_path}")
        return data
    except Exception as e:
        logger.error(f"Error loading population data: {e}")
        return None

def train_population_density_model(data):
    """Trains a linear regression model for population density estimation."""
    try:
        X = data[['building_footprint_area', 'road_network_density']]
        y = data['population_density']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = LinearRegression()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        logger.info(f"Mean Squared Error: {mse}")

        return model
    except Exception as e:
        logger.error(f"Error training population density model: {e}")
        return None

def predict_population_density(model, building_footprint_area, road_network_density):
    """Predicts population density given building footprint area and road network density."""
    try:
        new_data = pd.DataFrame({'building_footprint_area': [building_footprint_area], 'road_network_density': [road_network_density]})
        prediction = model.predict(new_data)
        return prediction[0]
    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        return None

if __name__ == '__main__':
    # Example usage (only for testing)
    logging.basicConfig(level=logging.INFO)  # Set logging level

    data = load_population_data()
    if data is not None:
        model = train_population_density_model(data)
        if model is not None:
            building_area = 1000
            road_density = 500
            predicted_density = predict_population_density(model, building_area, road_density)
            if predicted_density is not None:
                print(f"Predicted population density: {predicted_density:.2f}")