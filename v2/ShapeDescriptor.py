"""
Step1: define feature descriptor
1. convert to HSV and initialize features to quantify and represent the image
2. split by corners and elliptical mask
3. construct feature list by looping through corners and extending with center
"""
from math import copysign, log10

from cv2 import cv2


class ShapeDescriptor:
    # initialize features to quantify and represent the image
    def describe(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        features = cv2.HuMoments(cv2.moments(image)).flatten().tolist()

        for i in range(0, 7):
            features[i] = -1 * copysign(1.0, features[i]) * log10(abs(features[i]))

        return features
