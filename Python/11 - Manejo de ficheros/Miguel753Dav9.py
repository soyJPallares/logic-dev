import os

file_name = "Miguel753Dav9.txt"

with open(file_name, "w") as file:
    file.write("Miguel Pallares\n")
    file.write("12\n")
    file.write("Java")

with open(file_name, "r") as file:
    print(file.read())

os.remove(file_name)