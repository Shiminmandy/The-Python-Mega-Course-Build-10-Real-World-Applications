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
map1.add_child(fg)
map1.save("Map1.html")  # open in browser , do not open in pycharm
get_data = pandas.read_csv("Volcanoes.txt")
print(get_data)
