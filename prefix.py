# 6.    Python Program to remove lines starting with any prefix
f1=open('abc.txt','r')
f2=open('prefixremoved.txt','w')
for line in f1.readlines():
    if not (line.startswith('good')):
        print(line)
        f2.write(line)
f1.close()
f2.close()