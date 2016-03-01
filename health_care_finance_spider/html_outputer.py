# -*- coding: utf8 -*-
import sys

class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html','w')
        fout.write("""<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />""")
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

        # ascii
        for data in self.datas:
            print "*********** data **********:"%data
            fout.write("<tr>")
            fout.write("<td>%s</td>"%data['url'])
            fout.write("<td>%s</td>"%data['title'])
            # fout.write("<td>%s</td>"%data['title'].encode('utf-8'))
            # fout.write("<td>%s</td>"%data['summary'].encode('utf-8'))
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()

        print "Finish writing data"







