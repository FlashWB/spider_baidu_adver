import requests
import os # 系统编程模块 

def getHtml(url,root):
    path = root + url.split('%2F')[-1]
    print(path)
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            with open(path,'wb') as f:
                f.write(r.content)
                f.close()
                print("文件保存成功")
        else:
            print("文件已保存")
    except:
        print("error")

if __name__ == "__main__":
    url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1525875442533&di=4eb6ad776034e80ab0f19ba243ebfb51&imgtype=0&src=http%3A%2F%2Fimage.codes51.com%2FArticle%2Fimage%2F20160229%2F20160229084048_5249.png"
    root = "./photo/"
    getHtml(url,root)
    







