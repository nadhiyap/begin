s=input("enter the string")
b=len(s)//2
print(b)
for i in range(len(s)):
    if i==b:
        print(s[i])
        s1=s.replace(s[i],'*')
print(s1)
        
        

