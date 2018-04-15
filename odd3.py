a=0
c=0
d=0
n=int(input("enter the n"))
k=int(input("enter the k"))
for i in range(n):
    a=int(input())
    if a%2!=0:
        c=c+1
        if c==k:
            d=a
print(d)
        
        

