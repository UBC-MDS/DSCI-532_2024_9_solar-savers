from dash import Dash
import dash_bootstrap_components as dbc
import dash_vega_components as dvc

from .callbacks import *
from .components import *

# Initiatlizion
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Title
title = html.H1(
    ' Solar Savers',
    style={
        'backgroundColor': 'steelblue',
        'color': 'white',
        'font-size': '48px',
}
)

# SIDE BAR WIDGETS
# Roof Dimensions (for sidebar)
roof_dimensions = dbc.Row(
    [
        dbc.Col(roof_length_input), dbc.Col(roof_width_input), 
        output_panel_count
    ], 
    style={
        'background-color': 'white',
        'padding': 7,
        'border-radius': 3
    })
# Savings Summary
savings_summary = dbc.Row(
    [ 
        dbc.Col(ener_sav_card, width=6, style={'margin-right': 0, 'padding-right': 0}),  
        dbc.Col(savings_card, width=6, style={'margin-left': 0, 'padding-left': 0})
                                
    ], 
    style={'margin-left': 0, 'margin-right': 0}
)

# Cost & Payback Summary
cost_summary = dbc.Row(
    [
        dbc.Col(cost_card, width=6, style={'margin-right': 0, 'padding-right': 0}),  
        dbc.Col(payback_card, width=6, style={'margin-left': 0, 'padding-left': 0})
    ], 
    style={'margin-left': 0, 'margin-right': 0})

# Sidebar layout
sidebar = dbc.Col(
    [
        html.Div("Location"),
        province_dropdown,
        region_dropdown,
        html.Br(),
        html.Div("Roof Dimensions"),
        roof_dimensions, 
        html.Br(),
        html.Div("Number of Panels"),
        num_pan_slider,
        html.Br(),
        html.Div("Panel Type"),
        pan_eff_dropdown, 
        html.Br(),
        savings_summary, 
        cost_summary 
    ],
    style={
        'background-color': '#e6e6e6',
        'padding': 10,
        'border-radius': 0
    }
)
# BOTTOM BAR: PANEL COMPARISON
bottombar = dbc.Row(
    [
        dbc.Col(['Panel Comparison', pan_com_dropdown]),
        dbc.Col(comparison_graph), 
        dbc.Col(diff_sav_card)     
    ], 
    style={
        'background-color': 'rgba(173, 216, 230, 0.7)',
        'padding': 10
    }
)

# MAIN APP LAYOUT
app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col(title)),
        dbc.Row(
            [
                dbc.Col(sidebar, md=4),
                dbc.Col(altair_chart, md=6)
            ],
        ), 
        bottombar
    ],
    style={'margin': 0, 'padding': 0}
)

# Run the app/dashboard
if __name__ == '__main__':
    app.run(debug=False)
    