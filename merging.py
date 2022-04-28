# 9.    Python Program to merge two files into a third file
d1=d2=" "
f1=open('abc.txt','r')
d1=f1.read()
f2=open('Oddlinefile.txt','r')
d2=f2.read()
d1+="\n"
d1+=d2
f3=open('mergedfile.txt','w')
f3.write(d1)
f3.close()
f1.close()
f2.close()
with open('mergedfile.txt','r') as f:
    data=f.read()
    print(data)