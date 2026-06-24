# Arthimetic Operators(if condition)

# 1 Program to add two numbers
n1=87
n2=99
if (n1+n2):
   print(n1+n2)
else:
   print("False")

# 2 program to display quotient and remainder after division
a = 7
b = 9
if a > 0 and b > 0:
    print("Quotient =", a // b)
    print("Remainder =", a % b)

# 3 program to find the total and average of 3 numbers
n1 = 5
n2 = 7
n3 = 8
total = n1 + n2 + n3
average = total / 3
if average > 0:
    print("Total =", total)
    print("Average =", average)

# 4 program to find the square of given number
n = 5
if n > 0:
    print("Square =", n*n)

# 5 program to find the cube of given number
a = 6
if a > 0:
   print("Cube=",a**3)	

# 6 program to find the sum of square and cube of given number
a = 5
if a > 0:
    print((a * 2) + (a * 3))

# 7 program to display the last digit of the given number
n = 2345
if n > 0:
    print("Last Digit =", n % 10)

# 8 program to swap 2 numbers
a = 5
b = 9
if True:
    a, b = b, a
    print(a, b)

# 9  program to swap 2 numbers without third variable
a = 5
b = 9
if a != b:
    a = a + b
    b = a - b
    a = a - b
    print("a =", a)
    print("b =", b)

# 10 calculate the total amount for the given fruits purchased
Apple = 3
kiwi = 4
Orange = 5
if Apple > 0 and kiwi > 0 and Orange > 0:
    total = (Apple * 50) + (kiwi * 100) + (Orange * 30)
    print("Total Amount =", total)

# 11 calculate the area of the circle
radius = int(input("Enter radius: "))
if radius > 0:
    area = 3.14 * radius * radius
    print("Area of Circle =", area)

# 12 Calculate the area of triangle
base = 15
height = 7
if base > 0 and height > 0:
    Area = (base * height) / 2
    print("Area =", Area)

# 13 calculate the time taken  using speed and distance
speed = 67.5
distance = 5.76
if speed > 0:
    print("The Time Taken =", distance / speed)

# 14 calculate the speed by using distance and time
distance=45.9
time=34.8
if time > 0:
   print("The Speed=",distance/time)

# 15 calculate the distance by using speed and time
speed=56.8
time=25.9
if speed > 0 , time > 0:
print("The Distance=",(speed*time))
