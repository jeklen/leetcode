#!/usr/bin/python
# str.split(str="", num=string.count(str))
# str -- 分隔符，默认为所有的空字符，包括空格，换行(\n), 制表符(\t)等
# num -- 分割次数
import re

str = "Line1-abcdef \nLine2-abc \nLine4-abcd";

print(str.split())
print(str.split(' ', 1))

a = 'Beautiful, is; better*tan\nugly'
x = re.split(',|; |\*|\n', a)
print(x)
