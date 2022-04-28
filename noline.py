# 5.    Count number of lines in a text file in Python

with open('abc.txt','r') as f:
    data=f.readlines()
    N=0
    for line in data:
        print(line)
        N+=1
    print(N)