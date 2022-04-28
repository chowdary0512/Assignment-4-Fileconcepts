# 7.    Python – Append content of one text file to another
f1=open('a.txt','a') # new file
f2=open('abc.txt','r')
for line in f2:
    f1.write(line)
f1.close()
f2.close()
f1=open('a.txt','r')
data=f1.read()
print(data)
f1.close()