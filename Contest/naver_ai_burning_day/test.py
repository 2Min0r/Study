# coding: utf-8

import gensim
import os

model = gensim.models.Word2Vec.load(r"C:\Users\LG\Desktop\Study\Contest\naver_ai_burning_day\ko.bin")

result = model.wv.most_similar("긍정적")
print(result)
