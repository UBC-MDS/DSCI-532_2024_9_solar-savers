from dash import callback, Output, Input, State, no_update
import dash_bootstrap_components as dbc
import altair as alt
import pandas as pd

from dash.exceptions import PreventUpdate
from dash import callback_context

from .data import alt_data, price_df, panel_df, gdf_ca

# Callbacks and Reactivity
@callback(
    Output('region_dropdown', 'options'),
    Output('region_dropdown', 'value'),
    Output('altair-chart', 'spec'),
    Input('province_dropdown', 'value'),
    Input('region_dropdown', 'value')

)
def update_region_dropdown(province_dropdown, region_dropdown):
    print("flag")
    region_value = None  
    if province_dropdown is None:
        return [], region_value, get_default_chart()

    filtered_regions = alt_data[alt_data['Province'] == province_dropdown]['Municipality'].unique()
    region_options = [{'label': region, 'value': region} for region in filtered_regions]
    alt_chart_spec = generate_altair_chart(province_dropdown, region_dropdown)

    return region_options, region_dropdown, alt_chart_spec

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


    if panel_comparison and len(panel_comparison) > 2:
        panel_comparison = panel_comparison[:2]  

    if province is not None and region is not None:
        province_price = price_df[(price_df['province'] == province)]["price"].iloc[0] / 100
        filtered_row = alt_data[(alt_data['Province'] == province) & (alt_data['Municipality'] == region) & (alt_data['Month'] == 'Annual')]
        if not filtered_row.empty:
            energy_savings = filtered_row['South-facing with vertical (90 degrees) tilt'].iloc[0] * conversion_rate.get(efficiency, 0) * 1.65 * 365 * num_pan
            card_ener = dbc.Card([dbc.CardHeader('Energy Savings'), dbc.CardBody(f'{energy_savings:.2f} kWh/year')])
            card_sav = dbc.Card([dbc.CardHeader('Savings'), dbc.CardBody(f'${energy_savings * province_price:.2f}/year')])

        if efficiency:
            card_cost = dbc.Card([dbc.CardHeader('Panel Costs'), dbc.CardBody(f'${panel_price.get(efficiency, 0) * num_pan:.0f}')])
            card_payback = dbc.Card([dbc.CardHeader('Payback Period'), dbc.CardBody(f'{panel_price.get(efficiency, 0) * num_pan / (energy_savings * province_price):.2f} years')])

        if panel_comparison is not None and len(panel_comparison) >= 2:
            comparison_values = [conversion_rate[value] for value in panel_comparison]
            comparison_savings = []
            # print(region) # debug This is a bug by DASH
            # print(panel_comparison) # debug 
            # print(province) # debug
            for value in comparison_values:
                comparison_savings.append(filtered_row['South-facing with vertical (90 degrees) tilt'].iloc[0] * value * 1.65 * 365 * num_pan)
            diff = (comparison_savings[0] - comparison_savings[1]) * province_price  
            card_diff = dbc.Card([dbc.CardHeader('Difference in Savings'), dbc.CardBody(f'${diff:.2f}/yr'), dbc.CardFooter(f'{panel_comparison[0]} vs. {panel_comparison[1]}')])

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
    else:
        return create_empty_chart()
    
    if province is not None and region is not None:
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
        
        return create_empty_chart()
    
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
    
@callback(
    Output('num_pan_slider', 'max'),  # Only update the slider's max property
    [
        Input('input-roof-width', 'value'),
        Input('input-roof-length', 'value'),
        Input('panel_efficiency', 'value')
    ],
    [
        State('num_pan_slider', 'max')  # Retrieves the current max value of the slider
    ]
)
def calculate_max_panels(roof_width, roof_length, selected_panel_type, current_max):
    if roof_width is not None and roof_length is not None and selected_panel_type is not None and roof_width > 0 and roof_length > 0:
        panel_length = panel_df[panel_df['name '] == selected_panel_type]['length_m'].iloc[0]
        panel_width = panel_df[panel_df['name '] == selected_panel_type]['width_m'].iloc[0]

        max_fit = max_rectangles_with_residual(roof_width, roof_length, panel_width, panel_length)


        # Update the slider max only if the new calculation differs from the current max
        if max_fit != current_max:
            return max_fit  # Only return the new max value for the slider
        return no_update  # Do not update the slider max if it hasn't changed

    # Return the initial slider max if inputs are not valid
    return current_max  # or `no_update` if you prefer not to reset to a default
# Dropdown button for information
@callback(
    Output("info", "is_open"),
    [Input("info-button", "n_clicks")],
    [State("info", "is_open")],  
)
def toggle_button(n, is_open):
    print(n)  
    print(is_open)  
    if n:
        return not is_open
    return is_open


