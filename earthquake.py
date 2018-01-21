# this is for visualizing earthquakes occured
# around the world in one day.

import pandas
import folium

data = pandas.read_csv("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.csv")
map = folium.Map(location=[28.6248139,77.1082734], zoom_start=6)

lat = list(data["latitude"])
lon = list(data["longitude"])
place = list(data["place"])
mag = list(data["mag"])
time = list(data["time"])

fgs = folium.FeatureGroup(name="smallEarthquakes")
fgm = folium.FeatureGroup(name="mediumEarthquakes")
fgb = folium.FeatureGroup(name="bigEarthquakes")

for lat,lon,place,mag,time in zip(lat,lon,place,mag,time):
    if mag < 3:
        fgs.add_child(folium.CircleMarker(
        location=[lat,lon], fill= True, radius=6, fill_opacity=0.7 ,
        popup=folium.Popup(place+" "+str(mag)+" "+str(time).replace("T"," ").replace("Z"," "),parse_html=True), fill_color="blue", color="grey"))

        map.add_child(fgs)
    elif 3 <= mag < 5:
         fgm.add_child(folium.CircleMarker(
         location=[lat,lon], fill= True, radius=6, fill_opacity=0.7 ,
         popup=folium.Popup(place+" "+str(mag)+" "+str(time).replace("T"," ").replace("Z"," "),parse_html=True), fill_color="yellow", color="grey"))

         map.add_child(fgm)
    elif mag >= 5:
         fgb.add_child(folium.CircleMarker(
         location=[lat,lon], fill= True, radius=6, fill_opacity=0.7 ,
         popup=folium.Popup(place+" "+str(mag)+" "+str(time).replace("T"," ").replace("Z"," "),parse_html=True), fill_color="red", color="grey"))

         map.add_child(fgb)
map.add_child(folium.LayerControl())
map.save("EarthquakeVisualizer.html")
print("map saved.")
