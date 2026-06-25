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
    

