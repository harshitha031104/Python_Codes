1:# functions
def add_numbers():
    n1=34
    n2=56
    add=n1+n2
    print("sum of two numbers:",add)
add_numbers()

#2
def even_odd():
    n=int(input("Enter a number: "))
    if n%2==0:
        print("even")
    else:
        print("odd")
even_odd()

# 3
def biggest_number():
    n1=int(input("Enter a n1 number: "))
    n2=int(input("Enter a n2 number: "))
    n3=int(input("Enter a n3 number: "))
    if n1>n2 and n1>n3:
        print("n1 is the biggest")
    elif n2>n1 and n2>n3:
        print("n2 is the biggest")
    else:
        print("n3 is the biggest")
biggest_number()

# 4
def simple_interest(principal,rate,time):
    interest=(principal*rate*time)/100
    return(interest)
result=simple_interest(100000,1.5,7)
print("simple_interest",result)


def average_numbers(a,b,c,d):
    avg=(a+b+c+d)/4
    print("average of 4 numbers:",avg)
average_numbers(34,76,98,20)

def vote_valid(n):
    if n>=18:
        print("Eligible to vote")
    else:
        print("not eligible to vote")
vote_valid(34)
