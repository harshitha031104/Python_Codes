# 1
n=8
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1 or i==j :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("\n--------------------")
    
# 2
n=8
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i+j==n-1 :
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
print("\n-------------------------")
    
# 3
n=8
for i in range(n):
    for j in range(n):
        if i==0 or j==n-1 or i==j :
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
print("\n------------------")


n=8
for i in range(n):
    for j in range(n):
        if j==n-1 or i==n-1 or i+j==n-1:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
print("\n-------------------------")

for i in range(5):
    for j in range(5-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()
print("\n---------------------")

for i in range(1,6):
    for j in range(6-i-1):
        print(" ",end="")
    for k in range(2*i-1):
        print(i,end="")
    print()
print("\n---------------------")

