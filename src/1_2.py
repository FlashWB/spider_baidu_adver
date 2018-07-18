import requests
# r = requests.get("http://www.baidu.com")
# print(r.status_code)
# print("r.encoding:",r.encoding)
# print("r.apparent_encoding:", r.apparent_encoding)

def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "访问异常"

if __name__ == "__main__":
    url = "http://www.baidu.com"
    print(getHtmlText(url))

