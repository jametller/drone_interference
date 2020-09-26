import csv
import matplotlib.pyplot as plt
from geopy.distance import geodesic

def process_file (filename):
    # key distance, value rssi
    data = {}
    with open(filename) as csvfile:
        posreader = csv.reader(csvfile, delimiter=',')
        firstrow = None
        for row in posreader:
            if firstrow == None:
                firstrow = (float(row[0]),float(row[1]))
            geo = geodesic(firstrow, (float(row[0]),float(row[1]))).meters
            print(str(firstrow) + " " + str(row) + " " + str(int(row[2])) + " " + str(geo))
            data[int(row[2])] = float(geo)
        return data

def add_dataset (data):
    names = list(data.keys())
    values = list(data.values())
    plt.plot(names,values)
data = process_file('NER1-26-09-2020.csv')
add_dataset(data)
data = process_file('NER2-26-09-2020.csv')
add_dataset(data)
#data = process_file('NER3-26-09-2020.csv')
#add_dataset(data)
plt.show()
