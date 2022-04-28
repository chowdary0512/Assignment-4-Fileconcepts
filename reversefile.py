# 11. Python program to reverse the content of a file and store it in another file
f1=open('reversefile.txt','w')
with open('abc.txt','r') as file:
    data=file.read() 
    # data=file.readlines()
    R=data[::-1]
f1.write(R)   
#f1.writelines(R)
f1.close()
with open('reversefile.txt','r') as f:
    data=f.read()  
    print(data)