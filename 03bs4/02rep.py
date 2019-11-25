from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import *


def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'lxml')
        title = bs.h1
    except AttributeError as e:
        return None
    return title



if __name__ == "__main__":
    url="http://www.pythonscraping.com/pages/page1.html"
    title = get_title(url)
    if title == None:
        print("Title could not be found")
    else:
        print(title)