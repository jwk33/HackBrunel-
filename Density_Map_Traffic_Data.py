import numpy as np
import sys
import pandas
import geocoder
import geopy.distance as gpy
from scipy import signal
import matplotlib.pyplot as plt
import math
year_month = '2019-07'
kernel = np.ones((100,100))/10000
g = geocoder.ipinfo('me')
input_latitude = 51.87768652
input_longitude = -5.171686
input_coordinates = [input_latitude,input_longitude]
np.set_printoptions(threshold=sys.maxsize)
print(g.latlng)
f = 0.0714
print(gpy.distance(input_coordinates, (input_latitude, input_longitude + f)).miles)

def traffic_accident_filter(input_latitude, input_longitude):
    data = pandas.read_csv('dftRoadSafetyData_Accidents_2018.csv')
    latitude = data.Latitude.to_list()
    longitude = data.Longitude.to_list()
    severity = data.Accident_Severity.to_list()
    accident_latitude = []
    accident_longitude = []
    accident_severity = []
    accident_coordinates = []
    for i in range(len(latitude)-1):
        if math.isnan(latitude[i]) != True:
            if math.isnan(longitude[i]) != True:
                if gpy.distance((input_latitude,input_longitude), (latitude[i], longitude[i])).miles < 4.243:
                    accident_latitude.append(round(float(latitude[i]),4))
                    accident_longitude.append(round(float(longitude[i]),4))
                    accident_severity.append(severity[i])
                    accident_coordinates.append((round(float(longitude[i]),4),round(float(latitude[i]),4)))
    coordinate_accidentseverity_dict = dict(zip(accident_coordinates,accident_severity))
    return accident_latitude, accident_longitude,accident_severity,  coordinate_accidentseverity_dict,accident_coordinates

def accident_density_mapg():
    alat, alon, asev, caccsevdict, acc = traffic_accident_filter(input_latitude,input_longitude)
    f1 = 0.0435
    f = 0.0714
    coordinate_meshgrid = np.zeros((int(math.floor((input_longitude + f) * 10000) - math.floor((input_longitude - f) * 10000)), int(math.floor((input_latitude + f1) * 10000) - math.floor((input_latitude - f1) * 10000))))
    latitude_matrix = np.zeros((int(math.floor((input_longitude + f) * 10000) - math.floor((input_longitude - f) * 10000)), int(math.floor((input_latitude + f1) * 10000) - math.floor((input_latitude - f1) * 10000))))
    longitude_matrix = np.zeros((int(math.floor((input_longitude + f) * 10000) - math.floor((input_longitude - f) * 10000)), int(math.floor((input_latitude + f1) * 10000) - math.floor((input_latitude - f1) * 10000))))
    for i in range(math.floor((input_longitude - f) * 10000), math.floor((input_longitude + f) * 10000)):
        for j in range(math.floor((input_latitude - f1) * 10000), math.floor((input_latitude + f1) * 10000)):
            # print(i-math.floor((input_longitude-0.0119)*10000),j-(input_latitude-0.0145)*10000)

            if (round(float(i/10000),4),round(float(j/10000),4)) in acc:
                # print(i-math.floor((input_longitude-0.0119)*10000),j-math.floor((input_latitude-0.0145)*10000))
                coordinate_meshgrid[i - math.floor((input_longitude - f) * 10000), j - math.floor((input_latitude - f1) * 10000)] = float(caccsevdict[round(float(i / 10000), 4), round(float(j / 10000), 4)])
                latitude_matrix[i - math.floor((input_longitude - f) * 10000), j - math.floor((input_latitude - f1) * 10000)] = round(float(j / 10000),4)
                longitude_matrix[i - math.floor((input_longitude - f) * 10000), j - math.floor((input_latitude - f1) * 10000)] = round(float(i / 10000),4)
            else:
                try:
                    coordinate_meshgrid[i - math.floor((input_longitude - f) * 10000), j - math.floor((input_latitude - f1) * 10000)] = 0
                except IndexError:
                    break;
    grad = signal.convolve2d(coordinate_meshgrid, kernel, 'same')
    unrolled_density = grad.ravel()
    unrolled_latitude = list(latitude_matrix.ravel())
    unrolled_longitude = list(longitude_matrix.ravel())
    # print(unrolled_longitude ,unrolled_latitude)
    x = []
    y = []
    z = []

    for i in range(len(unrolled_latitude)-1):
        if unrolled_latitude[i] != 0 and unrolled_longitude[i] != 0:
            y.append(unrolled_latitude[i])
            x.append(unrolled_longitude[i])
            z.append(unrolled_density[i])
    unrolled_latitude = y
    unrolled_longitude = x
    unrolled_density = z

    return grad, latitude_matrix,longitude_matrix, unrolled_latitude,unrolled_longitude, unrolled_density

def plotter():
    grad, latitude_matrix,longitude_matrix, unrolled_latitude,unrolled_longitude, unrolled_density =  accident_density_mapg()
    a = [min(unrolled_longitude), max(unrolled_longitude),min(unrolled_latitude), max(unrolled_latitude)]
    plt.imshow(grad, extent=a)
    plt.show()
    return

plotter()
