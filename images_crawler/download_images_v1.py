# coding = utf-8
import re
from urllib.request import urlretrieve
import requests

"""
download images from pixabay in one page 
"""

# browser header
headers = {
    'Cookie': 'is_human=1; _ga=GA1.2.1016714791.1533287091; sessionid="eyJfbGFuZ3VhZ2UiOiJ6aCJ9:1foKHx:ydnofwM0HmYHR_zhIT3UlqwBF54"; _gid=GA1.2.1118425725.1533957003; client_width=1147',
    'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
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

    :param html: html
    :return [urls]
    """
    reg = '(https.+?\.jpg){1}'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html.text)

    x = 0
    for imgurl in imglist:
        # avoid too lang
        if len(imgurl) < 100:
            x += 1
            print(imgurl)
    print('total image:', x)
    return imglist


def download(imgadresses):
    """
    download images to local disk

    :param imgadresses: local directory
    :return:
    """
    localPath = r"D://爬虫/download/"
    baseName = 'image_'
    x = 0
    for adress in imgadresses:
        try:
            urlretrieve(adress, localPath + baseName + str(x) + '.jpg')
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

    html = getHtml("https://pixabay.com/zh/photos/?q=" + content)
    adresses = getImg(html)
    download(adresses)
