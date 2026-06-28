#1 multiplication table in last digit
arr=[3,7,8,2,5,6,4]
n=arr[-1]
print(n)
for i in range(1,11):
    print(n,"*",i,"=",n*i)
print("\n-------------------")

#2 
arr=[3,7,8,2,5,6,4]
mid=len(arr)//2
print(mid)
print("\n------------------------")

# 3
arr=[3,7,8,2,5,6,4,9]
print(len(arr))
mid=len(arr)//2
print(arr[3],arr[4])
print("sum of two middle elements:",arr[3]+arr[4])
print("\n--------------------")

# 4
arr=[3,7,8,2,5,6,4]
total=0
for i in arr:
    total=total+i
print(total)
print("\n-------------------")


# 5
arr=[3,7,8,2,5,6,4]
for even_num in arr:
    if even_num%2==0:
        print(even_num)
print("\n---------------------")

# 6
arr=[3,7,8,2,5,6,4]
total=0
for even_num in arr:
    if even_num%2==0:
        total=total+even_num
print(total)
print("\n-----------------")

# 7
a=5
b=10
temp=a
a=b
b=temp
print("a=",a)
print("b=",b)
print("\n-----------------")


# 7
arr=[3,7,8,2,5,6,4]
for i in arr:
    temp=arr[0]
    arr[0]=arr[-1]
    arr[-1]=temp
print(arr)
print("\n----------------")

# 8
arr=[3,7,8,2,5,6,4]
largest_num=arr[0]
for i in arr:
    if i>largest_num:
        largest_num=i
print("largest number:",largest_num)
    
# 9 
arr=[3,7,8,2,5,6,4]
smallest_num=arr[0]
for i in arr:
    if i<smallest_num:
        smallest_num=i
print("smallest number:",smallest_num)
    
    
# 10
arr=[3,7,8,2,5,6,4]
for i in arr[-1:-len(arr)-1:-1]:
    if i%2==0:
        print("first even number:",i)
    break
print("\n---------------------")

# 11
arr=[3,7,8,2,5,6,4]
for i in arr:
    if i%2==0:
        print("first even number:",i)
        break
print("\n------------------")

# 12
arr=[3,7,8,2,5,6,4]
largest = arr[0]
smallest = arr[0]
for i in arr:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i             # find largest and smallest values
for i in range(len(arr)):
    if arr[i] == largest:
        max_index = i
    if arr[i] == smallest:
        min_index = i
arr[max_index], arr[min_index] = arr[min_index], arr[max_index]

print("Updated list:", arr)
