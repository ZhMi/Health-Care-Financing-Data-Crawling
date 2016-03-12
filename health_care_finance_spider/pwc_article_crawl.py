# -*- coding: utf8 -*-

__author__ = 'Zhmi'

import constant_config
import html_downloader
from bs4 import BeautifulSoup
import csv

class crawl_pwc_data:
    def __init__(self):
        self.root_url = constant_config.root_urls[1]
    def download_html(self):
        downloader = html_downloader.HtmlDownloader()
        html_content = downloader.download(self.root_url)
        return html_content
    def get_article_url_title_date(self, html_content):
        global temp_list, data_list
        soup = BeautifulSoup(html_content,'html.parser',from_encoding = 'utf-8')
        first_article = soup.find('div',class_ = "item")
        sister_articles = first_article.find_next_siblings('div',class_ = "item")
        data_list = []
        for article in sister_articles:
            temp_list = []
            link = article.find('a').get("href").encode('raw-unicode-escape')
            title = article.find('a').get("title").encode('raw-unicode-escape')
            # <p class="extra-info">
            time = article.find('p', class_ = "extra-info").get_text().strip().encode('raw-unicode-escape')
            temp_list.append(link)
            temp_list.append(title)
            temp_list.append(time)
            data_list.append(temp_list)
        return data_list
    def write_csv_file(self,data_list,category,file_name):
        csvfile = file(file_name,'wb')
        writer = csv.writer(csvfile)
        writer.writerow(category)
        writer.writerows(data_list)
        csvfile.close()

if __name__ == "__main__":
    pwc_crawler_object = crawl_pwc_data()
    html_content = pwc_crawler_object.download_html()
    data_list = pwc_crawler_object.get_article_url_title_date(html_content)
    category = ['url', 'title', 'publish_date']
    file_name = "pwc_data.csv"
    pwc_crawler_object.write_csv_file(data_list, category, file_name)


