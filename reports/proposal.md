# Milestone 1 - Dashboard proposal: Solar Savers 

### 1. Motivation and purpose

The installation of a household solar energy system can be complicated for interested house owners. If we can visualize the potential savings of solar panels according to location and size according to different individuals, we can potentially motivate the house owners more for installation.

To clearly communicate the benefits of these panels, we will use two data sets. We will use the mean daily electricity production of different locations in Canada using a standard solar panel (efficiency = 20%.) Then we will combine it with the electricity price of each province, to calculate how much monetary value of electricity each square meter of solar panel is able to generate daily. Then we will convert the value to annual saving and allow the users to choose the size of their installation.

### 2. Description of the data

We will be analyzing 2 datasets: [pricePerProvince.csv](https://www.energyhub.org/electricity-prices/) and [municip_kWh.csv](https://open.canada.ca/data/en/dataset/8b434ac7-aedb-4698-90df-ba77424a551f/resource/b4b8ede1-512c-4e6f-92af-d0ff38cf4de5). 

The first dataset (13 rows, 2 columns) contains the average total cost of electricity (`price per ¢/kWh`) by Canadian province (`province`), based on a monthly consumption of 1,000 kWh in 2023.

The second dataset (45578 rows, 9 columns) contains the `Mean daily global insolation (kWh/m2)` measurements at different tilts (`South-facing with vertical (90 degrees) tilt`, `South-facing with latitude tilt`, `South-facing with tilt=latitude+15 degrees`, `South-facing with tilt=latitude-15 degrees`, `2-axis tracking`, `Horizontal (0 degree)`) of 3506 municipalities (`Municipality`) across all provinces of Canada (`Province`) for each month (`Month`) as well as for the year (same column contains it).

Using this data, we would derive new variables such as the monetary value of the potential electricity generated from solar panels with a certain tilt, a certain location, and conversion rate (`potential_generated_value`), as it would be crucial for Tom to explore how much money he could save by installing solar panels either at his current location or elsewhere.

### 3. Research questions

Tom is a resident of North Vancouver contemplating the installation of solar panels to economize on electricity costs. He faces uncertainty about the annual savings he might achieve, given the variability in sunlight exposure at his residence.  
  
Utilizing the "Solar Saver app," Tom is empowered to select his geographic location within Canada and adjust the efficiency settings of the solar panels through a slider, enabling a tailored solution to his needs. The application then provides an estimate of the annual average electricity savings (expressed in $kWh/m^2$), alongside detailed information on local electricity pricing and potential savings. This comprehensive data aids Tom in making an informed decision.  
  
From his research via the app, Tom ascertains that in North Vancouver, it's feasible to generate 3600 kW of electricity per square meter annually. By deploying two solar panels, each with dimensions of 0.5m by 1m, he stands to conserve 1200 kW of electricity each year, translating to savings of $800. Encouraged by these findings, he decided it was a good idea to install the solar panels and proceeded accordingly.

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