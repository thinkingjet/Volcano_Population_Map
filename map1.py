import folium
import pandas

data = pandas.read_csv("10_Real_World_Apps/2_Volcano_Population_Map/Webmap_datasources/Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])

def colour_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<=elevation<3000:
        return 'orange'
    else:
        return 'red' 

map = folium.Map(location=[28.7041, 77.1025], zoom_start=5, min_zoom=2, max_bounds=True, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt,ln,elv in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=str(elv)+" m", 
    fill_color=colour_producer(elv), color="grey", fill_opacity=0.7, fill=True))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open("10_Real_World_Apps/2_Volcano_Population_Map/Webmap_datasources/world.json", 'r', encoding='utf-8-sig').read()
, style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'yellow' if 10000000<=x['properties']['POP2005'] < 2000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("10_Real_World_Apps/2_Volcano_Population_Map/Map1.html")






