# Day 4 Exercise 3: Safe file handling

try:
    with open("missing_file.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found. Please check the path.")
