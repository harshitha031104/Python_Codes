#1 condition for the number divisible by both 2 and 3
a=18
if (a%2==0 & a%3==0):
    print("divisible")
else:
    print("not divisible")
    
    
#2 condition for the number divisible by 4 but not by 6
num=20
if (num%4==0 and num%6!=0):
    print("It is divisible")
else:
    print("not divisible")
    
#3 condition for first number less than the second number and greater than the third munber
num1=5
num2=25
num3=19
if (num1<num2 & num2>num3):
    print("True")
else:
    print("False")
    
    
#4 condition for the number between 20 and 40
x=23
if (20<x<40):
    print("between 20 and 40")
else:
    print("not between 20 and 40")
    
#5 condition for first  num even second num odd
a=2
b=7
if a%2==0 and b%2!=0:
    print("first num even and second num odd")
else:
    print("false")
    
#6 condition for the student score above 35 in all 4 subject
s1=45
s2=56
s3=62
s4=35
if (s1>=35 and s2>=35 and s3>=35 and s4>=35):
    print("Pass")
else:
    print("Fail")
    
#7 condition for the character a vowel 
char='e'
if char in "aeiouAEIOU" :
    print("vowels")


#8 condition for the character an upper case letter
char='H'
if ('A'<=char<='Z'):
    print("upper case")
    
char='S'
if char.isupper():
    print("Upper letter")
    
#9 condition for the character is digit 
num=6
if 0<=num<=9:
    print("Digit")
    
ch='8'
if ch.isdigit():
    print("digit")
    
#10 condition for the pin 4 digit long
num=4560
if 1000<=num<=9999:
    print("pin number")
    
pin=input("Enter PIN: ")
if len(pin)==4 and pin.isdigit():
    print("Valid PIN")
else:
    print("Invalid PIN")
    
    
#11 condition for the character an alphabet letter 
x='8'
if x.isalpha():
    print("True")
else:
    print("False")
    
x='E'
if ('A'<=x<='Z' or 'a'<=x<='z'):
    print("alphabets")
else:
    print("not an alphabets")
    
    
#12 condition for the character a symbol (non alphanumeric)
x='@'
if not x.isalnum():
    print("symbol")
else:
    print("not symbol")
    
#13 condition for the all three numbers equal to each other
a=5
b=5
c=5
if a==b==c:
    print("all 3 numbers are equal")
    
    
#14condition for the atleast two numbers among the three equal to each other
num1=6
num2=9
num3=6
if num1==num2 or num2==num3 or num3==num1 :
    print("At least two number equal")
    
#15 condition for the all three numbers different from each other
a=1
b=17
c=19
if a!=b!=c :
    print("True")

