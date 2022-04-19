import folium
import pandas

def elevationColor(elev):
    if elev < 1000:
        return "green"
    elif 1000 <= elev < 3000:
        return "orange"
    else:
        return "red"

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"]) 
elev = list(data["ELEV"])

map = folium.Map(location=[42.347867, -83.179629], zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanos")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup="Elevation: " + str(el) + "m",  fill_color=elevationColor(el), color="grey", fill_opacity=0.9))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
                                                      else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())

map.save("map1.html")