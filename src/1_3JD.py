import requests

def  get_html(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()  # 请求返回状态码，如果返回不成功郑码，会抛出异常
        r.encoding = r.apparent_encoding
        print(r.text[:1000])
    except:
        print("爬取失败")


if __name__ == "__main__":
    url = "http://www.baidu.com"
    get_html(url)



