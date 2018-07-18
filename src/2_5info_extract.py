import requests
from bs4 import BeautifulSoup
import re
url = "http://python123.io/ws/demo.html"
r = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
for link in soup.find_all("a"): # find_all()
    # print(link)
    print(link.get('href'))    

print('-'*50)
print("含course属性的a标签:\n",soup.find_all('p','course'))
print("link1:\n",soup.find_all(id='link1'))

print('-'*50)
print("使用正则re.compile():\n",soup.find_all(id=re.compile('link')))