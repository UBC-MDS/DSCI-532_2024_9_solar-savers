# Milestone 2 - Reflection

### Implementations Done as Planned

The following features have been implemented as planned in our sketch and proposal: 
- **Left-side Panel**: This includes the drop down for province, region, and panel efficiency; a slider for the number of panels; and an optional drop down for the panel comparison.
- **Savings Values**: This includes the cards for the amount of electricity (kWh/yr) and money ($/yr) saved. 
- **Panel Comparison**: This includes the card for the difference between the top two selected efficiencies and the corresponding bar chart.
- **Electricity Cost Table**: This is the summary table of the cost for electricity by province.

### Implementations Done Differently

- **Map of Canada**: We have this partially implemented as planned. The map is showing with a tool tip providing the region name. Choosing and implementing the best method to use to convert the latitude and longitude data into a map took time to figure out. We will need to colour this map by insolation and add in the corresponding legend. The legend will include a help button to explain insolation. Once doing so we can add in the insolation values on the map tool tip, as well.

### What is Working Well
- The widgets for the user input on the left side panel are linked up well with our cards. The overall layout and the features implemented is quite aligned with our original plans.

### Current Limitations and Future Improvements

- We will update the map as described above. Right now the plotted points on the map are too densely packed in certain areas. This goes against best practices from 531. As we further develop the map we will take this into account. 
- The electricity cost table is static. We will highlight the row based on the selected province. This will allow the user to see where their province ranks more easily.  
- We may move the panel comparison widget, difference in savings card and the bar chart to the right bottom corner. This way the user can easily identify these features as a standalone part of the dashboard. We are going to brainstorm some other options too, before implementing this.  
- Updating the colour theme, fonts and making the titles stand out, will improve the overall visual appeal of the dashboard. 
- **Bugs to fix:** 
    1. We recently discovered that there are a couple regions, upon selection, that cause an error in the dashboard. We will look deeper into the data on why that is. 
    2. There are some regions in the Northwest Territories that contain letters not part of the standard English alphabet, like "Behchokǫ̀", which is currently displaying in the drop down as "Benchok??". 


 