import requests
import re
from bs4 import BeautifulSoup


def down(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
    reponse = requests.get(url,headers)
    html = reponse.text
    return html,reponse.url
 
def get_cate():
    url = 'http://www.chinamedevice.cn'
    html, repose_url = down(url)
    #print(html)
    soup = BeautifulSoup(html,'lxml')
    x1 = soup.select('a.f12')
    if len(x1) !=0:
        for i in x1[0:-2]:
            real_url=i["href"]
            level0_url = url+real_url
            get_list(level0_url)

def get_list(url):
    base_url = url.rpartition('/')[0]
    for page in range(1,2):
        url = base_url+"/{}.html".format(str(page))
        html,cur_url = down(url)
        soup = BeautifulSoup(html,'lxml')
        list_a = soup.select('h3 > span > a[class="green fb f13"]')

        if len(list_a) == 0:
            break
        for page in list_a:
            link = page["href"]
            get_prodect(link)

def get_prodect(link):
    html, repose_url = down(link)
    soup = BeautifulSoup(html,'lxml')
    pro = soup.select('div.text01 > ul > li')
    p_name = pro[0].h3.get_text()
    p_class = pro[1].get_text()
    print("产品名称： "+p_name)
    print("产品分类： "+p_class)
    print("链接地址: "+link)



if __name__ == "__main__":
    get_cate()