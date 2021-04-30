string= input("Enter a string :")

count ={}
for x in string:
    if x in string:
        if x in count.keys():
            count[x]+=1
        else:
            count[x]=1

for x in count.keys():
    print(x, "= 0", count[x])
