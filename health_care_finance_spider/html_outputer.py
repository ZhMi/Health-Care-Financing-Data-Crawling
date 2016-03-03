# -*- coding: utf8 -*-
import sys
import csv

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)
    def write_csv_file(self):
        print "begin write file."
        csvfile = file('data.csv','wb')
        writer = csv.writer(csvfile)
        writer.writerow(['url','main_title','second_title','publish_time','summary'])
        writer.writerows(self.datas)
        csvfile.close()
        print "finish write file."







