import os
import geopandas as gpd
import pandas as pd
import pyarrow as pa
from shapely import wkb

os.chdir(os.path.dirname(os.path.abspath(__file__)))

price_df = pd.read_csv("../data/raw/pricePerProvince.csv", encoding='latin1').sort_values(by='price per ¢/kWh', ascending=False)
alt_data = pd.read_parquet('../data/processed/kWh_poly.parquet')
alt_data['geometry'] = alt_data['geometry'].apply(wkb.loads)
alt_data = gpd.GeoDataFrame(alt_data)
gdf_ca = gpd.read_parquet('../data/processed/ne_50m_admin_1_states_provinces.parquet')
panel_df = pd.read_csv('../data/raw/panels.csv')