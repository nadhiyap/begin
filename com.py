n=int(input("enter n"))
b=1
for i in range(2,n):
    if n%i==0:
        print(i)
        b=0
if b==0:
    print("yes")
else:
     print("no")
