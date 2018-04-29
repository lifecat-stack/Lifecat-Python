# PythonCrawler-Album
Lifecat系统之Python爬虫--Python爬虫爬取Demo图片数据
------
**功能：**
  使用`python`爬取并下载图片到本地  
  
**目的：**
  获取lifecat相册处理系统的demo数据，故采用python爬虫从pixabay上爬取关键词=child的数据

**pixabay是优秀的图片搜索网站：https://pixabay.com/**

![image](https://img-blog.csdn.net/20180428195814724?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dzaDU5NjgyMzkxOQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)


**下载情况：**

![image](https://img-blog.csdn.net/20180428200042979?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dzaDU5NjgyMzkxOQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

------

**version1.x快速实现(单线程操作)：**
```python
# coding = utf-8  
from urllib.request import urlretrieve  
import requests  
import re  
from lxml import etree  
  
# 请求头--伪装浏览器  
headers = {  
    'Cookie': '打开Chrome->F12->抓包XHR->request->cookie',  
    'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'  
}  
  
  
def getHtml(url):  
    """ 
    获取response 
    :param url: url 
    :return: html 
    """  
    html = requests.get(url, headers=headers)  
    return html  
  
  
def getImg(html):  
    """ 
    正则表达式方法: 
        获取image.jpg-url 
    :param html: html 
    :return: [urls] 
    """  
    reg = '(https.+?\.jpg){1}'  
    imgre = re.compile(reg)  
    imglist = re.findall(imgre, html.text)  
  
    x = 0  
    for imgurl in imglist:  
        if len(imgurl) > 100:  
            imgurl = None  
        else:  
            x += 1  
            print(imgurl)  
    print('total:', x)  
    return imglist  
  
  
# def getImg_xpath(html):  
#     """  
#     xpath方法:  
#         获取image.jpg-url  
#     :param html: html  
#     :return: [urls]  
#     """  
#     # TODO: something error  
#     selector = etree.HTML(html.text)  
#     xpath_content = []  
#     for i in range(100):  
#         xpath_content.append(selector.xpath(  
#             ' // *[ @ id = "content"] / div / div[3] / div / div / div[{}] / a'.format(str(i))))  
#         print(xpath_content)  
#     return xpath_content  
  
  
def download(imgadresses):  
    path = r"D://Python/download/"  
    name = 'image_'  
    x = 0  
    for adress in imgadresses:  
        try:  
            urlretrieve(adress, path + name + str(x) + '.jpg')  
            x += 1  
        except:  
            print('下载失败')  
  
if __name__ == '__main__':  
    """ 
    从pixabay网站下载图片 
        ?q='search框中搜索的关键词' 
    """  
    html = getHtml("https://pixabay.com/zh/photos/?q=child")  
    adresses = getImg(html)  
    download(adresses)  
  
# getImg_xpath(html)  
```
