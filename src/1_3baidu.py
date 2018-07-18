import requests

def getHtml(url,word):
    try:
        kv = {'wd':word}  #只可以是键值对
        r = requests.get(url, params=kv)
        print(r.request.url)
        r.raise_for_status()
        print(r.text)
    except:
        print("error")

if __name__ == "__main__":
    url = "http://www.baidu.com/s"
    keyword = "python"
    getHtml(url,keyword)
