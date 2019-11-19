import requests
from time import sleep
import random
from lxml import etree
import csv
import codecs


def tiebaSpider(name,start,end):

    url='https://tieba.baidu.com/f?'
    base_url='https://tieba.baidu.com'
    headers = {'User-Agent':'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
    for page in range(start,end+1):
        pn = (page-1)*50
        params = {'kw':name,'pn':pn}
        reponse = requests.post(url,headers=headers,params=params)
        html = reponse.content.decode("utf-8")

        selector = etree.HTML(html)
        ls = selector.xpath('//li[contains(@class,"j_thread_list clearfix")]')

        for itrm  in ls:
            title = itrm.xpath('.//a[@class="j_th_tit "]/text()')[0]
            detail_url =base_url+itrm.xpath('.//a[@class="j_th_tit "]/@href')[0]
            nums = itrm.xpath('.//span[@class="threadlist_rep_num center_text"]/text()')[0]
            author = itrm.xpath('.//a[@class="frs-author-name j_user_card "]/text()')[0]
            get_info = "标题:"+title+"\t作者:"+author+"\t链接:"+detail_url+"\t访问量:"+nums
            print(get_info)
            # with open('./data/tieba-{}.txt'.format(name),'a') as fw:
            #     fw.write(get_info+"\n")
            with codecs.open('./data/tieba-{}.csv'.format(name),'a',encoding='utf-8') as csv_w:
                wr = csv.writer(csv_w)
                wr.writerow([title,author,nums,detail_url])

        sleep(random.random()*2)

if __name__ == '__main__':
    name='python爬虫'
    start=1
    end=3
    tiebaSpider(name,start,end)