import requests
from bs4 import BeautifulSoup


def down(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
    reponse = requests.get(url,headers)
    html = reponse.text
    return html,reponse.url
 
def get_cate():
    url = 'http://www.chinamedevice.cn/'
    html ,repose_url = down(url)
    #print(html)
    soup = BeautifulSoup(html,'lxml')
    x1 = soup.select('a')
    print(x1)

def get_list():
    pass

def get_prodect():
    pass


if __name__ == "__main__":
    get_cate()