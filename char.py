#2.    Python program to read character by character from a file

with open('abc.txt','r') as f:
    data=f.read()
    for i in data:
        print(i)