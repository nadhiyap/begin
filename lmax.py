n=int(input("enter n"))
n1=int(input("enter n1"))
l=[]
for i in range(1,n1):
    if n%i==0 and n1%i==0:
        l.append(i)
print(max(l))
