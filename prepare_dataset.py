import cv2
from keras.datasets import cifar10
import argparse
from PIL import Image as im
import os.path
from os import path

(X_train, y_train), (X_test, y_test) = cifar10.load_data()

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()

# Switch for the path to our photos directory
ap.add_argument("-dte", "--dataset_test", required=True, help="Path to file that contains images test")
ap.add_argument("-dtr", "--dataset_train", required=True, help="Path to file that contains images train")
args = vars(ap.parse_args())

path_test = args["dataset_test"]
if (path.isdir(path_test) == False):
    os.mkdir(path_test)

path_train = args["dataset_train"]
if (path.isdir(path_train) == False):
    os.mkdir(path_train)

for i in range(len(X_train)):
    data = im.fromarray(X_train[i])
    cv2.imwrite(os.path.join(path_train, str(i) + "_train.png"), X_train[i])
    cv2.waitKey(0)

for i in range(len(X_test)):
    data = im.fromarray(X_test[i])
    cv2.imwrite(os.path.join(path_test, str(i) + "_test.png"), X_test[i])
    cv2.waitKey(0)
