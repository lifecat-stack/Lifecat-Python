# coding = utf-8
from urllib.request import urlretrieve
import requests
import re

"""
download images from pixabay in multiple pages 
"""

# browser header
headers = {
    'Cookie': '_ga=GA1.2.1336089541.1524833580; is_human=1; g_rated=; _gid=GA1.2.1465229331.1530691193; sessionid="eyJfbGFuZ3VhZ2UiOiJ6aCJ9:1facj9:hfXd1l39cUI0NGxyJI75D12dnqU"; client_width=962',
    'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}


def getHtml(url):
    """
    get response html

    :param url :url
    :return html
    """
    html = requests.get(url, headers=headers)
    return html


def getImg(html):
    """
    get url:image.jpg from html by Regular expression

    because there are three same images
    so we can filter these only get one image
    :param html: html
    :return [urls]
    """
    reg = '(https.+?\.jpg){1}'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html.text)

    for imgurl in imglist:
        # avoid too lang
        if len(imgurl) < 100:
            print(imgurl)
    print('过滤前共有total:', len(imglist), 'urls')
    return imglist


def img_filter(imgs):
    """
    filter urls

    :param imgs: 本例网站中统一图片url连续出现三次，故逢三取一
    :return: 过滤后的Urls
    """
    x = 0
    fimgs = []
    for img in imgs:
        x += 1
        if x % 3 == 0:
            fimgs.append(img)
    print('过滤后共有total:', len(fimgs), 'urls')
    return fimgs


def download(imgurls, count):
    """
    download images to local disk

    :param imgadresses: local directory
    :return:
    """
    # 下载到本地的目录，需存在
    localPath = r"D://爬虫/download/"
    baseName = 'page' + str(count) + '_image'
    x = 0
    for url in imgurls:
        try:
            urlretrieve(url, localPath + baseName + str(x) + '.jpg')
            x += 1
        except:
            print('下载失败')


if __name__ == '__main__':
    """
    download images from pixabay
    
    ?q='search框中搜索的关键词'
    """
    print("fill in path and cookie")

    content = input("download content")
    pages = input("请输入要爬取多少页(1页约100张):")

    urls = ["https://pixabay.com/zh/photos/?q=" + content + "&pagi={}".format(i) for i in range(1, int(pages) + 1)]
    # 页面html数据集合
    htmls = []

    # 已获取的页面数
    x = 0
    # 获取页面url的request-html
    for url in urls:
        x += 1
        print('已获取', x, '页/', int(pages))
        htmls.append(getHtml(url))
    # 对页面html进行图片爬取

    # 已下载的页面数
    count = 0
    for html in htmls:
        imgs = getImg(html)
        # 过滤重复图片-->同一图片的Url会出现三次-->过滤掉两次
        fimgs = img_filter(imgs)
        # 下载
        count += 1
        download(fimgs, count)
