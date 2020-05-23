import csv
import pandas as pd
from sklearn.cluster import KMeans
writer = csv.reader('./Static/fob_spring_2019_aggregates.csv')
with open('./Static/fob_spring_2019_aggregates.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in data:
        print(', '.join(row))
