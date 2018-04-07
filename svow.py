a=input("enter a string ")
b=['a','e','i','o','u']
c=0
for i in range(len(a)):
    if a[i] in b:
        c=1
if c==1:
    print("yes")
else:
    print("no")
    
