#10.    Python program to Reverse a single line of a text file

with open('abc.txt','r') as f:
    lines=f.readlines()
n=1
line=lines[n].split()
R=" ".join(line[::-1])
print("Reversed line:",R)
lines.pop(n)
lines.insert(n,R)
f1=open('reverse.txt','w')
f1.writelines(lines)
f1.close()