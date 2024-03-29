# Milestone 1 - Dashboard proposal: Solar Savers 

### 1. Motivation and purpose
### 2. Description of the data

We will be analyzing 2 datasets: pricePerProvince.csv and municip_kWh.csv. 

The first dataset (13 rows, 2 columns) contains the average total cost of electricity (`price per ¢/kWh`) by Canadian province (`province`), based on a monthly consumption of 1,000 kWh in 2023 (https://www.energyhub.org/electricity-prices/). 


The second dataset (45578 rows, 9 columns) contains the `Mean daily global insolation (kWh/m2)` measurements at different tilts (`South-facing with vertical (90 degrees) tilt`, `South-facing with latitude tilt`, `South-facing with tilt=latitude+15 degrees`, `South-facing with tilt=latitude-15 degrees`, `2-axis tracking`, `Horizontal (0 degree)`) of 3506 municipalities (`Municipality`) across all provinces of Canada (`Province`) for each month (`Month`) as well as for the year (same column contains it).  

Using this data, we would derive new variables such as the monetary value of the potential electricity generated from solar panels with a certain tilt, a certain location, and conversion rate (`potential_generated_value`), as it would be crucial for Tom to explore how much money he could save by installing solar panels either at his current location or elsewhere.

###  3. Research questions
### 4. App sketch and description

**App Sketch**
![Sketch](/img/sketch.png)

**Description** 

This app displays an interactive map of Canada along with relevant metrics to assist in informed decision-making for purchasing solar panels. The features are outlined below. 
- **Map of Canada**: The map will be colored by *mean daily global insolation (kWh/m<sup>2</sup>)*. The corresponding legend with an `info` button provides an explanation of the meaning of this measure. The map includes a tooltip feature that reveals detailed information upon hovering over a location. This includes the region name, electricity cost ($/kWh), and precise values for the mean daily global insolation.
- **Left Side-panel**: This allows the user to input their location, the number of panels (with a slider), the level of panel efficiency (low, standard, high and premium) and an optional input for solar panel comparison. Based on these inputs the graphs along the bottom will adjust. 
- **Savings Values:** The bottom right corner includes the the amount of electricity (kWh/yr) and money ($/yr) saved. These values are based on the user's selection of panel efficiency and number of panels. 
- **Panel comparsion**: Optionally, the user can specify multiple types of panels to compare. The amount of savings will be displayed as the net difference (\$/yr) between the panels, along with a bar chart for the savings (\$/yr) for each specified panel type.
- **Electricity Cost**: This summary table on the right side includes the cost of electricity ($/kWh) by province. Based on the user input, the province selected will be highlighted. 