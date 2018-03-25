a=int(input("enter num1"))
n=""
while(a!=0):
    n=n+' '+str(a%10)
    a=a//10
print(n[::-1])
