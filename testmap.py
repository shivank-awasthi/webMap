# this is all about generating a basic map of any
# random location in the world through python in html.

import folium
import pandas
d = pandas.read_csv("Volcanoes_USA.csv")
map = folium.Map(location=[28.6248139,77.1082734])
lat = list(d["LAT"])
lon = list(d["LON"])
ele = list(d["ELEV"])
name = list(d["NAME"])
fg = folium.FeatureGroup(name="liveVolcanoes")
fg1 = folium.FeatureGroup(name="GeoJson Data")
fg1.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'red'}))
for lat, lon, name, el in zip(lat,lon,name,ele):
    if el > 2000:
        stri = '#ff0000'
    elif el > 1000:
        stri = '#00ff00'
    else:
        stri = '#0000ff'
    fg.add_child(folium.CircleMarker(location=[lat,lon], fill= True, radius=6, fill_opacity=0.7 ,popup=folium.Popup(name+" "+str(el),parse_html=True), fill_color=stri, color="grey"))

map.add_child(fg)
map.add_child(fg1)
map.add_child(folium.LayerControl())
map.save("testmap1.html")
print(map)
print("map saved!")
