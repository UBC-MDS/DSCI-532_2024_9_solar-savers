from dash import Dash, html, dcc, callback, Output, Input, dash_table
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import pandas as pd
import altair as alt

from .data import alt_data, price_df, gdf_ca, panel_df

# Components

## Province & Region Selection Dropdowns
province_dropdown = dcc.Dropdown(id='province_dropdown', 
                                 options=[{'label': province, 'value': province} for province in alt_data["Province"].unique()], 
                                 value=None, 
                                 placeholder='Select Province or Territory...')
region_dropdown = dcc.Dropdown(id='region_dropdown', options=[], 
                               value=None, 
                               placeholder='Select Region...')

## Number of Panels
# num_pan_slider = dcc.Slider(id='num_pan_slider',
#                             min=0,
#                             max=20,
#                             step=1,
#                             value=5,
#                             marks={0: '0', 20: '20'},
#                             tooltip={'always_visible': True,
#                                       'placement': 'top'}, 
#                             style = {'background-color': '#f8f9fa'}                
#                             )

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
    style={'background-color': 'white', 'margin-top': '10px'}
)

## Panel Efficiency
pan_eff_dropdown = dcc.Dropdown(id='panel_efficiency', options=[{'label': name , 'value': name } for name  in panel_df["name "].unique()], value=None)

## Panel Comparison
pan_com_dropdown = dcc.Dropdown(id='panel_comparison', options=[{'label': name , 'value': name } for name  in panel_df["name "].unique()], value=None, multi=True)

## Difference in savings card
diff_sav_card = dbc.Card(id='diff_card', children=[dbc.CardHeader('Difference in Savings'), dbc.CardBody('$XXX /yr')]),

## Comparison graph
comparison_graph = dvc.Vega(id='bars', spec={})

## Altair Chart
background = alt.Chart(gdf_ca).mark_geoshape(
    fill='lightgray',
    stroke='white'
).project(
    type = 'transverseMercator',
    rotate=[90, 0, 0]
    # scale = scale, 
    # translate=translate
).properties(
    width=500,
    height=400
)

points = alt.Chart(alt_data).mark_circle().encode(
    longitude='longitude:Q', 
    latitude='latitude:Q',
    color=alt.Color('South-facing with vertical (90 degrees) tilt',
                    scale=alt.Scale(scheme="lighttealblue"),
                    legend=alt.Legend(title='Solar Energy (kWh)')),     
    size=alt.value(50),  
    tooltip='Municipality:N',
    ).project(
        type = 'transverseMercator',
        rotate=[90, 0, 0]
        # scale = scale, 
        # translate=translate
    )

combined_chart = (background + points).configure_view(
        clip=True
    )

altair_chart = (dvc.Vega(id="altair-chart",
                        opt={"renderer": "svg", "actions": False},
                        spec=combined_chart.to_dict()))

## Energy Savings Card
#ener_sav_card = dbc.Card(id='ener_card', children=[dbc.CardHeader('Energy Savings'), dbc.CardBody('XXX kWh/year')]),

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
#savings_card = dbc.Card(id='sav_card', children=[dbc.CardHeader('Financial Savings'), dbc.CardBody('$XXX /year')]),

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
#payback_card = dbc.Card(id='payback_card', children=[dbc.CardHeader('Payback Period'), dbc.CardBody('X year')])
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
        #dbc.Col(html.Div("Width:"), width=4),
        dbc.Col(dbc.Input(id='input-roof-width', type='number', placeholder='Enter width (meters)') ),
    ],
    className='mb-2'
)

roof_length_input = dbc.Row(
    [
        #dbc.Col(html.Div("Length:"), width=4),
        dbc.Col(dbc.Input(id='input-roof-length', type='number', placeholder='Enter length (meters)')),
    ],
    className='mb-2'
)

# Output component for the number of solar panels
output_panel_count = dbc.Row(
    html.Div(id='output-panel-count'),
    className='mt-2', 
)