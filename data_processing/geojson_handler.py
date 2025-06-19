import geopandas as gpd
import json
import logging

logger = logging.getLogger(__name__)

def load_geojson(geojson_file):
    """Loads a GeoJSON file into a GeoPandas GeoDataFrame."""
    try:
        gdf = gpd.read_file(geojson_file)
        logger.info(f"GeoJSON loaded successfully from {geojson_file}")
        return gdf
    except Exception as e:
        logger.error(f"Error loading GeoJSON: {e}")
        return None

def extract_feature_info(gdf, feature_id):
    """Extracts information about a specific feature from the GeoDataFrame."""
    try:
        feature = gdf.iloc[feature_id]
        properties = feature.drop('geometry').to_dict()
        geometry = feature.geometry.__geo_interface__

        feature_info = {
            "properties": properties,
            "geometry": geometry
        }
        return feature_info
    except IndexError:
        logger.warning(f"Feature with ID {feature_id} not found.")
        return None
    except Exception as e:
        logger.error(f"Error extracting feature info: {e}")
        return None

def calculate_area(gdf):
    """Calculates the area of each feature in the GeoDataFrame."""
    gdf['area'] = gdf.geometry.area
    return gdf

def save_geojson(gdf, output_file):
    """Saves a GeoDataFrame to a GeoJSON file."""
    try:
        gdf.to_file(output_file, driver='GeoJSON')
        logger.info(f"GeoJSON saved successfully to {output_file}")
    except Exception as e:
        logger.error(f"Error saving GeoJSON: {e}")

if __name__ == '__main__':
    # Example Usage
    logging.basicConfig(level=logging.INFO)
    geojson_file = "slum_area.geojson"
    gdf = load_geojson(geojson_file)
    if gdf is not None:
      gdf = calculate_area(gdf)
      save_geojson(gdf, "slum_area_with_area.geojson")