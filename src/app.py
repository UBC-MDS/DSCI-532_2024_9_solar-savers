from dash import Dash, html, dcc, callback, Output, Input, dash_table
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import pandas as pd
import altair as alt
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
comparison_graph = dvc.Vega(id='bars', spec={})

## Energy Savings Card
ener_sav_card = dbc.Card(id='ener_card', children=[dbc.CardHeader('Energy Savings'), dbc.CardBody('XXX kWh/yr')]),

## Savings
savings_card = dbc.Card(id='sav_card', children=[dbc.CardHeader('Savings'), dbc.CardBody('$XXX /yr')]),

## Price information card
price_info_card = dash_table.DataTable(price_df.to_dict('records'), [{"name": i, "id": i} for i in price_df.columns],
    style_table={'height': '300px', 'overflowY': 'auto'})

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
        dbc.Col(dbc.Row(["Legend Placeholder", price_info_card]))
            ]),
    dbc.Row([
        dbc.Col(diff_sav_card),
        dbc.Col(comparison_graph),
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
    Output('diff_card', 'children'),
    Input('province_dropdown', 'value'),
    Input('region_dropdown', 'value'),
    Input('panel_efficiency', 'value'),
    Input('num_pan_slider', 'value'),
    Input('panel_comparison', 'value')
)
def update_savings_cards(province, region, efficiency, num_pan, panel_comparison):
    conversion_rate = {
        "Low < 15%": 0.15,
        "Standard 15-18%": 0.18,
        "High 18-22%": 0.22,
        "Premium > 22%": 0.25
    }
 
    card_ener = [
        dbc.CardHeader('Energy Savings'),
        dbc.CardBody('XXX kWh/yr')
    ]

    card_sav = [
        dbc.CardHeader('Savings'),
        dbc.CardBody('$XXX/yr')
    ]
    
    card_diff = [
        dbc.CardHeader('Difference in Savings'),
        dbc.CardBody('$XXX/yr')
    ]
 
    if province and region:
        province_price = price_df[(price_df['province'] == province)]["price per ¢/kWh"].iloc[0] / 100
        filtered_row = sunlight_df[(sunlight_df['Province'] == province) & (sunlight_df['Municipality'] == region) & (sunlight_df['Month'] == 'Annual')]
        if not filtered_row.empty:
            energy_savings = filtered_row['South-facing with vertical (90 degrees) tilt'].iloc[0] * conversion_rate.get(efficiency, 0) * 1.65 * 365 * num_pan
            card_ener = dbc.Card([dbc.CardHeader('Energy Savings'), dbc.CardBody(f'{energy_savings:.2f} kWh/yr')])
            card_sav = dbc.Card([dbc.CardHeader('Savings'), dbc.CardBody(f'${energy_savings * province_price:.2f}/yr')])

            if panel_comparison and len(panel_comparison) >= 2:
                comparison_values = [conversion_rate[value] for value in panel_comparison]
                comparison_savings = []
                for value in comparison_values:
                    comparison_savings.append(filtered_row['South-facing with vertical (90 degrees) tilt'].iloc[0] * value * 1.65 * 365 * num_pan)
                diff = (comparison_savings[0] - comparison_savings[1]) * province_price  
                card_diff = dbc.Card([dbc.CardHeader('Difference in Savings'), dbc.CardBody(f'${diff:.2f}/yr'), dbc.CardFooter(f'{panel_comparison[0]} vs. {panel_comparison[1]}')])


            return card_ener, card_sav, card_diff
    return card_ener, card_sav, card_diff

@callback(
    Output('bars', 'spec'),
    Input('panel_comparison', 'value'),
    Input('province_dropdown', 'value'),
    Input('region_dropdown', 'value'),
    Input('num_pan_slider', 'value'),
)
def create_chart(panel_comparison, province, region, num_pan):
    if panel_comparison:
        conversion_rate = {
            "Low < 15%": 0.15,
            "Standard 15-18%": 0.18,
            "High 18-22%": 0.22,
            "Premium > 22%": 0.25
        }

    if province and region:
        province_price = price_df[(price_df['province'] == province)]["price per ¢/kWh"].iloc[0] / 100
        filtered_row = sunlight_df[(sunlight_df['Province'] == province) & (sunlight_df['Municipality'] == region) & (sunlight_df['Month'] == 'Annual')]
        if not filtered_row.empty:
            if panel_comparison and len(panel_comparison) >= 1:
                comparison_values = [conversion_rate[value] for value in panel_comparison]
                comparison_savings = []
                for value in comparison_values:
                    comparison_savings.append(filtered_row['South-facing with vertical (90 degrees) tilt'].iloc[0] * value * 1.65 * 365 * num_pan * province_price)
                df = pd.DataFrame({comp: [saving] for comp, saving in zip(panel_comparison, comparison_savings)})
                df = df.T.reset_index().rename(columns={'index': 'Panel Comparison', 0: 'Savings'})
                return(
                    alt.Chart(df).mark_bar().encode(
                            y=alt.Y('Panel Comparison', title='Panel Comparison'),
                            x=alt.X('Savings', title='Savings ($/yr)', stack=None)
                        ).interactive().to_dict()
                )
    else:
        return {}




# Run the app/dashboard
if __name__ == '__main__':
    app.run(debug=True)