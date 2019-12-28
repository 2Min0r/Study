# [practice08.py]
# coding: utf-8

import csv

with open("../diary.txt", "r") as f:
    print(f.read())

answer = input("What's your favorite animal?")
with open("fav_animal.txt", "w") as f:
    f.write(answer)

movies = [["Top Gun", "Risky Business", "Minority Report"],
["Titanic", "The Revenant", "Inception"],
["Training Day", "Man on Fire", "Flight"]]

with open("movies.csv", "w") as f:
    write = csv.writer(f, delimiter = ",")
    for movie in movies:
        write.writerow(movie)