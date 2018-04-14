a=int(input("enter num1"))
b=int(input("enter num2"))
l=[]
for i in range(1,a):
    if a%i==0 and b%i==0:
        l.append(i)
print(max(l))
