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
    max_power_drone1 = None
    max_power_drone2 = None
    max_power_drone3 = None
    max_power_center1 = None
    max_power_center2 = None
    max_power_center3 = None
    center = None
    MAP = None
    point = {}
    for row in posreader:

        if center == None:
            center = [float(row[0]),float(row[1])]
            MAP = folium.Map(location = list(center), zoom_start = 200)
        
        else:
            
            if row[3] == '1':
                if max_power_drone1 == None:
                    max_power_drone1 = float(row[2])
        
                if max_power_center1 == None:
                    max_power_center1 = [float(row[0]),float(row[1])] 
        
                if max_power_drone1 < float(row[2]):
                    max_power_drone1 = float(row[2])
                    max_power_center1 = [float(row[0]),float(row[1])]

            if row[3] == '2':
                if max_power_drone2 == None:
                    max_power_drone2 = float(row[2])
        
                if max_power_center2 == None:
                    max_power_center2 = [float(row[0]),float(row[1])] 
        
                if max_power_drone2 < float(row[2]):
                    max_power_drone2 = float(row[2])
                    max_power_center2 = [float(row[0]),float(row[1])]

            if row[3] == '3':
                if max_power_drone3 == None:
                    max_power_drone3 = float(row[2])
        
                if max_power_center3 == None:
                    max_power_center3 = [float(row[0]),float(row[1])] 
        
                if max_power_drone3 < float(row[2]):
                    max_power_drone3 = float(row[2])
                    max_power_center3 = [float(row[0]),float(row[1])]
        
        point = (float(row[0]),float(row[1]))
            
        folium.Marker(point).add_to(MAP)

folium.Circle(location = center,
                    radius = 10,
                    color = '#fd3300',
                    fill = True,
                    fill_color = '#fd3300').add_to(MAP)

folium.Circle(location = max_power_center1,
                    radius = 15,
                    color = '#8db100',
                    fill = True,
                    fill_color = '#8db100').add_to(MAP)

folium.Circle(location = max_power_center2,
                    radius = 15,
                    color = '#8db100',
                    fill = True,
                    fill_color = '#8db100').add_to(MAP)

folium.Circle(location = max_power_center3,
                    radius = 15,
                    color = '#8db100',
                    fill = True,
                    fill_color = '#8db100').add_to(MAP)

MAP.save('interference_localization_3drones.html')
