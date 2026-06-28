import folium
import pandas

data = pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

def color_producer(elevation):
        if elevation < 1000:
            return 'green'
        elif 1000 <= elevation < 3000:
            return 'orange'
        else:
            return 'red'

map = folium.Map(location=[lat[0], lon[0]], zoom_start=8, tiles='OpenStreetMap')

fg_loc = folium.FeatureGroup(name='Volcanoes')

for lt, ln, el in zip(lat, lon, elev):
    fg_loc.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=f'Elevation: {el} m', 
                                     fill_color=color_producer(el), colour = 'grey', fill_opacity=0.7))

fg_pop = folium.FeatureGroup(name='Population')

fg_pop.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                                style_function=lambda x: {'fillColor': 'yellow' if x['properties']['POP2005'] < 10000000
                                                          else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                                                          else 'red'}))

map.add_child(fg_loc)
map.add_child(fg_pop)
map.add_child(folium.LayerControl())

map.save('map1.html')