n=5
for i in range(1,11):
    print(f"{n}*{i}={n*i}")
    
# 2    
n=5
for i in range(1,11):
    print(n,"*",i,"=",n*i)
    
# 3
for i in range(122,96,-1):
    print(chr(i),end=" ")
print("\n------------------")

#  4
num=int(input("Enter a number:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("Factorial:",fact)

# 5
a=input("Enter a string: ")
print(a[::-1])

# 6
a=input("Enter a string: ")
reverse=""
for i in a:
    reverse=i+reverse
print(reverse)
