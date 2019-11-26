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
        list_a = soup.select('a[class="green fb f13"]')
        #list_a = soup.find_all(re.compile(r'<a .* class=\"green fb f13\" .*?</a>'))

        if len(list_a) == 0:
            break
        for page in list_a:
            if page.string == None:
                continue
            name = page.get_text()
            link = page["href"]
            get_prodect(link)

def get_prodect(link):
    html, repose_url = down(link)
    soup = BeautifulSoup(html,'lxml')
    pro = soup.select('div.text01 > ul > li')
    for li in pro:
        print(li.get_text().replace("\n","").replace("・",""))
    print("="*60)


if __name__ == "__main__":
    get_cate()