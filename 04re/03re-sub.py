import re


regex = re.compile(r'(\w+) (\w+)')
s1 = 'one12twothree34four'
s2 = 'hello hello2 233 456.765'

print(regex.sub(r'qqq qqq',s2))
print(regex.sub(r'\2 \1',s2))

def func(m):
    return 'HI'+ ' '+m.group(1)

print(regex.sub(func,s2,1)) #里面的1代表只替换一次