def get_default_chart():
    """
    Generate a default Altair chart representing solar energy potential across Canadian regions.

    Returns:
        dict: A dictionary representing the Altair chart specification.
    """
    background = alt.Chart(gdf_ca).mark_geoshape(
        fill='lightgray',
        stroke='white'
    ).project(
        type='transverseMercator',
        rotate=[90, 0, 0]
    ).properties(
        width=500,
        height=400,
        title="Solar Energy Potential Across Canadian Regions"
    )

    points = alt.Chart(alt_data).mark_circle().encode(
        longitude='longitude:Q',
        latitude='latitude:Q',
        color=alt.Color(
            'South-facing with vertical (90 degrees) tilt',
            scale=alt.Scale(scheme="oranges"),
            legend=alt.Legend(title='Mean Daily Insolation (kWh/m²)')
        ),
        size=alt.value(50),
        tooltip=[
            alt.Tooltip('Municipality:N', title='Region'),
            alt.Tooltip('price', title='Electricity Cost (¢/kWh)'),
            alt.Tooltip('South-facing with vertical (90 degrees) tilt', title='Insolation (kWh/m²)')
        ]
    ).project(
        type='transverseMercator',
        rotate=[90, 0, 0]
    )

    combined_chart = background + points
    return combined_chart.to_dict()

def generate_altair_chart(province_dropdown, region_dropdown):
    """
    Generate an Altair chart based on selected province and region.

    Args:
        province_dropdown (str or None): Selected province name.
        region_dropdown (str or None): Selected region name.

    Returns:
        dict: A dictionary representing the Altair chart specification.
    """
    if province_dropdown is None:
        return get_default_chart()

    background = alt.Chart(gdf_ca.query(f'name == "{province_dropdown}"')).mark_geoshape(
        fill='lightgray',
        stroke='white'
    ).project(
        type='transverseMercator',
        rotate=[90, 0, 0]
    ).properties(
        width=500,
        height=400,
        title="Solar Energy Potential Across Canadian Regions"
    )

    points = alt.Chart(alt_data.query(f'Province == "{province_dropdown}"')).mark_circle().encode(
        longitude='longitude:Q',
        latitude='latitude:Q',
        color=alt.condition(
            alt.datum.Municipality == region_dropdown,
            alt.value('blue'),
            alt.Color(
                'South-facing with vertical (90 degrees) tilt',
                scale=alt.Scale(scheme="oranges"),
                legend=alt.Legend(title='Mean Daily Insolation (kWh/m²)')
            )
        ),
        size=alt.condition(
            alt.datum.Municipality == region_dropdown,
            alt.value(130),
            alt.value(50)
        ),
        tooltip=[
            alt.Tooltip('Municipality:N', title='Region'),
            alt.Tooltip('price', title='Electricity Cost (¢/kWh)'),
            alt.Tooltip('South-facing with vertical (90 degrees) tilt', title='Insolation (kWh/m²)')
        ]
    ).project(
        type='transverseMercator',
        rotate=[90, 0, 0]
    )

    combined_chart = background + points
    return combined_chart.to_dict()

# Callback to disable options in panel_comparison dropdown
@callback(
    Output('panel_comparison', 'options'),
    Output('panel_comparison', 'value'),
    Input('panel_comparison', 'value'),
    State('panel_comparison', 'options')
)
def toggle_panel_comparison_options(selected_panels, current_options):
    ctx = callback_context
    if not ctx.triggered:
        raise PreventUpdate

    max_panels = 2  

    if not selected_panels:
        updated_options = [
            {**option, 'disabled': False}
            for option in current_options
        ]
        return updated_options, []

    if len(selected_panels) >= max_panels:
        updated_options = [
            {**option, 'disabled': True} if option['value'] not in selected_panels else option
            for option in current_options
        ]
    else:
        updated_options = [
            {**option, 'disabled': False}
            for option in current_options
        ]

    return updated_options, selected_panels

def create_empty_chart():
    """
    Generate an empty Altair chart with specific properties.

    Returns:
        alt.Chart: An Altair chart object representing an empty chart.

    Example Usage:
        chart = create_empty_chart()
        chart.show()  # Display the empty chart
    """
    chart = alt.Chart(pd.DataFrame()).mark_point().encode(
    x=alt.X('empty:Q', axis=None),  
    y=alt.Y('empty:Q', axis=None),  
    ).properties(
    width=500,
    height=70,
    title="Panel Comparison"
) 

    return chart.to_dict()