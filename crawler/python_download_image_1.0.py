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
