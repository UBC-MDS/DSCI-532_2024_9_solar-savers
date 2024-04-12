from dash import Dash
import dash_bootstrap_components as dbc
import dash_vega_components as dvc

from .callbacks import *
from .components import *

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
                         roof_width_input,
                         roof_length_input,
                         dbc.Row(["Panel Efficiency", pan_eff_dropdown]), 
                         output_panel_count,
                         dbc.Row(["Number of Panels", num_pan_slider]), 
                         dbc.Row([
                                    dbc.Col(ener_sav_card, width=5, style={'margin-right': 0, 'padding-right': 0}),  
                                    dbc.Col(savings_card, width=5, style={'margin-left': 0, 'padding-left': 0})
                                ], style={'margin-left': 0, 'margin-right': 0}),
                         dbc.Row([
                                    dbc.Col(cost_card, width=5, style={'margin-right': 0, 'padding-right': 0}),  
                                    dbc.Col(payback_card, width=5, style={'margin-left': 0, 'padding-left': 0})
                                ], style={'margin-left': 0, 'margin-right': 0})
                         ])),

        dbc.Col(dvc.Vega(id="altair-chart",
                        opt={"renderer": "svg", "actions": False},
                        spec=combined_chart.to_dict()), width=7),
        # dbc.Col(dbc.Row(["Legend Placeholder", price_info_card]))
            ], style={'height': '600px'}),
    dbc.Row([
        dbc.Col(["Panel Comparison", 
                    pan_com_dropdown]),
        dbc.Col(comparison_graph),
        dbc.Col(diff_sav_card)
        ])
], style={'margin': '10px'})


# Run the app/dashboard
if __name__ == '__main__':
    app.run(debug=False)
    