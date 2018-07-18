#coding=utf-8
import requests
import re
import bs4
class spider(object):
    def __init__(self,url):
        super(spider,self).__init__()
        self.url = url
        # self.word = word

    def getHtml(self,word):
        kv = {'user-agent':'Mazilia/5.0'}  # 模拟浏览器访问
        kw = {'wd':word}
        try:
            r = requests.get(self.url,headers=kv, params=kw)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except:
            return "error"
    
    # def save_file(self,file_name, contents):
    #     f = open(file_name,'w')
    #     f.write(contents)
    #     f.close()

    

    def conductHtml(self,html):
        soup = bs4.BeautifulSoup(html,"html.parser")
        # div_ = soup.div
        i = 0
        tag = soup.find('div',id='content_left')
    #     # print (len(list(tag.children)))     # 子标签
    #     # print (len(list(tag.descendants)))  # 所有标签 子子孙孙
    #     self.save_file('result.txt',''.join(list(tag.descendants)))
    #     print(tag)

##############################################################
        for child_div in tag.children:
            # print(child_div)
            # tag1 = child_div.find('span') # 只能在子标签中长span
            # print(tag1)
            # print('-'*20)
            try:
                for child_div_div in child_div.find('div').descendants:
                    tag1 = child_div_div.find('span')
                    print(tag1)
                    if tag1 == -1:
                        # print(-1)
                        pass
                    elif tag1 == None:
                        # print(-1)
                        pass
                    else:
                        # print(tag1)
                        try:
                            if tag1.string=="广告":
                                i =i + 1
                                print(child_div_div.div[2])

                        except:
                            pass
            except:
                pass
###################################################

            # if child_div=='广告':
            #     i=i+1
            #     try:
            #         # print(child_div.name)
            #         print(child_div.string) 
            #         # print (child_div.div.h3.a.img.get_text().encode("utf-8"))
            #     except Exception:
            #         pass
                #help(child_div.div)
            # print(child_div.get_text())
################################################

        # for child_div in tag.descendants:
        #     try:
        #         tag_span = child_div.find('span')
        #         if tag_span.string == '广告':
        #             i += 1
        #             print(tag_span)
        #     except:
        #         pass
        print(i)
        return i


    def pringList(self,num):
        pass

if __name__ == "__main__":
    url = "http://www.baidu.com/s"
    word = "手机"
    sp = spider(url)
    htmlText = sp.getHtml(word)
    sp.conductHtml(htmlText)



