__author__ = 'Zhmi'

# -*- coding: utf8 -*-

import constant_config
import csv

class extract_health_care_article(object):

    def __init__(self):
        self.kpmg_data_path = constant_config.kpmg_data_path
        self.article_list = []
        self.date_dict = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,
                          'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12} #date form: Wed Feb 25 14:00:00 UTC 2015
    def read_file(self):
        with open(self.kpmg_data_path,'rb') as f:
            reader = csv.reader(f)
            for line in reader:
                for index in xrange(3):
                    line[index+1] = line[index+1].lower().split()
                self.article_list.append(line[:4])
            print self.article_list # ['url', 'main_title', 'second_title', 'publish_time']

    def data_pretreat(self):
        '''
        function description:
            date form of raw data is ['Thu', 'Jan', '01', '05:00:00', 'UTC', '2015']
            filter correct form of time as follows: ['2015', 'Aug', '01']
            combine main title and second title
        '''
        data_list = map(lambda x:[x[0],list(set(x[1]+x[2])),x[3][5:]+ x[3][1:2] +x[3][2:3]],self.article_list[1:])
        return data_list

    def filter_contains_topic_data(self,data_list):
        '''
        data form:
            every piece of data is a list contains words of main title and second title
            key_words is a list contains key words
        function description:
            if record contain contains key words,intersection of those two list is not null
            change words vector into length of intersection
            return the data which contains key words(length of intersection is not 0)
        '''
        key_words = constant_config.key_words
        for index in xrange(len(data_list)): # data_list: [['url', ['a', 'welcome', ], ['2015', 'nov', '23']]
            words_vector = data_list[index][1]
            intersection = list(set(words_vector) & set(key_words))
            data_list[index][1] = len(intersection)
            if 1 == len(intersection):
                print "***  words_vector  ***",len(words_vector)
                print "***  content of words_vector ***",words_vector
                print "***  intersection  ***",len(intersection)
                print "\n"
        contain_topic_data = filter(lambda x: x[1] != 0,data_list)
        return contain_topic_data

    def filter_record_belongs_particular_time(self,data_list,year,month):
        date_filtered_data = filter(lambda x: x[2][0:1] == year and x[2][1:2] == month,data_list)
        date_filtered_url_date = map(lambda x:[x[0],x[2]],date_filtered_data)
        return date_filtered_url_date

    def write_csv_file(self,data_list,category,file_name):
        csvfile = file('filtered_date_key_words_date','wb')
        writer = csv.writer(csvfile)
        writer.writerow(['url','date'])
        writer.writerows(data_list)
        csvfile.close()

if __name__ == '__main__':
    object = extract_health_care_article()
    object.__init__()
    article_list = object.read_file()
    filtered_data_list = object.data_pretreat()
    contain_topic_data = object.filter_contains_topic_data(filtered_data_list)
    print "contain_topic_data:%s"%contain_topic_data
    date_filtered_url_date = object.filter_record_belongs_particular_time(contain_topic_data,constant_config.year,constant_config.month)
    print "date_filted_url_date:%s"%date_filtered_url_date
    category = ['url','date']
    file_name = 'filtered_date_key_words_date'
    object.write_csv_file(date_filtered_url_date,category,file_name)

