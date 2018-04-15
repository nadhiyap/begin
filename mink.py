a=0
c=0
l=[]
n=int(input("enter the n"))
k=int(input("enter the k"))
for i in range(n):
    a=int(input())
    l.append(a)
for i in range(k-1):
    c=min(l)
    l.remove(c)
print(min(l))
        
        

