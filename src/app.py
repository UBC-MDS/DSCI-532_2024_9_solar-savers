from dash import Dash, html
import dash_bootstrap_components as dbc

from components import (
    title,
    sidebar,
    altair_chart,
    bottombar,
    info_section,
    info_button
)

# Initiatlizion
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server


# MAIN APP LAYOUT
app.layout = dbc.Container([
        dbc.Row([

                dbc.Col(title), dbc.Col(html.Div(info_button), className="text-right", width="auto", style={'background-color': 'transparent'})
            ], 
            style={'background-color':'steelblue'}
            ),
        dbc.Row(
            dbc.Col(info_section, style={"margin-top": "4px"})
        ),
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
    