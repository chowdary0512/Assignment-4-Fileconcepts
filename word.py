# 1.    Python program to read file word by word
#f=open('abc.txt','w')
#f.write("Hi Drakshayani\n")
#f.write("good morning\n")
#f.write("welcome to python\n")
#f.close()
f=open('abc.txt','r')
R=f.read()
for i in R.split(' '):
    print(i)
f.close

