import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import geopy.distance as gpy

input_latitude = 52.2018
input_longitude = 0.1144
input_coordinates = [input_latitude,input_longitude]
convolution_matrix = [[1,1,1],[1,1,1],[1,1,1]]
data = pd.read_csv("2019-08-cambridgeshire-street.csv",None)
crime = data['Crime type'].values
crime_types = np.unique(crime)
crime_weighting = [1 for i in range(len(crime_types)-1)]
crime_dictionary = dict(zip(crime_types,crime_weighting))
print(crime_dictionary)
crime_latitude = data['Latitude'].values
crime_longitude = data['Longitude'].values
coords_1 = (52.2018, 0.1144)
coords_2 = (52.2018, 0.1144)
for i in range(len(crime_latitude)):
    if
print(gpy.distance(coords_1, coords_2).miles)