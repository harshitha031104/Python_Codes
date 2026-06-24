#1
for i in range(1,6):
    for j in range(i):
        if i%2==0:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()
print("\n-----------------")
    
# 2
for i in range(5,0,-1):
    for j in range(i):
        if i%2==0:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()
print("\n-------------------")

#3
for i in range(1,6):
    for j in range(i):
        if j%2==0:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()
print("\n------------------")

#4
for i in range(1,6):
    for j in range(1,i+1):
        if (i+j)%2==0:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print() b
