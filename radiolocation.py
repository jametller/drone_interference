#!/usr/bin/python3

import csv
import folium
import numpy as np
import sys
from geopy.distance import geodesic

data_file = sys.argv[1]
print(str(data_file))
with open(data_file) as csvfile:
    posreader = csv.reader(csvfile, delimiter=',')
    max_power = None
    max_power_center = None
    center = None
    MAP = None
    point = {}
    for row in posreader:



        if center == None:
            center = [float(row[0]),float(row[1])]
            MAP = folium.Map(location = list(center), zoom_start = 200)
        
        else:

            if max_power == None:
                max_power = float(row[2])
        
            if max_power_center == None:
                max_power_center = [float(row[0]),float(row[1])] 
        
            if max_power < float(row[2]):
                max_power = float(row[2])
                max_power_center = [float(row[0]),float(row[1])]
        
        print(str(max_power))
        print(str(max_power_center))
        point = (float(row[0]),float(row[1]))
            
        folium.Marker(point).add_to(MAP)

folium.Circle(location = center,
                    radius = 10,
                    color = '#fd3300',
                    fill = True,
                    fill_color = '#fd3300').add_to(MAP)

folium.Circle(location = max_power_center,
                    radius = 10,
                    color = '#8db100',
                    fill = True,
                    fill_color = '#8db100').add_to(MAP)

MAP.save('interference_localization.html')
