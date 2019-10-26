import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
input_latitude = 0
input_longitude = 0
convolution_matrix = [[1,1,1],[1,1,1],[1,1,1]]
data = pd.read_csv("2019-08-cambridgeshire-street.csv",None)
crime = data['Crime type'].values
crime_types = np.unique(crime)
crime_weighting = [1 for i in range(len(crime_types)-1)]
crime_dictionary = dict(zip(crime_types,crime_weighting))
print(crime_dictionary)
crime_latitude =