from dash import callback, Output, Input
import dash_bootstrap_components as dbc
import altair as alt
import pandas as pd

from .data import alt_data, price_df, panel_df, gdf_ca

# Callbacks and Reactivity
@callback(
    Output('region_dropdown', 'options'),
    Output('altair-chart', 'spec'),
    Input('province_dropdown', 'value'),
    Input('region_dropdown', 'value')
)
def update_region_dropdown(province_dropdown, region_dropdown):
    if province_dropdown is None:
        background = alt.Chart(gdf_ca).mark_geoshape(
        fill='lightgray',
        stroke='white'
        ).project(
            type='transverseMercator',
            rotate=[90, 0, 0], 
        ).properties(
            width=500,
            height=400, 
            title = "Solar Energy Potential Across Canadian Regions"
        )
        
        points = alt.Chart(alt_data).mark_circle().encode(
        longitude='longitude:Q', 
        latitude='latitude:Q',
        color=alt.Color('South-facing with vertical (90 degrees) tilt',
                        scale=alt.Scale(scheme="lighttealblue"),
                        legend=alt.Legend(title='Insolation (kWh/m²)')),     
        size=alt.value(50),  
        tooltip=[alt.Tooltip('Municipality:N', title='Region'),
                 alt.Tooltip('price', title='Electricity Cost (¢/kWh)'),
                 alt.Tooltip('South-facing with vertical (90 degrees) tilt', title='Insolation (kWh/m²)')] 
        ).project(
            type='transverseMercator',
            rotate=[90, 0, 0], 
        )
        combined_chart = background + points

        return [], combined_chart.to_dict()
    else:
        filtered_regions = alt_data[alt_data['Province'] == province_dropdown]['Municipality'].unique()
      
        province_zoom = {'British Columbia': {'scale': 1200, 'translate': [660, 1460]}, 
                'Alberta': {'scale': 1680, 'translate': [644, 1876]}, 
                'Saskatchewan':{'scale': 1736, 'translate': [523, 1890]}, 
                'Manitoba':{'scale': 1736, 'translate': [378, 1862]},
                'Ontario':{'scale': 1484, 'translate': [168, 1470]}, 
                'Quebec': {'scale': 1113, 'translate': [10.5, 1260]}, 
                'Northwest Territories': {'scale': 1220, 'translate': [520,1640]}, 
                'Yukon Territory': {'scale': 1240, 'translate': [600, 1720]},
                'Nunavut': {'scale': 880, 'translate':[260, 1320]}, 
                'New Brunswick': {'scale': 1480, 'translate': [-200, 1400]}, 
                'Nova Scotia': {'scale': 1480, 'translate': [-200, 1400]}, 
                'Prince Edward Island': {'scale': 1480, 'translate': [-200, 1400]}, 
                'Newfoundland and Labrador': {'scale': 1160, 'translate': [-140, 1320]}
                }

        scale = province_zoom[province_dropdown]["scale"]
        translate = province_zoom[province_dropdown]["translate"]

        background = alt.Chart(gdf_ca.query(f'name == "{province_dropdown}"')).mark_geoshape(
        fill='lightgray',
        stroke='white'
        ).project(
            type='transverseMercator',
            rotate=[90, 0, 0], 
        ).properties(
            width=500,
            height=400, 
            title = "Solar Energy Potential Across Canadian Regions"
        )

        points = alt.Chart(alt_data.query(f'Province == "{province_dropdown}"')).mark_circle().encode(
        longitude='longitude:Q', 
        latitude='latitude:Q',
        color=alt.condition(
        alt.datum.Municipality == region_dropdown,  # Check if the name matches the dropdown
        alt.value('red'),  # Color for true condition
        alt.Color('South-facing with vertical (90 degrees) tilt',  # Field for false condition
                  scale=alt.Scale(scheme="lighttealblue"),
                  legend=alt.Legend(title='Insolation (kWh/m²)'))
    ),
        size=alt.condition(
        alt.datum.Municipality == region_dropdown,  # Check if the name matches the dropdown
        alt.value(130),  # Color for true condition
        alt.value(50)
    ),
        tooltip=[alt.Tooltip('Municipality:N', title='Region'),
                 alt.Tooltip('price', title='Electricity Cost (¢/kWh)'),
                 alt.Tooltip('South-facing with vertical (90 degrees) tilt', title='Insolation (kWh/m²)')],
        ).project(
            type='transverseMercator',
            rotate=[90, 0, 0], 
        )


        combined_chart = background + points
        return [{'label': region, 'value': region} for region in filtered_regions], combined_chart.to_dict()

