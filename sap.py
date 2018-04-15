n=int(input("enter n"))
a=int(input("enter a"))
d=int(input("enter d"))
s=0
for i in range(1,n+1):
    s=s+(a+(i-1)*d)
print(s)
