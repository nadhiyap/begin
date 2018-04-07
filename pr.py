a=int(input("enter a n1"))
b=1
for i in range(2,a):
    if(a%i==0):
        print("not a prime")
        b=0
        break
if b==1:
    print("prime")
