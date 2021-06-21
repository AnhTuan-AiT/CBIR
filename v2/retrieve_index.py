"""
Step 4: Retrieval system design
1. extract feature from query image
2. perform retrieval through index table
3. loop over results of retrieved top limit image and display the result
"""
# !/usr/bin/python
# usage
# python retrieve_index.py --query <query file path> --result-path <training set folder path>
# e.g. python retrieve_index.py --query D:/PersonalProjects/image-retrieval-OpenCV/test/6_test.png --result-path D:/PersonalProjects/image-retrieval-OpenCV/train

import getopt
import os
import sys
from datetime import datetime

from v2.FeatureDescriptor import *
from v2.Retriever import *

# parse command line argument
# print sys.argv[1:] # for debugging
try:
    (optlist, args) = getopt.getopt(sys.argv[1:], '', ['query=', 'result-path='])
except getopt.GetoptError as e:
    print(str(e))
    print('Usage: %s --query query_image --result-path dataset' % sys.argv[0])
    sys.exit(2)

# store argument into variables
query_file_path = ''
result_folder_path = ''

for opt, val in optlist:
    if opt == '--query':
        query_file_path = val
    else:
        result_folder_path = val

# extract feature from query image
# print(query_file_path)
query_img = cv2.imread(query_file_path)
feature_descriptor = FeatureDescriptor((8, 12, 3))
query_features = feature_descriptor.describe(query_img)

# perform retrieval through index file
'''retrieves db'''
retriever = Retriever()

start = datetime.now()
retrieval_results = retriever.search(query_features, limit=10)
print("Search time: ")
print(datetime.now() - start)

# display query image
query_img = cv2.resize(query_img, (300, 300))
cv2.imshow("Query", query_img)

# loop over results of retrieved top limit image
for (id, distance) in retrieval_results:
    result_file_path = os.path.abspath(result_folder_path + '/' + id + '.png')
    result = cv2.imread(result_file_path)

    # print(result)
    # print(result_file_path)
    im = cv2.resize(result, (300, 300))
    cv2.imshow("Result", im)
    cv2.waitKey(0)
    # cv2.destroyAllWindows()
