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
        # /view/123.htm
        # links = soup.find_all('a',href = re.compile(r"/view/\d+\.htm"))
        links = soup.find_all("a",href=True)

        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self,page_url,soup):
        res_data = {}
        # url
        res_data['url'] = page_url
        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        # title_node = soup.find('dd',class_ = "lemmaWgt-lemmaTitle-title")
        # <section class="module-basicpagetitle component">
        # <section class="module-articleintroduction component bg-white">
        # <section class="module-basicpagetitle component">
        try:
            title_node = soup.find('h2',class_ = "basic-title desktop-only")
            if title_node == None:
                # <section class="module-tmpl-article-detail">
                title_node = soup.find('section', class_ ="module-basicpagetitle component")

            res_data['title'] = title_node.get_text()
            print "*******  res_data_title: *******",res_data['title']
            if res_data['title'] == None:
                res_data['url'] == ""
                res_data['title'] = "*"
            # <div class = "lemma-summary">
            # summary_node = soup.find('div',class_ = "lemma-summary")
            # <div class="bodytext-data">
            summary_node = soup.find('div',class_ = "bodytext-data")
            res_data['summary'] = summary_node.get_text()
            print "*******  res_data_summary:   *******",res_data['summary']
            if res_data['summary'] == None:
                res_data['summary'] = "*"
            print "********** Web data ***********"
            print res_data
        except:
            print"*********No artitle**********"
        finally:
            return res_data

    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont,'html.parser',from_encoding = 'utf-8')

        new_urls = self._get_new_urls(page_url,soup)

        new_data = self._get_new_data(page_url,soup)

        return new_urls,new_data
