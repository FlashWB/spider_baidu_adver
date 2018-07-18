import requests
from bs4 import BeautifulSoup
import bs4
import re
class spider(object):
    def __init__(self,url):
        super(spider,self).__init__() # super(父类,self).__init__()
        self.url = url

    def getHtmlText(self):
        try:
            r = requests.get(self.url, timeout = 30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except:
            return "error"

    def fillUnivList(self, ulist, html):
        soup = BeautifulSoup(html, "html.parser")
        for tr in soup.find('tbody').children:
            # print(tr)
            # print(bs4.element.Tag)
            if isinstance(tr,bs4.element.Tag):# classinfo 判断， 如果tr与参数2类型相同，返回True
                tds = tr('td')
                ulist.append([tds[0].string, tds[1].string, tds[3].string])
    
    def printUnivList(self, ulist, num): # num打印学校数量
        # print("{:^2}\t{:<20}\t{:5}".format("排名","学校名称","部分")) # 优化前
        tplt = "{0:^10}\t{1:{3}<10}\t{2:<10}"  # 新建打印格式
        print(tplt.format("排名","学校名称","部分",chr(12288))) # chr(12288)中文字符空格
        for i in range(num):
            u = ulist[i]
            # print("{:^2}\t{:<20}\t{:5}".format(u[0],u[1],u[2])) # {:^10} 中间对齐，宽度为10 优化前
            print(tplt.format(u[0],u[1],u[2],chr(12288)))

if __name__ == "__main__":
    uinfo = []
    number = 10
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    sp = spider(url)
    html = sp.getHtmlText()
    sp.fillUnivList(uinfo, html)
    sp.printUnivList(uinfo, number)




