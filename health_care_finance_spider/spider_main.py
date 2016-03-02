# -*- coding: utf-8 -*-
from __future__ import unicode_literals # 解决控制台输出中文乱码问题
import url_manager , html_downloader , html_parser , html_outputer

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    def craw(self,root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s'%(count,new_url)
                html_cont = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 5:
                    break
                count = count + 1
            except:
                print 'craw %s html failed'%new_url
        print "begin write data into file"

        self.outputer.write_csv_file()

if __name__ == "__main__":
    # root_url = "http://baike.baidu.com/view/21"
    # https://home.kpmg.com/xx/en/home.html
    root_url =  "https://home.kpmg.com/xx/en/home.html"
    obj_spider = SpiderMain() # 创建爬虫总调度程序
    obj_spider.craw(root_url) # start spider