from dash import Dash, html
import dash_bootstrap_components as dbc

from .components import (
    title,
    sidebar,
    altair_chart,
    bottombar,
    info_section,
    info_button
)

# Initiatlizion
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], title="Solar Savers")
server = app.server


# MAIN APP LAYOUT
app.layout = dbc.Container([
        dbc.Row([
                dbc.Col(title), dbc.Col(html.Div(info_button), className="text-right", width="auto", style={'background-color': 'transparent', 
                                                                                                            'padding-right': '24px', 
                                                                                                            'padding-top': '12px',
                                                                                                            'padding-bottom': '12px'})
                ],style={'background-color':'#FCAE1E'}
        ),

        dbc.Row(
            dbc.Col(info_section, style={"margin-top": "0px"})
        ),
        dbc.Row(
            [
                dbc.Col(sidebar, md=4),
                dbc.Col(altair_chart, md=8)
            ],
        ), 
        bottombar
    ],
    fluid=True,
    style={'margin': 0, 'padding': 0, 'overflow-x': 'hidden'}
)

# Run the app/dashboard
if __name__ == '__main__':
    app.run(debug=False)
    