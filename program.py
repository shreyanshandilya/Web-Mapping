import folium
import pandas

def colour(k):
    if k<1000:
        return "green"
    elif 1000<=k<3000:
        return "orange"
    else:
        return "red"

a = pandas.read_csv("Volcanoes.txt")
lat = list(a["LAT"])
lon = list(a["LON"])
elev = list(a["ELEV"])
html = """<h4>Volcano information</h4>
Height: %s m
"""
map = folium.Map(location=[38.58,-99.09], zoom_start=8, tiles="Stamen Terrain", icon="red")
fg = folium.FeatureGroup(name="My Map")

for i, j, k in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % k, width = 200, height = 100)
    fg.add_child(folium.CircleMarker(location=[i,j], popup=folium.Popup(iframe), fill_color=colour(k), color="grey", opacity=0.7))
map.add_child(fg)

map.save("Map1.html")
