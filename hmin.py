n=int(input("enter n"))
n=n%(24*3600)
h=n//3600
n%=3600
m=n//60
print(h," ",m)
