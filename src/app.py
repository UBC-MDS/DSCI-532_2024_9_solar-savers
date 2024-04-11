from dash import Dash
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
from src.callbacks import *
from src.components import * # title, province_dropdown, region_dropdown, num_pan_slider, pan_eff_dropdown, ener_sav_card, savings_card, combined_chart, pan_com_dropdown, comparison_graph, diff_sav_card


# Initiatlizion
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server


# Layout
app.layout = dbc.Container([
    dbc.Row([title]),
    dbc.Row([
        dbc.Col(dbc.Row([ 
                         dbc.Row(["Province & Region Selection", 
                                  province_dropdown, 
                                  region_dropdown]),
                         dbc.Row(["Number of Panels", 
                                  num_pan_slider]), 
                         dbc.Row(["Panel Efficiency", 
                                  pan_eff_dropdown]), 
                         dbc.Row(ener_sav_card),
                         dbc.Row(savings_card)])),
        dbc.Col(dvc.Vega(id="altair-chart",
                        opt={"renderer": "svg", "actions": False},
                        spec=combined_chart.to_dict()), width=7),
        # dbc.Col(dbc.Row(["Legend Placeholder", price_info_card]))
            ], style={'height': '500px'}),
    dbc.Row([
        dbc.Col(["Panel Comparison", 
                    pan_com_dropdown]),
        dbc.Col(comparison_graph),
        dbc.Col(diff_sav_card)
        ])
], style={'margin': '10px'})


# Run the app/dashboard
if __name__ == '__main__':
    app.run(debug=True)
    