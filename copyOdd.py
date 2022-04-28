# 8.    Python program to copy odd lines of one file to other
f1=open('abc.txt','r')
f2=open('Oddlinefile.txt','w')
line=f1.readlines()
for i in range(0,len(line)):
    if (i % 2 == 0):
        f2.write(line[i])
    else:
        pass
f1.close()
f2.close()

with open('Oddlinefile.txt','r') as f3:
    data=f3.read()
    print(data)