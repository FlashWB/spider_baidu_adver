import requests
from bs4 import BeautifulSoup
url = "http://python123.io/ws/demo.html"
r = requests.get(url)
print(r.text)

demo = r.text
soup = BeautifulSoup(demo, "html.parser") # 按html格式解析
# print(soup.prettify()) # 美化格式
# print("soup.a:", soup.a)
# print("soup.a.name:", soup.a.name) # 对标签通过 .name获取
# print("soup.a.parent.name:", soup.a.parent.name) # 包含 a标签的上一层标签

tag = soup.a # a标签 <tag>
print(".attrs查看属性:",tag.attrs) # 以字典形式输出
print(".string查看标签内容:",tag.string) 
print("type类型——非属性字符串:", type(tag.string))
print("type类型——属性中字符串：", type(tag.attrs['href']))

