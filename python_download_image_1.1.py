# coding = utf-8
from urllib.request import urlretrieve
import requests
import re

# 请求头--伪装浏览器
headers = {
    'Cookie': '_ga=GA1.2.1336089541.1524833580; _gid=GA1.2.337646689.1524833580; is_human=1; sessionid="eyJfbGFuZ3VhZ2UiOiJ6aCJ9:1fC3AJ:QS3tnTkIcsUVpnRM7EkIwDXnLUA"; client_width=677',
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


def img_filter(imgs):
    x = 0
    fimgs = []
    for img in imgs:
        x += 1
        if x % 3 == 0:
            fimgs.append(img)
    return fimgs


def download(imgurls, count):
    """
    根据url下载图片到本地
    :param imgurls: Url
    :param count: 当前下载的页面-->防止后一页面覆盖前一页面
    :return:
    """
    # 下载到本地的目录，需存在
    path = r"D://Python/download/"
    name = 'page' + count + '_image'
    x = 0
    for url in imgurls:
        try:
            urlretrieve(url, path + name + str(x) + '.jpg')
            x += 1
        except:
            print('下载失败')


if __name__ == '__main__':
    """
    从pixabay网站下载图片
        ?q='search框中搜索的关键词'
    """
    word = input("请输入搜索关键词:")
    pages = input("请输入要爬取多少页(1页约100张):")
    # 构建页面循环源
    urls = ["https://pixabay.com/zh/photos/?q=" + word + "&pagi={}".format(i) for i in range(1, int(pages) + 1)]
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
