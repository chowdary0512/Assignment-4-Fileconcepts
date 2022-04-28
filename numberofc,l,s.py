# 3.    Python – Get number of characters, words, spaces and lines in a file
f=open('abc.txt','r')
data=f.read()
Nc=0
Ns=0
Nw=0
Nl=0
for i in data:
    if i ==' ':
        Ns=Ns+1
    else:
        Nc=Nc+1    
print("No of spaces", Ns)
print("No of characters", Nc)
for i in data.split():
    Nw=Nw+1
print("No of words",Nw)
f=open('abc.txt','r')
line=f.readlines()
for i in line:
    Nl=Nl+1
print("no of lines", Nl)
f.close()