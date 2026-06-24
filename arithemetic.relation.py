# 1 (arithmetic)
n=2
s=n*n
c=n*n*n
print(s+c)

# 2 
bal=5000
amt=3500
bal=bal+amt
print(bal)

# 3
a=5
b=3
c=a+b
print(c)

# 4
a=5
b=3
a=b
b=a
print(a,b)

# 5
sum=0
i=1
sum=sum+i
i=i+1
sum=sum+i
i=i+1
sum=sum+i
i=i+1
sum=sum+i
print(sum)
print(i)

# 6 (factorial)
fact = 1
i = 1

fact = fact*i
i=i+1

fact=fact*i
i=i+1

fact=fact*i
i=i+1

fact=fact*i
print(fact)
print(i)

# 7 
n = 2345
sum=0
sum=sum+n%10
n=n/10

sum=sum+n%10
n=n/10

sum=sum+n%10
n=n/10

sum=sum+n%10
n=n/10

print(sum,n)


# 8 
n=2345
rev=0

rev=rev*10+n%10
n=n/10

rev=rev*10+n%10
n=n/10

rev=rev*10+n%10
n=n/10

rev=rev*10+n%10
n=n/10

print(rev,n)

# 9  Program to add two numbers
x=10
y=70
sum=x+y
print(sum)

# 10 program to display quotient and remainder after division
p=6
r=2
quotient=p//r
remainder=p%r
print("quotient=",quotient)
print("remainder=",remainder)

 # 11 program to find the total and average of 3 numbers
x=2
y=3
z=4
total=(x+y+z)
avg=(x+y+z)/3
print(total)
print(avg)

# 12  program to find the square of given number
a=int(input())
b=a*a
print(b)

# 13 program to find the cube of given number
x = 5
y = 3
cube=x**y
print(f"The Cube of Three Numbers {cube}")

# 14 program to find the sum of square and cube of given number
a=6
b=a*a
sum1=b
print(sum1)
n1=4
n2=3
sum2=(n1**n2)
print(sum2)
sum=sum1+sum2
print(sum)

# 15 program to display the last digit of the given number
x=int(input("Enter N:"))
sum=x*(x + 1) // 2
print("Sum =", sum)

# 16 program to swap 2 numbers
a=3
b=9
a,b=b,a
print(a)
print(b)

# 17 program to swap 2 numbers without third variable
a=3
b=9
a,b=b,a
print(a)
print(b)

# 18 calculate the total amount for the given fruits purchased
Apple = 3
kiwi = 4
Orange = 5
total = (Apple * 50) + (kiwi * 100) + (Orange * 30)
print(total)

# 19 calculate the area of the circle
radius = int(input("Enter radius: "))
area = 3.14 * radius * radius
print("Area of Circle =", area)

# 20 Calculate the area of triangle
base=15
height=7
Area=(15*7)/2
print(Area)

# 21 calculate the time taken  using speed and distance
speed=67.5
distance=5.76
print(f"The Time Taken={distance/speed}")

# 22 calculate the speed by using distance and time
distance=45.9
time=34.8
print("The Speed=",(distance/time))

# 23 calculate the distance by using speed and time
speed=56.8
time=25.9
print("The Distance=",(speed*time))
