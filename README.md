# Web-Mapping
In this project, there is a file containing majorly the list of volcanoes in the United States.
It consists of their latitudes, longitudes, location and height of the volcanoes.
My task was to plot these locations on a world map and then selectively identify various volcanoes.
The criteria for classification was:
height < 1000 -> colour : green;
1000 <= height <= 3000 -> colour : orange;
else :
colour -> red;
On clicking the various locations, the volcano height gets displayed.
Techstack Used:
Python, Libraries : Folium(to plot on the world map) and Pandas(to use data from a csv file).
