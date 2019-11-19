from lxml import etree
import requests
import random
from time import sleep


def down(url):
    headers = {}
    headers["User-Agent"]="Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/78.0.3904.97 Safari/537.36"
    reponse = requests.get(url,headers=headers)
    html = reponse.content.decode('utf-8')
    return html

def parase(html):
    html = etree.HTML(html)
    ls = html.xpath('//li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')
    print("ls: ",len(ls))
    for item in ls:
        link = item.xpath('.//div[@class="info clear"]/div[@class="title"]/a/@href')[0]
        detail_html = down(link)
        detail_html = etree.HTML(detail_html)


def saveDate():
    pass

if __name__ == "__main__":
    for page in range(1,51):
        if page == 1:
            url='https://zz.lianjia.com/ershoufang/'
        else:
            url='https://zz.lianjia.com/ershoufang/p{}/'.format(str(page))
        html = down(url)
        parase(html)
        sleep(random.random()*2)