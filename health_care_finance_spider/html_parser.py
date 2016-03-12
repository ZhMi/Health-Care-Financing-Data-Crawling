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
        # https://home.kpmg.com/xx/en/home.html
        # https://home.kpmg.com/xx/en/home/insights/2016/02/announcing-the-2016-hr-transformation-survey.html
        links = soup.find_all("a",href = True)
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url,new_url)
            if ".htm" in new_full_url:
                new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self,page_url,soup):
        is_article_url = re.findall(r'https://home.kpmg.com/xx/en/home/insights/\d.',page_url)
        if len(is_article_url) != 0 and ".htm" in page_url:
            res_data = []
            try:
                # 添加 url
                res_data.append(page_url)

                # 找正标题
                # <h2 class="primary-head visible-lg visible-md visible-md-block">
                # <h2 class="basic-title desktop-only">Enhance your performance </h2>
                main_title_node = soup.find('h2',class_ = "basic-title desktop-only")
                if main_title_node == None:
                    main_title_node = soup.find('h2', class_ ="primary-head visible-lg visible-md visible-md-block")
                if main_title_node == None:
                    res_data.append("")
                res_data.append(main_title_node.get_text())

                # 找副标题
                # <p class="basic-desc desktop-only">
                # <p class="article-desc">
                second_title_node = soup.find('p',class_ = "basic-desc desktop-only")
                if second_title_node == None:
                    second_title_node = soup.find('p', class_ ="article-desc")
                if second_title_node == None:
                    res_data.append("")
                res_data.append(second_title_node.get_text())

                # 添加时间
                # <p class="publish-date" data-showtime="false" data-publisheddate="Tue Mar 01 15:48:00 UTC 2016">1 March 2016</p>
                time_node = soup.find('p',class_ = "publish-date")
                print "time_node text: %s"%time_node["data-publisheddate"]
                if time_node == None:
                    res_data.append("")
                else:
                    res_data.append(time_node["data-publisheddate"])

                # 添加正文
                #<div class="bodytext-data"><p>
                summary_node = soup.find('div',class_ = "bodytext-data")
                # 找不到指定标签的元素，soup 返回None
                if summary_node == None:
                    res_data.append("")
                else:
                    res_data.append(summary_node.get_text())

            except:
                print"********* No artitle  **********"
                for i in xrange(5):
                    res_data.append('')
            finally:
                print res_data
                return res_data
        else:
            print "***    this page has no article    ***"

    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding = 'utf-8')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data
