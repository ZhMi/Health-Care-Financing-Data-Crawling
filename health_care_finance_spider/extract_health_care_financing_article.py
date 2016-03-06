__author__ = 'Zhmi'

# -*- coding: utf8 -*-

import constant_config
import csv

class extract_health_care_article(object):

    def __init__(self):
        self.kpmg_data_path = constant_config.kpmg_data_path
        self.article_list = []
        self.date_dict = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,
                          'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12} #date form: Wed Feb 25 14:00:00 UTC 2015
    def read_file(self):
        with open(self.kpmg_data_path,'rb') as f:
            reader = csv.reader(f)
            for line in reader:
                line[3] = line[3].split()
                self.article_list.append(line[:4])
            print self.article_list # ['url', 'main_title', 'second_title', 'publish_time']

    def date_transform(self):
        date_list = map(lambda x:[x[0],x[1]+x[2],x[3][5:]+x[3][1:2]+x[3][2:3]],self.article_list[1:]) # ['Thu', 'Jan', '01', '05:00:00', 'UTC', '2015']
        return date_list

if __name__ == '__main__':
    object = extract_health_care_article()
    object.__init__()
    article_list = object.read_file()
    date_list = object.date_transform()
    print date_list



