# 1 print "Hello, World!".
def statement():
    print("Hello World")
statement()

# Write a function that takes two numbers as arguments and returns their sum.
def sum(a,b):
    add=a+b
    print("sum of two numbers:",add)
    return add
sum(40,40)

# 3 Write a function to find the square of a number.
def squ(n):
    square=n**2
    print("Square of number:",square)
squ(6)


# 4 Write a function that checks whether a number is even or odd.
def even_odd(i):
    if i%2==0:
        print("Even")
    else:
        print("Odd")
even_odd(8)
    
    
# Write a function to calculate the factorial of a number.
def factorial():
    n=int(input("Enter a number: "))
    fact=1
    for i in range(1,n+1):
        fact=i*fact
    print(fact)
factorial()
