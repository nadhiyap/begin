a=int(input("enter num"))
b=1
c=0
while a!=0:
    c=a%10
    b=b*c
    a=a//10
print(b)
