#4. Python program to Count the Number of occurrences of a key-value pair in a text file

#f=open('dict.txt','a')
#f.write("Coin:H\n")
#f.write("Coin:T\n")
#f.write("Coin:H\n")
#f.write("Coin:T\n")
#f.write("Coin:H\n")
#f.write("Coin:Ht\n")
#f.write("Coin:HH\n")
#f.write("Coin:HTH\n")
#f.write("Coin:HHT\n")
#f.write("Coins\n")
#f.close()
f=open('dict.txt','r')
d=dict()
for r in f:
    lines=r.split()
    for line in lines:
        if line in d:
            d[line]=d[line]+1
        else:
            d[line]=1
f.close()

for key in list(d.keys()):
    print("The count of {} is {}".format(key,d[key]))