@callback(
    Output('ener_card', 'children'),
    Output('sav_card', 'children'),
    Output('cost_card', 'children'),
    Output('payback_card', 'children'),
    Output('diff_card', 'children'),
    Input('province_dropdown', 'value'),
    Input('region_dropdown', 'value'),
    Input('panel_efficiency', 'value'),
    Input('num_pan_slider', 'value'),
    Input('panel_comparison', 'value')
)
def update_savings_cards(province, region, efficiency, num_pan, panel_comparison):
    conversion_rate = {row['name ']: row['efficiency '] for index, row in panel_df.iterrows()}
    panel_price = {row['name ']: row['price '] for index, row in panel_df.iterrows()}

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

    card_cost = [
        dbc.CardHeader('Panel Costs'),
        dbc.CardBody('$XXX')
    ]

    card_payback = [
        dbc.CardHeader('Payback Period'),
        dbc.CardBody('X year')
    ]

    if province and region:
        province_price = price_df[(price_df['province'] == province)]["price"].iloc[0] / 100
        filtered_row = alt_data[(alt_data['Province'] == province) & (alt_data['Municipality'] == region) & (alt_data['Month'] == 'Annual')]
        if not filtered_row.empty:
            energy_savings = filtered_row['South-facing with vertical (90 degrees) tilt'].iloc[0] * conversion_rate.get(efficiency, 0) * 1.65 * 365 * num_pan
            card_ener = dbc.Card([dbc.CardHeader('Energy Savings'), dbc.CardBody(f'{energy_savings:.2f} kWh/year')])
            card_sav = dbc.Card([dbc.CardHeader('Savings'), dbc.CardBody(f'${energy_savings * province_price:.2f}/year')])

            # card_cost = dbc.Card([dbc.CardHeader('Panel Costs'), dbc.CardBody(f'${panel_price.get(efficiency, 0) * num_pan:.0f}')])
            # card_payback = dbc.Card([dbc.CardHeader('Payback Period'), dbc.CardBody(f'{panel_price.get(efficiency, 0) * num_pan / (energy_savings * province_price):.2f} years')])

        if efficiency:
            card_cost = dbc.Card([dbc.CardHeader('Panel Costs'), dbc.CardBody(f'${panel_price.get(efficiency, 0) * num_pan:.0f}')])
            card_payback = dbc.Card([dbc.CardHeader('Payback Period'), dbc.CardBody(f'{panel_price.get(efficiency, 0) * num_pan / (energy_savings * province_price):.2f} years')])

            if panel_comparison and len(panel_comparison) >= 2:
                comparison_values = [conversion_rate[value] for value in panel_comparison]
                comparison_savings = []
                for value in comparison_values:
                    comparison_savings.append(filtered_row['South-facing with vertical (90 degrees) tilt'].iloc[0] * value * 1.65 * 365 * num_pan)
                diff = (comparison_savings[0] - comparison_savings[1]) * province_price  
                card_diff = dbc.Card([dbc.CardHeader('Difference in Savings'), dbc.CardBody(f'${diff:.2f}/yr'), dbc.CardFooter(f'{panel_comparison[0]} vs. {panel_comparison[1]}')])

            return card_ener, card_sav, card_cost, card_payback, card_diff
    return card_ener, card_sav, card_cost, card_payback, card_diff

@callback(
    Output('bars', 'spec'),
    Input('panel_comparison', 'value'),
    Input('province_dropdown', 'value'),
    Input('region_dropdown', 'value'),
    Input('num_pan_slider', 'value'),
)
def create_chart(panel_comparison, province, region, num_pan):
    if panel_comparison:
        conversion_rate = {row['name ']: row['efficiency '] for index, row in panel_df.iterrows()}
        # conversion_rate = {
        #     "Low < 15%": 0.15,
        #     "Standard 15-18%": 0.18,
        #     "High 18-22%": 0.22,
        #     "Premium > 22%": 0.25
        # }
    if province and region:
        province_price = price_df[(price_df['province'] == province)]["price"].iloc[0] / 100
        filtered_row = alt_data[(alt_data['Province'] == province) & (alt_data['Municipality'] == region) & (alt_data['Month'] == 'Annual')]
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
                            y=alt.Y('Panel Comparison', title='Efficiency', sort='-x'),
                            x=alt.X('Savings', title='Savings ($/yr)', stack=None)                            
                        ).properties(
                            title = 'Panel Comparison'
                        ).interactive().to_dict()
                )
    else:
        return {}
    
def max_rectangles_with_residual(a, b, x, y):
    # First orientation
    count_x = a // x
    count_y = b // y
    total_first = count_x * count_y

    # Residual space calculation for first orientation
    residual_a = a - count_x * x
    residual_b = b - count_y * y
    additional_first = (residual_a // y) * count_y + (residual_b // x) * count_x

    # Second orientation (rotated small rectangles)
    count_x_rotated = a // y
    count_y_rotated = b // x
    total_second = count_x_rotated * count_y_rotated

    # Residual space calculation for second orientation
    residual_a_rotated = a - count_x_rotated * y
    residual_b_rotated = b - count_y_rotated * x
    additional_second = (residual_a_rotated // x) * count_y_rotated + (residual_b_rotated // y) * count_x_rotated

    # Sum totals and additional fits
    total_with_residual_first = total_first + additional_first
    total_with_residual_second = total_second + additional_second

    # Return the maximum of the two orientations considering the residual spaces
    return max(total_with_residual_first, total_with_residual_second)
    
panel_df['length_m'] = panel_df['length (mm) '] / 1000
panel_df['width_m'] = panel_df['width (mm)'] / 1000

# Assume that your CSV has a single type of panel, otherwise, you'll need to handle multiple types.
panel_length = panel_df['length_m'].iloc[0]
panel_width = panel_df['width_m'].iloc[0]

@callback(
    Output('output-panel-count', 'children'),
    [Input('input-roof-width', 'value'),
     Input('input-roof-length', 'value')]
)
def calculate_max_panels(roof_width, roof_length):
    if roof_width is not None and roof_length is not None and roof_width > 0 and roof_length > 0:
        max_fit = max_rectangles_with_residual(roof_width, roof_length, panel_width, panel_length)
        return f'Maximum panels for your roof: {max_fit}'
    return 'Maximum panels for your roof:'