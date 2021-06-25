import os

filename = input("Filename whose path you want to take out: ")
print("Path of the directory from which the search should begin")

# if user doesn't enter anything then root directory will be used
path = input("(Press Enter to start from root directory): ") or os.path.abspath(os.sep)

