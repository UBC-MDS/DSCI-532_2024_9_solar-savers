from dash import callback, Output, Input
import dash_bootstrap_components as dbc
import altair as alt
import pandas as pd


from data import alt_data, price_df

# Callbacks and Reactivity
@callback(
    Output('region_dropdown', 'options'),
    Input('province_dropdown', 'value')
)
def update_region_dropdown(province_dropdown):
    if province_dropdown is None:
        return []
    else:
        filtered_regions = alt_data[alt_data['Province'] == province_dropdown]['Municipality'].unique()
        return [{'label': region, 'value': region} for region in filtered_regions]

@callback(
    Output('ener_card', 'children'),
    Output('sav_card', 'children'),
    Output('diff_card', 'children'),
    Input('province_dropdown', 'value'),
    Input('region_dropdown', 'value'),
    Input('panel_efficiency', 'value'),
    Input('num_pan_slider', 'value'),
    Input('panel_comparison', 'value')
)
def update_savings_cards(province, region, efficiency, num_pan, panel_comparison):
    conversion_rate = {
        "Low < 15%": 0.15,
        "Standard 15-18%": 0.18,
        "High 18-22%": 0.22,
        "Premium > 22%": 0.25
    }
 
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
 
    if province and region:
        province_price = price_df[(price_df['province'] == province)]["price per ¢/kWh"].iloc[0] / 100
        filtered_row = alt_data[(alt_data['Province'] == province) & (alt_data['Municipality'] == region) & (alt_data['Month'] == 'Annual')]
        if not filtered_row.empty:
            energy_savings = filtered_row['South-facing with vertical (90 degrees) tilt'].iloc[0] * conversion_rate.get(efficiency, 0) * 1.65 * 365 * num_pan
            card_ener = dbc.Card([dbc.CardHeader('Energy Savings'), dbc.CardBody(f'{energy_savings:.2f} kWh/yr')])
            card_sav = dbc.Card([dbc.CardHeader('Savings'), dbc.CardBody(f'${energy_savings * province_price:.2f}/yr')])

            if panel_comparison and len(panel_comparison) >= 2:
                comparison_values = [conversion_rate[value] for value in panel_comparison]
                comparison_savings = []
                for value in comparison_values:
                    comparison_savings.append(filtered_row['South-facing with vertical (90 degrees) tilt'].iloc[0] * value * 1.65 * 365 * num_pan)
                diff = (comparison_savings[0] - comparison_savings[1]) * province_price  
                card_diff = dbc.Card([dbc.CardHeader('Difference in Savings'), dbc.CardBody(f'${diff:.2f}/yr'), dbc.CardFooter(f'{panel_comparison[0]} vs. {panel_comparison[1]}')])


            return card_ener, card_sav, card_diff
    return card_ener, card_sav, card_diff

@callback(
    Output('bars', 'spec'),
    Input('panel_comparison', 'value'),
    Input('province_dropdown', 'value'),
    Input('region_dropdown', 'value'),
    Input('num_pan_slider', 'value'),
)
def create_chart(panel_comparison, province, region, num_pan):
    if panel_comparison:
        conversion_rate = {
            "Low < 15%": 0.15,
            "Standard 15-18%": 0.18,
            "High 18-22%": 0.22,
            "Premium > 22%": 0.25
        }

    if province and region:
        province_price = price_df[(price_df['province'] == province)]["price per ¢/kWh"].iloc[0] / 100
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