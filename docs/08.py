# -*- coding:utf-8 -*-
# @Description
# @Author: Shimin
# @Copyright
# @Version:0.0.1
import folium
import pandas

map1 = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
fgv = folium.FeatureGroup(name='Volcanoes')
fgv.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
# add multiple points
fgv.add_child(folium.Marker(location=[35.2, -90.1], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
# map1.add_child(fg)
# map1.save("Map1.html")  # open in browser , do not open in pycharm
# adding points from files/use for loop
get_data = pandas.read_csv("Volcanoes.txt")
print(get_data)
print(type(get_data))  # <class 'pandas.core.frame.DataFrame'>
print(get_data.columns)
"""
Index(['VOLCANX020', 'NUMBER', 'NAME', 'LOCATION', 'STATUS', 'ELEV', 'TYPE',
       'TIMEFRAME', 'LAT', 'LON'],
      dtype='object')
"""
lat = list(get_data["LAT"])
# print(lat)   get a list of lat
lon = list(get_data["LON"])
# for lt, ln in zip(lat, lon):    # for a, b in zip([1,2,3],[4,5,6]), print(a,b) will get 1 4/2 5/ 3 6
#     fg.add_child(folium.Marker(location=[lt, ln], popup="Hi I am a Marker", icon=folium.Icon(color='green')))

# popup elevation and name from the file
elev = list(get_data["ELEV"])
name = list(get_data["NAME"])


# make different colors to points
def color_producer(elevation):  # the parameter name is what ever you want
    if elevation < 1000:
        return 'green'
    elif 1000 < elevation < 3000:
        return 'orange'
    else:
        return 'red'


for lt, ln, el, name in zip(lat, lon, elev, name):  # for a, b in zip([1,2,3],[4,5,6]), print(a,b) will get 1 4/2 5/ 3 6
    # fg.add_child(folium.Marker(location=[lt, ln], radius=10, popup=name + '\t' + str(el) + 'm', icon=folium.Icon(
    # color=color_producer(el))))
    # change marker to circle
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=10, popup=name + '\t' + str(el) + 'm',
                                     fill_color=color_producer(el), color='gray', fill_opacity=0.7))
# adding a GeoJson Polygon layer
# fgp.add_child(folium.GeoJson(data=(open('file/world.json', 'r', encoding='utf-8-sig').read())))
fgp = folium.FeatureGroup(name='Population')
fgp.add_child(folium.GeoJson(data=open('file/world.json', 'r', encoding='utf-8-sig').read(),  # don't missing .read()
                            style_function=lambda x: {'fillColor': 'yellow' if x['properties']['POP2005'] < 10000000
                            else 'green' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
print(type(el))  # <class 'float'> we need to change to string format in popup window

map1.add_child(fgv)
map1.add_child(fgp)
map1.add_child(folium.LayerControl())
map1.save("Map1.html")
print(dir(folium))
# help(folium.CircleMarker)
