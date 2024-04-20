# Milestone 4 - Reflection

### Implementations Done as Planned

The following features have been implemented as planned in our sketch and proposal: 
- Added a new feature to zoom into the selected province and highlight the selected region in blue.
- Updated the maximum slider value to reflect the number of panels that fit the roof dimensions.
- Updated the overall color theme to orange.
- Fixed region names with accented characters.
- Rearranged layout.
- Limited panel comparison to two types of panels.

### Implementations Done Differently
 - We have removed the text showing the maximum number of panels that can fit onto a roof of specified dimensions. This value is now shown at the maximum of the slider bar to avoid confusion.
 - A "Learn More" button has been added to provide extra guidance to users when needed.

### What is Working Well
 - The app is running significantly faster on render.com, thanks to our efforts to improve performance, such as loading only the relevant data points from the dataset instead of filtering the entire map. Caching and switching to a binary data file also helped.
 - The colour theme is attractive and provide a clear segmentation of different sections.
 - There are no apparent bugs and errors.

### Limitations
- Users are unable to specify the tilt and orientation of solar panels. Although this would be a useful feature, we cannot implement it due to the extensive technical expertise required in geometry and physics.
- Some smaller regions might not be included in the app due to a lack of data.

### What could have done differently
- We could have decided on the features before finalizing the layout, as it is time-consuming to adjust the layout after adding or removing features.

- Some features were removed because we do not think they are informative to users. This could have been prevented and development time saved if we had discussed more thoroughly in advance.
