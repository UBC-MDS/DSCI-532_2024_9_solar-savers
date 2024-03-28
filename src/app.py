from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Initiatlizion
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout
app.layout = dbc.Container([
    html.Label('My first slider'),  # Label
    dcc.Slider(min=0, max=10, value=5),
])

# Callbacks and Reactivity


# Run the app/dashboard
if __name__ == '__main__':
    app.run(debug=True)