from bs4 import BeautifulSoup
import re


htmlx="""
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(htmlx,'lxml')

print(soup.prettify())

print(soup.title)
print(soup.a)
print(soup.head)
print(soup.head.string)


print(soup.a)
print(soup.find_all('a'))

head_tag = soup.head
print(head_tag)
print(head_tag.contents)

body_tag = soup.body
print(body_tag)
print(body_tag.contents)

print("="*60)
for i in body_tag.children:
    print(i)

print(body_tag.children)
#
# print("="*60)
# for i in body_tag.descendants:
#     print(i)

print(soup.a)
print(soup.find_all('a'))
print(soup.body.string)
for i in soup.body.strings:
    print(i)

for i in soup.body.stripped_strings:
    print(i)


title_tag = soup.title
print(title_tag)
print(title_tag.parent)

a_link = soup.a
for i in a_link.parents:
    if i is None:
        print(i)
    else:
        print(i.name)

#===========================

tt = soup.find_all('b')
print(tt)

t2 = soup.find_all(re.compile('^b'))
print(t2)

t3 = soup.find_all(['a','b'])
print(t3)

def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
t4 = soup.find_all(has_class_but_no_id)
print(t4)