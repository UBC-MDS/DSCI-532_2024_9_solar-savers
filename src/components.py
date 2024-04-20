from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import altair as alt

from .data import alt_data, price_df, gdf_ca, panel_df

# Description & Explanation
app_info = [
    html.P(
        "Welcome to Solar Savers! Our app is crafted to empower Canadian homeowners (like, you!) with the knowledge to make well-informed decisions when considering the purchase of solar panels.", style={'font-size': '16px'}
    ),
    html.Br(),
    html.P(
        "Begin your journey by selecting your province or territory, then specify your region. Optionally, input your roof dimensions to calculate the maximum number of solar panels for your home. Select a panel type, then see your energy and financial savings soar!", style={'font-size': '16px'}
    ), 
    html.P("Explore the map to visualize the amount of insolation (solar energy received per square meter of land) and electricity costs in different regions. Can't decide between two panels? Let our panel comparison widget at the bottom guide your decision!", style={'font-size': '16px'})
]

info_button = dbc.Button(
    "Learn More!",
    id="info-button",
    outline=False,
    style={
        'width': '150px',
        'background-color': 'steelblue',
        "font-weight": "bold",
        'color': 'white'
    }
)

info_section = dbc.Collapse(
        app_info,
    id="info",
    style ={'background-color':'white', 
            'padding': 10}
)

# Title
title = html.H1(
    ' Solar Savers',
    style={
        'backgroundColor': '#FCAE1E',
        'color': 'white',
        'font-size': '48px',
        'margin' : '0',
        'padding-left': '10px', 
        'padding-right': '10px'

}
)

## Province & Region Selection Dropdowns
province_dropdown = dcc.Dropdown(id='province_dropdown', 
                                 options=[{'label': province, 'value': province} for province in alt_data["Province"].unique()], 
                                 value=None, 
                                 placeholder='Select Province or Territory...')
region_dropdown = dcc.Dropdown(id='region_dropdown', options=[], 
                               value=None, 
                               placeholder='Select Region...')

## Number of Panels
num_pan_slider = html.Div(
    dcc.Slider(
        id='num_pan_slider',
        min=0,
        max=20,
        step=1,
        value=5,
        marks={0: '0', 20: '20'},
        tooltip={'always_visible': True, 'placement': 'top'}
    ),
    style={'background-color': '#e6e6e6', 'margin-top': '10px'}
)

## Panel Efficiency
pan_eff_dropdown = dcc.Dropdown(id='panel_efficiency', options=[{'label': name , 'value': name } for name  in panel_df["name "].unique()], value=None)

## Panel Comparison
pan_com_dropdown = dcc.Dropdown(id='panel_comparison', options=[{'label': name , 'value': name } for name  in panel_df["name "].unique()], value=None, multi=True)

## Comparison graph
comparison_graph = dvc.Vega(id='bars', spec={})

## Altair Chart
background = alt.Chart(gdf_ca).mark_geoshape(
fill='lightgray',
stroke='white'
).project(
    type='transverseMercator',
    rotate=[90, 0, 0]
).properties(
    width=700,
    height=500, 
    title = "Solar Energy Potential Across Canadian Regions"
)

points = alt.Chart(alt_data).mark_circle().encode(
longitude='longitude:Q', 
latitude='latitude:Q',
color=alt.Color('South-facing with vertical (90 degrees) tilt',
                scale=alt.Scale(scheme="oranges"),
                legend=alt.Legend(title='Mean Daily Insolation (kWh/m²)')),     
size=alt.value(50),  
tooltip=[alt.Tooltip('Municipality:N', title='Region'),
            alt.Tooltip('price', title='Electricity Cost (¢/kWh)'),
            alt.Tooltip('South-facing with vertical (90 degrees) tilt', title='Insolation (kWh/m²)')] 
).project(
    type='transverseMercator',
    rotate=[90, 0, 0]
)

combined_chart = (background + points).configure_view(
        clip=True
    )

altair_chart = (dvc.Vega(id="altair-chart",
                        opt={"renderer": "svg", "actions": False},
                        spec=combined_chart.to_dict()))

