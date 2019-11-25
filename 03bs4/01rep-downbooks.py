import requests
import random
from time import sleep,ctime,time
from bs4 import BeautifulSoup


def down(url,headers):
    reponse = requests.get(url,headers)
    html = reponse.content.decode('gb18030')
    return html

def parase(html):
    soup = BeautifulSoup(html,'lxml')
    h1 = soup.select('h1.articleH1')[0].get_text()
    save_data('\n\n'+h1+'\n')
    content = soup.select('div#content > p')
    for p_text in content:
        t = p_text.get_text()
        save_data(t)


def save_data(text):
    with open('超新星纪元.txt','a',encoding='utf-8') as wf:
        wf.write(text)


if __name__ == "__main__":

    headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}

    print("开始爬取时间：",ctime())
    start_time = time()
    for i in reversed([x for x in range(210980,211015)]): #210980
        url='http://book.sbkk8.com/xiandai/liucixinzuopinji/chaoxinxingjiyuan/{}.html'.format(str(i))
        html = down(url,headers)
        parase(html)
        sleep(random.random()*2)
    stop_time = time()
    print("爬取完成时间：",ctime())
    print("总用时：{}秒".format(str(stop_time-start_time)))