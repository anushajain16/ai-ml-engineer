# Day 4 Exercise 1: Read a file

with open("sample.txt", "r", encoding="utf-8") as file:
    contents = file.read()
    print(contents)
