# -*- coding: utf8 -*-
import urllib2

class HtmlDownloader(object):
    def download(self,url):
        if url is None or True == ".htm" in url:
            return None
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
