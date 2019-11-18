import requests
from time import sleep
import random


def tiebaSpider(name,start,end):

    url='https://tieba.baidu.com/f?'
    headers = {'User-Agent':'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
    for page in range(start,end+1):
        pn = (page-1)*50
        params = {'kw':name,'pn':pn}
        reponse = requests.post(url,headers=headers,params=params)
        html = reponse.content.decode("utf-8")

        filename = './data/page-'+str(page)+'.html'
        with open(filename,'w+',encoding='utf-8') as wf:
            wf.write(html)

        sleep(random.random()*2)

if __name__ == '__main__':
    name='python爬虫'
    start=1
    end=3
    tiebaSpider(name,start,end)