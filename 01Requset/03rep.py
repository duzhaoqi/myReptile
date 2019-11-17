import requests

headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}

proxies={
    "http":"113.124.93.82:9999",
    "http":"59.57.241.6:9999",
    "https":"113.124.93.231:9999",
    "https":"114.239.148.32:808"
         }

try:
    response = requests.get("https://www.baidu.com/",headers=headers,timeout=5,proxies=proxies)
    print(response.status_code)
    #content 返回字节流数据
    # print(response.content.decode("UTF-8"))
    print(response.url)
except Exception as e:
    print(e)
