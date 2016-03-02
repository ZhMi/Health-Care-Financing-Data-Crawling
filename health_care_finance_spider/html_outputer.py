# -*- coding: utf8 -*-

# author: zhmi
# mail: zhmi120@sina.com

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
        writer.writerow(['url','title','summary'])
        writer.writerows(self.datas)
        csvfile.close()
        print "finish write file."





