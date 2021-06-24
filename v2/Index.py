#!/usr/bin/python
# Index Class would support :
# 0. write all img path  in the directory into Image Table
# 1. read all img path from Image Table
# 2. write all features into Index Table
# 3. read all freatures from Index Table

import MySQLdb
import os
import traceback


class Index:
    def write_img_path_into_Image(self, dataset):
        db = MySQLdb.connect(user="root", passwd="dongphuong189", host="localhost", db="image_retrieval")
        cursor = db.cursor()

        for file_id, file in enumerate(os.listdir(dataset)):
            if file.endswith('.png'):
                file_id = file[:-4]
                file_path = dataset + "/" + file
                sql = """insert into image (img_id, file_path) values ('{0}','{1}');""".format(str(file_id), file_path)

                # print(sql)

                try:
                    # execute sql statement
                    cursor.execute(sql)
                    db.commit()  # commit changes in db
                except Exception:
                    db.rollback()  # rollback in case error
                    print("Error: Unable to write into Image")
                    print(traceback.format_exc())

        # disconnect from server
        db.close()

    def read_img_path_from_Image(self):
        db = MySQLdb.connect(user="root", passwd="dongphuong189", host="localhost", db="image_retrieval")
        cursor = db.cursor()
        sql = """select * from image;"""

        try:
            cursor.execute(sql)
            data = cursor.fetchall()
        except Exception:
            "Error: Unable to fetch data from Image"

        # print(data)

        # disconnect from server
        db.close()
        return data

    def write_all_features_into_Index(self, img_id, feature, humoments_feature):
        feature = str(feature)
        humoments_feature = str(humoments_feature)

        db = MySQLdb.connect(user="root", passwd="dongphuong189", host="localhost", db="image_retrieval")
        cursor = db.cursor()

        sql = "insert into image_index (img_id, color_histogram_feature, humoments_feature) values ('{0}','{1}','{2}')".format(
            img_id, feature,
            humoments_feature)

        # print(sql)

        try:
            cursor.execute(sql)
            db.commit()
        except Exception:
            db.rollback()
            print(traceback.format_exc())

        db.close()

    def read_all_features_from_Index(self):
        db = MySQLdb.connect(user="root", passwd="dongphuong189", host="localhost", db="image_retrieval")
        cursor = db.cursor()
        sql = "select * from image_index;"

        try:
            cursor.execute(sql)
            data = cursor.fetchall()
        except Exception:
            print(traceback.format_exc())

        db.close()
        return data
