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
num_pan_slider = dcc.Slider(id='num_pan_slider',
                            min=0,
                            max=20,
                            step=1,
                            value=5,
                            marks={0: '0', 20: '20'},
                            tooltip={'always_visible': True, 'placement': 'top'}
                            )

## Panel Efficiency
pan_eff_dropdown = dcc.Dropdown(id='panel_efficiency', options=["Low < 15%", "Standard 15-18%", "High 18-22%", "Premium > 22%"], value=None)

## Panel Comparison
pan_com_dropdown = dcc.Dropdown(id='panel_comparison', options=["Low < 15%", "Standard 15-18%", "High 18-22%", "Premium > 22%"], value=None, multi=True)

## Difference in savings card
diff_sav_card = dbc.Card(id='diff_card', children=[dbc.CardHeader('Difference in Savings'), dbc.CardBody('$XXX /yr')]),

## Comparison graph


## Energy Savings Card
ener_sav_card = dbc.Card(id='ener_card', children=[dbc.CardHeader('Energy Savings'), dbc.CardBody('XXX kWh/yr')]),

## Savings
savings_card = dbc.Card(id='sav_card', children=[dbc.CardHeader('Savings'), dbc.CardBody('$XXX /yr')]),



# Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(dbc.Row([title, 
                         dbc.Row(["Province & Region Selection", 
                                  province_dropdown, 
                                  region_dropdown]),
                         dbc.Row(["Number of Panels", 
                                  num_pan_slider]), 
                         dbc.Row(["Panel Efficiency", 
                                  pan_eff_dropdown]), 
                         dbc.Row(["Panel Comparison", 
                                  pan_com_dropdown])])),
        dbc.Col("Map Placeholder"),
        dbc.Col(dbc.Row([title, title]))
            ]),
    dbc.Row([
        dbc.Col(diff_sav_card),
        dbc.Col(title),
        dbc.Col(ener_sav_card),
        dbc.Col(savings_card)
        ])
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

@callback(
    Output('ener_card', 'children'),
    Output('sav_card', 'children'),
    Input('province_dropdown', 'value'),
    Input('region_dropdown', 'value'),
    Input('panel_efficiency', 'value'),
    Input('num_pan_slider', 'value')
)
def update_cards(province, region, efficiency, num_pan):
    card_ener = [
        dbc.CardHeader('Energy Savings'),
        dbc.CardBody('XXX kWh/yr')
    ]

    card_sav = [
        dbc.CardHeader('Savings'),
        dbc.CardBody('$XXX/yr')
    ]

    if efficiency == "Low < 15%":
        conversion_rate = 0.15
    elif efficiency == "Standard 15-18%":
        conversion_rate = 0.18
    elif efficiency == "High 18-22%":
        conversion_rate = 0.22
    elif efficiency == "Premium > 22%":
        conversion_rate = 0.25
    else:
        conversion_rate = 0

    if province and region:
        province_price = price_df[(price_df['province'] == province)]["price per ¢/kWh"].iloc[0] / 100
        filtered_row = sunlight_df[(sunlight_df['Province'] == province) & (sunlight_df['Municipality'] == region) & (sunlight_df['Month'] == 'Annual')]
        if not filtered_row.empty:
            energy_savings = filtered_row['South-facing with vertical (90 degrees) tilt'].iloc[0] * conversion_rate * 1.65 * 365 * num_pan
            card_ener = dbc.Card([dbc.CardHeader('Energy Savings'), dbc.CardBody(f'{energy_savings:.2f} kWh/yr')])
            card_sav = dbc.Card([dbc.CardHeader('Savings'), dbc.CardBody(f'${energy_savings * province_price:.2f}/yr')])

            return card_ener, card_sav
    return card_ener, card_sav

# Run the app/dashboard
if __name__ == '__main__':
    app.run(debug=True)