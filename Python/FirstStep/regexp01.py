# [regexp.py]
# coding: utf-8

import re

line = "Beautiful is better than ugly."

matches = re.findall("Beautiful", line)
print(matches)

matches = re.findall("beautiful", line, re.IGNORECASE)
print(matches)




zen = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
"""

m = re.findall("^If", zen, re.MULTILINE)
print(m)

m = re.findall("idea.$", zen, re.MULTILINE)
print(m)


string = "Two too."
m = re.findall("t[ow]o", string, re.IGNORECASE)
print(m)


line = "123 hi 34hello"
m = re.findall("\\d", line, re.IGNORECASE)
print(m)


line = "I love $"
m = re.findall("\\$", line, re.IGNORECASE)
print(m)