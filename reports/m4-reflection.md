# Milestone 4 - Reflection

### Implementations for Milestone 4

The following features have been implemented since the last release: 
- Added a new feature to zoom into the selected province and highlight the selected region in blue.
- Updated the maximum slider value to reflect the number of panels that fit the roof dimensions.
- Updated the overall color theme to orange.
- Fixed region names with accented characters.
- Rearranged layout.
- Limited panel comparison to two types of panels.
- Binary formatting. 
- Moved data wrangling to the data process folder. 
- Include more info in the map tooltip.

### Implementations Done Differently

One thing we incorporated that was not on the original sketch is the max_panel function. The function calculates the maximum amount of panels that can fit into a given dimension of the users’ roof; the function will create different outputs depending on roof size and panel size. We believe that this is helpful for our target users because it is quick and the function considers different ways to place the panels. 

Another additional implementation is the inclusion of panel cost and payback period. The original idea only consisted of savings and energy savings, however, we came to realize that the amount customers spend on these panels is just as important as the amount that they save. By having a payback period, we attempted to balance out the gap between the cost and the savings and make it more understandable for the users. 

In our current dashboard, we also removed the energy cost chart. This is because we believe that the energy prices of other provinces will not be a determining factor for users to decide whether to purchase a panel or not. 

We also implemented a “Learn More” button to provide more context on the dashboard. 


### What is Working Well

 - The app is running significantly faster on render.com, thanks to our efforts to improve performance, such as loading only the relevant data points from the dataset instead of filtering the entire map. Caching and switching to a binary data file also helped.
 - The color theme is attractive and provides a clear segmentation of different sections.
 - There are no apparent bugs and errors.

### Limitations

- Users are unable to specify the tilt and orientation of solar panels. Although this would be a useful feature, we cannot implement it due to the extensive technical expertise required in geometry and physics.
- Some smaller regions might not be included in the app due to a lack of data.

### What could have done differently

- We could have decided on the features before finalizing the layout, as it is time-consuming to adjust the layout after adding or removing features.
- Some features were removed because we do not think they are informative to users. This could have been prevented and development time saved if we had discussed it more thoroughly in advance.
