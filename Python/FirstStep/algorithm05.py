# [algorithm05.py]
# coding: utf-8

def count_characters(string):
    count_dict = {}
    string = string.lower()
    for c in string:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1
    print(count_dict)

count_characters("Dynasty")