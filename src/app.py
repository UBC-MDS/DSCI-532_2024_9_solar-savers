from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

price_df = pd.read_csv("../data/raw/pricePerProvince.csv", encoding='latin1')
sunlight_df = pd.read_csv("../data/processed/processed_municip_kWh.csv", encoding='latin1')

# Initiatlizion
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


# Components
## Title
title = html.H1('Solar Savers')

## Province & Region Selection Dropdowns
province_dropdown = dcc.Dropdown(id='province_dropdown', options=[{'label': province, 'value': province} for province in sunlight_df["Province"].unique()], value=None)
region_dropdown = dcc.Dropdown(id='region_dropdown', options=[], value=None)

## Number of Panels
num_pan_slider = dcc.Slider(min=0,
                            max=20,
                            step=1,
                            value=5,
                            marks={0: '0', 20: '20'},
                            tooltip={'always_visible': True, 'placement': 'top'}
                            )

# Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(dbc.Row([title, 
                         dbc.Row(["Province & Region Selection", 
                                  province_dropdown, 
                                  region_dropdown]),
                         dbc.Row(["Number of Panels", 
                                  num_pan_slider]), 
                         title, 
                         title])),
        dbc.Col(title),
        dbc.Col(dbc.Row([title, title]))
            ]),
    dbc.Row([
        dbc.Col(title),
        dbc.Col(title),
        dbc.Col(title),
        dbc.Col(title)
        ]),
    # dcc.Slider(min=0, max=10, value=5),
])

# Callbacks and Reactivity
@callback(
    Output('region_dropdown', 'options'),
    Input('province_dropdown', 'value')
)
def update_region_dropdown(province_dropdown):
    if province_dropdown is None:
        return []
    else:
        filtered_regions = sunlight_df[sunlight_df['Province'] == province_dropdown]['Municipality'].unique()
        return [{'label': region, 'value': region} for region in filtered_regions]

# Run the app/dashboard
if __name__ == '__main__':
    app.run(debug=True)