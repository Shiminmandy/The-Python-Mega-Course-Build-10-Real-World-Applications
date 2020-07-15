# -*- coding:utf-8 -*-
# @Description
# @Author: Shimin
# @Copyright
# @Version:0.0.1
import folium
import pandas

map1 = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name='My Map')
fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
# add multiple points
fg.add_child(folium.Marker(location=[35.2, -90.1], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
# map1.add_child(fg)
# map1.save("Map1.html")  # open in browser , do not open in pycharm
# adding points from files/use for loop
get_data = pandas.read_csv("Volcanoes.txt")
print(get_data)
print(type(get_data))       # <class 'pandas.core.frame.DataFrame'>
print(get_data.columns)
"""
Index(['VOLCANX020', 'NUMBER', 'NAME', 'LOCATION', 'STATUS', 'ELEV', 'TYPE',
       'TIMEFRAME', 'LAT', 'LON'],
      dtype='object')
"""
lat = list(get_data["LAT"])
# print(lat)   get a list of lat
lon = list(get_data["LON"])
for lt, ln in zip(lat, lon):    # for a, b in zip([1,2,3],[4,5,6]), print(a,b) will get 1 4/2 5/ 3 6
    fg.add_child(folium.Marker(location=[lt, ln], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
map1.add_child(fg)
map1.save("Map1.html")