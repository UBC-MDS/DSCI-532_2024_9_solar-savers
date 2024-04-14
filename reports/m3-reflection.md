# Milestone 3 - Reflection

### Implementations Done as Planned

The following features have been implemented as planned in our sketch and proposal: Left-side panel, savings values, panel comparison, (discussed in detail in `m2-reflection.md`)

### Implementations Done Differently
- **The Electricity Cost Table:** We decided to take this out. It was taking up quite a bit of space and wasn't adding significant value to the dashboard. Instead, we can provide the user the same information by including the electricity cost on the tooltip for the map, so when they hover over their location they can see the price/kwh. 
- **Panel Efficiency**: we included specific panel options into the panel selection, rather than just ranges of efficiency. This gives the user real options for the types of panels they can choose. It also includes the price of the panel. 

#### Additional Updates since Milestone 2
- **Incorporating the cost of the panels:** now that we included specific panels to choose from, we included two new cards: one, `Panel Cost`, telling the user the total cost for the number of panels they wish to buy, and the other, `Payback Period`, informing the user how many years it will take to breakeven with the savings gained from the solar panels.
- **Roof Dimensions:** This is a new feature that allows the user to enter the size of their roof, to obtain the maximum number of panels they could fit on their roof. 
- **Map Zoom:** Upon selection of the province, the map will zoom in to display the region better. This allows the user to more easily observe their selected location and view corresponding metrics. 
- **Panel Comparison:** We grouped these along the bottom for more clarity. 
- **Formatting:** The main changes included incorporating a sidebar and bottom bar for visual appeal and making it more clear which inputs affect which outputs. We also added colour and spacing between the inputs and outputs.  
- **Region Names:** We fixed the names of the regions of Northwest Territories that were not displaying correctly in the dropdown. 
- modularized our code 

### What is Working Well
- The widgets for the user input on the left side panel are linked up well with our cards. The features like, map zoom, roof dimensions, number of panels, and panel comparison all work as planned. There are no major changes required, aside from formatting enhancements. 

### Corner Cases
- we need to reset the newly added cards and panel comparison, in the case that the user selects everything then reselects a new province.
- we came across a formatting issue: the default map (when no province is selected) appears to have extended whitespace (pushing the bottom panel comparison widgets down). This resolves after selecting a province.

### Fixes for Milestone 4
- Corner cases (above)
- Formatting enhancements