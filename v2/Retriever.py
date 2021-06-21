"""
Step 3: Retrieve index by query image
1. read all indices from db
2. compute distance of feature vectors between query and each row
3. sort the dictionary, return a tuple of (id, distance)
"""
# !/usr/bin/python
import math
import operator
from datetime import datetime

from v2.Index import Index


class Retriever:
    def __init__(self):
        print("Retriever begin to search Index")

    def search(self, query, limit):
        # build a new dictionary
        distances = {}

        # read all index from db
        index_obj = Index()
        data_list = index_obj.read_all_features_from_Index()

        # loop over rows in data list
        # and compute distance between query and row's feature
        print("START COMPUTE DISTANCE")
        start = datetime.now()

        for img_id, feature in data_list:
            # extract features out from db and convert back to numeric
            features = [float(x) for x in feature.strip('[]').split(',')]

            # compute distance between query and row's feature
            distance = self.calc_distance(features, query)
            distances[img_id] = distance

        print("COMPUTE TIME: ")
        print(datetime.now() - start)
        print("COMPLETE COMPUTE DISTANCE")
        # print("All distances from query as dict:")
        # [print(key, ':', value) for key, value in distances.items()]

        # sort the dictionary, return a list of tuples (id, distance)
        # smaller distances implies more relevant images
        print("START SORTING RESULT")
        start = datetime.now()

        if limit == 1:
            distances = [min(distances.items(), key=operator.itemgetter(1))]
        else:
            distances = sorted(distances.items(), key=operator.itemgetter(1))

        print("SORTING TIME: ")
        print(datetime.now() - start)
        print("COMPLETE SORTING RESULT")
        # print("Sorted distances as list of tuple:")
        # print(distances)

        # return top k records
        return distances[:limit]

    @staticmethod
    def calc_distance(features, query):
        # compute euclidean distance
        return sum([(x - y) ** 2 for x, y in zip(features, query)])
        # math.sqrt(sum([(x - y) ** 2 for x, y in zip(features, query)]))
