"""
Step 2: Extracting Features from Dataset
1. read in list of filenames for all jpg images in directory
2. write the path and name into database
3. extract features out using the feature descriptor and write feature vectors into database
"""
# !/usr/bin/python
# USAGE:
# python feature_extraction.py --dataset <folder path of training set>
# e.g. python feature_extraction.py --dataset D:/PersonalProjects/image-retrieval-OpenCV/train

import getopt
import sys

# import pkgs
from v2.FeatureDescriptor import *
from v2.Index import *

# parse arguments
try:
    optlist, args = getopt.getopt(sys.argv[1:], '', ['dataset='])
    # print optlist, args
except getopt.GetoptError as e:
    print(str(e))
    print('Usage: %s --dataset path/to/dataset' % sys.argv[0])
    sys.exit(2)

data_dir = ''

for opt, val in optlist:
    if opt == '--dataset':
        data_dir = val

print(data_dir)
print()

# initialize feature descriptor
# set bin = 16, H=
feature_descriptor = FeatureDescriptor((8, 12, 3))

# write all images' path into db
index_obj = Index()
index_obj.write_img_path_into_Image(data_dir)

# read in list of filenames for all png images in directory
data_list = index_obj.read_img_path_from_Image()
# print(data_list)

# extract feature for each image in dataset directory and store into db
for file in data_list:
    # print(file)
    img = cv2.imread(file[1])

    imgID = file[0]
    feature = feature_descriptor.describe(img)

    # write id, features to output
    index_obj.write_all_features_into_Index(imgID, feature)
