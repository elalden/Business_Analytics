import csv

import documents as documents
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

writer = csv.reader('./Static/fob_spring_2019_aggregates.csv')
doc_string = []
with open('./Static/fob_spring_2019_aggregates.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     for row in spamreader:
         doc_string.append(str(row))

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(doc_string)

true_k = 2
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=3)
model.fit(X)

print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :10]:
        print(' %s' %terms[ind]),
    print


