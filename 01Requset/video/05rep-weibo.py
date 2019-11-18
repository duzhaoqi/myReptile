import requests

url='https://weibo.com/p/1005056259768047/home?from=page_100505&mod=TAB&is_all=1'
headers={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    'Cookie':'SINAGLOBAL=3586581222882.2036.1571199720376; UOR=v.baidu.com,widget.weibo.com,www.baidu.com; UM_distinctid=16dd898962896-02b61543e2e537-1a201708-1fa400-16dd898962e5aa; login_sid_t=1a58b509959c24543f975eca83287bb1; cross_origin_proto=SSL; Ugrow-G0=7e0e6b57abe2c2f76f677abd9a9ed65d; YF-V5-G0=f5a079faba115a1547149ae0d48383dc; WBStorage=384d9091c43a87a5|undefined; _s_tentry=www.baidu.com; wb_view_log=1920*10801.100000023841858; Apache=2327755760227.3413.1574053113770; ULV=1574053113778:6:1:1:2327755760227.3413.1574053113770:1572394068916; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW9X8X2W0YrjVARcRC6Lvec5JpX5K2hUgL.FoqESK.NSon7ShM2dJLoI0qLxK-L1-BL1K5LxKML1-BL1h5LxKML1-2L1hBLxKMLB-zL1K.LxKMLB-zL12zLxKBLB.2LB.2t; ALF=1605589126; SSOLoginState=1574053126; SCF=AvDUp53L70y_FJ7_mY2B6LPL4mBrgopYeOVXaRBw3geW5jaQQh0K1hXcuhIC_A4821ALHat0TcL-e8h90nIzit4.; SUB=_2A25w1lVXDeRhGeBM7lsW9ibMzzuIHXVTosGfrDV8PUNbmtANLUHHkW9NRM0wp5F8GRpn5DA2W-B1RFvoQTJii2J-; SUHB=0d4-QbFl3dE1LT; un=18738399739; wvr=6; wb_view_log_6259768047=1920*10801.100000023841858; YF-Page-G0=530872e91ac9c5aa6d206eddf1bb6a70|1574053149|1574053138; webim_unReadCount=%7B%22time%22%3A1574053163177%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D'
         }

reponse = requests.get(url,headers=headers)
html = reponse.text
print(html)