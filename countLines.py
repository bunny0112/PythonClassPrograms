fp=open("example file","r")
words=[]
count=0
for i in fp:
    words=words+i.split(" ")
for i in words:
    count=count+1
print(count)