## Energy Savings Card
ener_sav_card = dbc.Card(
    id='ener_card',
    children=[
        dbc.CardHeader('Energy Savings', style={"background-color": "steelblue", "color": "white", "font-weight": "bold"}),
        dbc.CardBody(
            [
                html.H5('XXX kWh/year', style={"color": "steelblue"}),
            ],
            style={"padding": "10px"}
        )
    ],
    style={"box-shadow": "0px 2px 4px rgba(0, 0, 0, 0.1)"}
)

## Savings
savings_card = dbc.Card(
    id='sav_card',
    children=[
        dbc.CardHeader('Financial Savings',  style={"background-color": "steelblue", "color": "white", "font-weight": "bold"}), 
        dbc.CardBody(
            [
                html.H5('$XXX /year', style={"color": "steelblue"}),
            ], 
            style={"padding": "10px"})
    ],
    style={"box-shadow": "0px 2px 4px rgba(0, 0, 0, 0.1)"}
)

## panel cost Card
cost_card = dbc.Card(
    id='cost_card', 
    children=[
            dbc.CardHeader('Panel Costs', style={"background-color": "steelblue", "color": "white", "font-weight": "bold"}), 
            dbc.CardBody(
                [
                html.H5('$XXX', style={"color": "steelblue"}),
                ],
                style={"padding": "10px"}
                )
        ], 
        style={"box-shadow": "0px 2px 4px rgba(0, 0, 0, 0.1)"}
)

## Payback period Card
payback_card = dbc.Card(
    id='payback_card', 
    children=[
            dbc.CardHeader('Payback Period', style={"background-color": "steelblue", "color": "white", "font-weight": "bold"}), 
            dbc.CardBody(
                [
                html.H5('X year(s)', style={"color": "steelblue"}),
                ],
                 style={"padding": "10px"}
                )
        ], 
        style={"box-shadow": "0px 2px 4px rgba(0, 0, 0, 0.1)"}
)

## Difference in savings card
diff_sav_card = dbc.Card(
        id="diff_card",
        children=[
            dbc.CardHeader("Difference in Savings", style={"background-color": "steelblue", "color": "white", "font-weight": "bold"}), 
            dbc.CardBody([
                html.H5("$XXX /yr", style={"color": "steelblue"}),
                ],
                 style={"padding": "10px"}
                 )
        ], 
        style={"box-shadow": "0px 2px 4px rgba(0, 0, 0, 0.1)"}
    )


## Price information card
highlight_province = province_dropdown

# Define the conditional formatting rule
price_info_card = dash_table.DataTable(price_df.to_dict('records'), [{"name": i, "id": i} for i in price_df.columns],
    style_table={'height': '300px', 'overflowY': 'visible'}, 
    style_cell={'fontSize': '12px'},
    )

# optimization fuction
roof_width_input = dbc.Row(
    [
        dbc.Col(dbc.Input(id='input-roof-width', type='number', placeholder='Enter width (meters)') ),
    ],
    className='mb-2'
)

roof_length_input = dbc.Row(
    [
        dbc.Col(dbc.Input(id='input-roof-length', type='number', placeholder='Enter length (meters)')),
    ],
    className='mb-2'
)

# Output component for the number of solar panels
output_panel_count = dbc.Row(
    html.Div(id='output-panel-count'),
    className='mt-2', 
)


# SIDE BAR WIDGETS
# Roof Dimensions (for sidebar)
roof_dimensions = dbc.Row(
    [
        dbc.Col(roof_length_input, width=6, style={'margin-right': 0, 'padding-right': 0}), 
        dbc.Col(roof_width_input, width=6, style={'margin-right': 0, 'padding-right': 0})
    ], 
    style={
        'background-color': '#e6e6e6',
        'margin-left': 0, 'margin-right': 0
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
        html.Div("Panel Type"),
        pan_eff_dropdown,
        html.Br(),
        html.Div("Roof Dimensions"),
        roof_dimensions, 
        html.Br(),
        html.Div("Number of Panels"),
        num_pan_slider,
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
        'background-color': '#F9DDB1',
        'padding': 10
    }
)
