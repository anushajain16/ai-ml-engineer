# Day 4 Exercise 2: Write to a file

with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Hello from Python file I/O practice.\n")

print("File written successfully.")
