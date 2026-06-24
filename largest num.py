#1
num=35
if num%2==0:
    print("Even")
else:
    print("Odd")
    
#2
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if a>=b and a>=c :
    print("largest number:",a)
elif b>=a and b>=a:
    print("largest number:",b)
else:
    c>=a and c>=b
    print("largest number:",c)
    
    
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
largest=max(a,b,c)
print("largest number:",largest)
