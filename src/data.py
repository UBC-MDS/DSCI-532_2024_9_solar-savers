import os
import geopandas as gpd
import pandas as pd


os.chdir(os.path.dirname(os.path.abspath(__file__)))

price_df = pd.read_csv("../data/raw/pricePerProvince.csv", encoding='latin1').sort_values(by='price per ¢/kWh', ascending=False)
# sunlight_df = pd.read_json("../data/processed/kWh_poly.json", lines=True, encoding='latin1')

json_file_path = '../data/processed/kWh_poly.json'
df1 = gpd.read_file(json_file_path)
alt_data = df1.to_crs(epsg=4326)  
alt_data = alt_data.dropna(subset=['latitude', 'longitude'])

file_path = '../data/raw/ne_50m_admin_1_states_provinces/ne_50m_admin_1_states_provinces.shp'
gdf1 = gpd.read_file(file_path)
gdf_ca = gdf1[gdf1['iso_a2'] == 'CA']

panel_file_path = '../data/raw/panels.csv'
panel_df = pd.read_csv(panel_file_path)