# -*- coding: utf8 -*-

from bs4 import BeautifulSoup
import re
import urlparse
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class HtmlParser(object):

    def _get_new_urls(self,page_url,soup):

        new_urls = set()
        # root_url = "http://baike.baidu.com/view/21"
        # /view/123.htm
        # links = soup.find_all('a',href = re.compile(r"/view/\d+\.htm"))

        # https://home.kpmg.com/xx/en/home.html
        # https://home.kpmg.com/xx/en/home/insights/2016/02/announcing-the-2016-hr-transformation-survey.html

        links = soup.find_all("a",href = True)

        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self,page_url,soup):
        res_data = []
        # url
        res_data.append(page_url)
        try:
            title_node = soup.find('h2',class_ = "basic-title desktop-only")
            if title_node == None:
                # <section class="module-tmpl-article-detail">
                title_node = soup.find('section', class_ ="module-basicpagetitle component")
            res_data.append(title_node.get_text())
            # <div class="bodytext-data">
            summary_node = soup.find('div',class_ = "bodytext-data")
            # 找不到指定标签的元素，soup 返回None
            res_data.append(summary_node.get_text())

        except:
            print"********* No artitle  **********"
            for i in xrange(2):
                res_data.append('')
        finally:
            print res_data
            return res_data

    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont,'html.parser',from_encoding = 'utf-8')

        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data
