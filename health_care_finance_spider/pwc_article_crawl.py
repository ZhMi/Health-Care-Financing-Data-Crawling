__author__ = 'Zhmi'
# -*- coding: utf8 -*-

import constant_config
import html_downloader
from bs4 import BeautifulSoup


root_url = constant_config.root_urls[1]

downloader = html_downloader.HtmlDownloader()
html_content = downloader.download(root_url)

# print "html_content:%s" %html_content

soup = BeautifulSoup(html_content,'html.parser',from_encoding = 'utf-8')
links = soup.find_all("a",href = True)

first_article = soup.find('div',class_ = "item")
# print "******** first_srticle:",first_article
article_set = first_article.find_next_siblings('div',class_ = "item")
for article in article_set:
    print "href:",article.find('a').get("href")
    print "title:",article.find('a').get("title").encode('raw-unicode-escape')
    # <p class="extra-info">
    time = article.find('p', class_ = "extra-info").get_text().strip()
    print "time:",time
    print "****************"
print "******** article set:",len(article_set)

