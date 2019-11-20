from  lxml import etree

htmlx="""
<div>
    <ul>
        <li class="item-0"><a href="www.baidu.com">baidu</a>
        <li class="item-1"><a href="https://blog.csdn.net/qq_25343557">myblog</a>
        <li class="item-2"><a href="https://www.csdn.net/">csdn</a>
        <li class="item-3"><a href="https://hao.360.cn/?a1004">hao123</a>
"""

html = etree.HTML(htmlx)
full_html = etree.tostring(html)
print(full_html.decode('utf-8'))