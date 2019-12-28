# [file01.py]
# coding: utf-8

import os
print(os.path.join("Users", "bob", "st.txt"))

st = open("st.txt", "w")
st.write("Hi from Python!")
st.close()

with open("st.txt", "w") as f:
    f.write("Hi from Python!")

with open("st.txt", "r") as f:
    print(f.read())