list=[10,20,30,40,50]
print(type(list[0]))
print(list)

# 2
prices=[12.00,560.00,456.0,543.0]
print(type(prices[1]))
student=[111,"shiva","python",4500.0,"A"]
print(student)

# 3  eval() function
names=eval(input("Enter your names: "))
print(names)

# 4
even_nums=list(range(2,30,2))
print(even_nums)
print(type(even_nums))

list=[100,200,300,400,500,600,700,800,900,1000]
print(list[0:9])
print(list[5])
print(list[9])
print(list[-2])

# slicing
list=[100,200,300,400,500,600,700,800,900,1000]
print(len(list))
print(list[::])
print(list[0:6])
print(list[-1:-11:-1])
print(list[0:6:2])
print(list[-1:-8:-2])

animals=['tiger','lion','fox','rabbit','dog','cat','rat','cat','elephant']
print(animals[0:9])
print(animals[::])
print(animals[0:9:2])
print(animals[-1:-9:-2])
print(animals[-1:-8:-4])

# With for loop
animals=['tiger','lion','fox','rabbit','dog','cat','rat','cat','elephant']
for animal in animals:
    print(animal,end=" ")
print("\n----------------")
    
animals=['tiger','lion','fox','rabbit','dog','cat','rat','cat','elephant']
length=len(animals)
for animal in animals[-1:-length:-1]:
    print(animal,end=" ")
    
animals=['tiger','lion','fox','rabbit','dog','cat','rat','cat','elephant']
for animal in animals:
    print(animal.upper(),end=" ")
    
    
animals=['tiger','lion','fox','rabbit','dog','cat','rat','cat','elephant']
for animal in animals:
    if animal.startswith("r"):
        print(animal,end=" ")
    
# 1 Find the sum of all elements in a list.
num=[10,20,30,40,50]
print(sum(num))

# 2 Find the maximum and minimum elements in a list.
num=[12,45,7,89,23]
print(max(num))
print(min(num))

# 3 Reverse a list.
fruits = ["apple", "banana", "mango", "orange"]
print(fruits[-1:-5:-1])

# 4 Print only the even numbers from a list.
nums = [2, 5, 8, 11, 14, 17, 20]
for even_num in nums:
    if even_num%2==0:
        print(even_num)
        
# 5 Remove duplicate elements from a list.
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_num=list(set(numbers))
print(unique_num)

# using loop
numbers=[1,2,2,3,4,4,5]
unique_num=[]
for num in numbers:
    if num not in unique_num:
        unique_num.append(num)
print(unique_num)


# using loop for sum of numbers
num=[10,20,30,40,50]
total=0
for i in num:
    total=total+i
print(total)


# using loop for max and min
num=[12,45,7,89,23]
lar_ele=num[0]
for i in num:
    if i>lar_ele:
        lar_ele=i
print(lar_ele)


num=[12,45,7,89,23]
sma_ele=num[0]
for i in num:
    if i<sma_ele:
        sma_ele=i
print(sma_ele)
