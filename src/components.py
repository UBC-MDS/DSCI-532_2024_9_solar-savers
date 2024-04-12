from dash import Dash, html, dcc, callback, Output, Input, dash_table
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import pandas as pd
import altair as alt



from .data import alt_data, price_df, gdf_ca, panel_df
from .data import alt_data, price_df, gdf_ca, panel_df


background = alt.Chart(gdf_ca).mark_geoshape(
    fill='lightgray',
    stroke='white'
).project(
    'transverseMercator',
    rotate=[90, 0, 0]
).properties(
    width=500,
    height=400
)

points = alt.Chart(alt_data).mark_circle().encode(
    longitude='longitude:Q', 
    latitude='latitude:Q',
    color=alt.Color('South-facing with vertical (90 degrees) tilt',
                    scale=alt.Scale(scheme="oranges"),
                    legend=alt.Legend(title='Solar Energy (kWh)')),     
    size=alt.value(50),  
    tooltip='Municipality:N',
    )


combined_chart = background + points


# Components
## Title
title = html.H1('Solar Savers',
                style={
                    'backgroundColor': 'orange',
                    # 'text-align': 'center'
                })

## Province & Region Selection Dropdowns
province_dropdown = dcc.Dropdown(id='province_dropdown', options=[{'label': province, 'value': province} for province in alt_data["Province"].unique()], value=None)
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
pan_eff_dropdown = dcc.Dropdown(id='panel_efficiency', options=[{'label': name , 'value': name } for name  in panel_df["name "].unique()], value=None)

## Panel Comparison
pan_com_dropdown = dcc.Dropdown(id='panel_comparison', options=[{'label': name , 'value': name } for name  in panel_df["name "].unique()], value=None, multi=True)

## Difference in savings card
diff_sav_card = dbc.Card(id='diff_card', children=[dbc.CardHeader('Difference in Savings'), dbc.CardBody('$XXX /yr')]),

## Comparison graph
comparison_graph = dvc.Vega(id='bars', spec={})

## Energy Savings Card
ener_sav_card = dbc.Card(id='ener_card', children=[dbc.CardHeader('Energy Savings'), dbc.CardBody('XXX kWh/year')]),

## Savings
savings_card = dbc.Card(id='sav_card', children=[dbc.CardHeader('Savings'), dbc.CardBody('$XXX /year')]),

## panel cost Card
cost_card = dbc.Card(id='cost_card', children=[dbc.CardHeader('Panel Costs'), dbc.CardBody('$XXX')])

## Payback period Card
payback_card = dbc.Card(id='payback_card', children=[dbc.CardHeader('Payback Period'), dbc.CardBody('X year')])

## Price information card
highlight_province = province_dropdown

# Define the conditional formatting rule
price_info_card = dash_table.DataTable(price_df.to_dict('records'), [{"name": i, "id": i} for i in price_df.columns],
    style_table={'height': '300px', 'overflowY': 'visible'}, 
    style_cell={'fontSize': '12px'},
    )