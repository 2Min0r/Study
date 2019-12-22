# coding: utf-8

def palindprome(s):
    qu = []
    st = []
    for x in s:
        if x.isalpha():
            qu.append(x.lower())
            st.append(x.lower())
    while qu:
        if qu.pop(0) != st.pop():
            return False
    return True

def palindprome2(s):
    start = 0
    end = len(s) - 1
    while start < len(s) and end >= 0:
        if s[start].isalpha() == False:
            start += 1
        elif s[end].isalpha() == False:
            end -= 1
        elif s[start].lower() != s[end].lower():    
            return False
        else:
            start += 1
            end -= 1
    return True


print(palindprome("Wow"))
print(palindprome("Madam, I'm Adam."))
print(palindprome("Madam, I am Adam."))

print(palindprome2("Wow"))
print(palindprome2("Madam, I'm Adam."))
print(palindprome2("Madam, I am Adam."))