n=int(input("enter num"))
l=[]
for i in range(n):
    a=int(input())
    l.append(a)
for j in range(n):
    if j==n-1:
        break
    if l[j]+1==l[j+1]:
        pass
    else:
        print(l[j+1])
        break
        
