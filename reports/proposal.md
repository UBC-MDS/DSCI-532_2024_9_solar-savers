# Milestone 1 - Dashboard proposal: Solar Savers 

### 1. Motivation and purpose
### 2. Description of the data
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