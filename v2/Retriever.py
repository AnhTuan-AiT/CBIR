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
import numpy as np


class Retriever:
    def search(self, query, limit):
        print("RETRIEVER BEGIN TO SEARCH INDEX")

        # build a new dictionary
        distances = {}

        # read all index from db
        index_obj = Index()
        img_features = index_obj.read_all_features_from_Index()

        # loop over rows in data list
        # and compute distance between query and row's feature
        print("START COMPUTE DISTANCE")
        start = datetime.now()

        for img_id, color_histogram_feature, humoments_feature in img_features:
            # extract features out from db and convert back to numeric
            color_feature = [float(x) for x in color_histogram_feature.strip('[]').split(',')]
            # moments_feature = [float(x) for x in humoments_feature.strip('[]').split(',')]

            # compute distance between query and row's feature
            distance = self.euclidean_distance(color_feature, query)
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
    def chi2_distance(histA, histB, eps=1e-10):
        # compute the chi-squared distance
        d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
                          for (a, b) in zip(histA, histB)])

        # return the chi-squared distance
        return d

    @staticmethod
    def euclidean_distance(features, query):
        # compute euclidean distance
        return math.sqrt(sum([(x - y) ** 2 for x, y in zip(features, query)]))
