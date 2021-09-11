import os

def getExtension(file):
    return os.path.splitext(file)[1]

file = input("Enter file name with extension: ")
print(getExtension(file))
