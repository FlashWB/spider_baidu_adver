import requests

def getHtml(url):
    kv = {'user-agent':'Mazilia/5.0'}  # 模拟浏览器访问
    try:
        r = requests.get(url, headers = kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text[1000:2000])
    except:
        print("爬取失败")

if __name__ == "__main__":
    url = "https://www.amazon.cn/dp/B00QJDOLIO/461-0344781-0596249?_encoding=UTF8&pf_rd_i=desktop&pf_rd_m=A1AJ19PSB66TGU&pf_rd_p=ce9fc27b-a4fd-4da7-bb9a-95ad1b6617a0&pf_rd_r=XKNHNRWHKHYX4GGYE39Y&pf_rd_s=Tcg-slide-1&pf_rd_t=36701&ref_=p-Tcg-slide-1--2efc1934-96f8-455f-bc30-b0debca468f9"
    getHtml(url)

