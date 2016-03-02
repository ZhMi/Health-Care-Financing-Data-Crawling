# -*- coding: utf8 -*-
import urllib2
import http.cookiejar

class HtmlDownloader(object):

    def makeMyOpener(self):
        head = {'Connection': 'Keep-Alive',
                'Accept': 'text/html, application/xhtml+xml, */*',
                'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
               }
        print "head:%s"%head
        cj = http.cookiejar.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        header = []

        print "weizhuangliulanqi"
        for key,value in head.items():
            elem = (key, value)
            header.append(elem)

        opener.addheaders = header
        return opener

    def download(self,url):
        if url is None:
            return None
        oper = self.makeMyOpener()
        uop = oper.open(url,timeout = 1000)
        print "response.getcode():%s"%uop.getcode()
        if 200 != uop.getcode():
            return None
        return uop.read()

