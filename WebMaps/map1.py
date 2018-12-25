import folium
import pandas
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'blue'
    else:
        return 'red'


html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""
map = folium.Map(location=[40.7146, 69], tiles = "Mapbox Bright")
fg = folium.FeatureGroup(name="My Map")

for lt,ln, el, name in zip(lat,lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lt,ln], radius = 6, popup=folium.Popup(iframe), fill_color = color_producer(el), color = 'grey', fill_opacity = 0.7))

fg.add_child(folium.GeoJson(data = open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg)
#map.save("Map1.html")
map.save("Map_html_popup_advanced.html")