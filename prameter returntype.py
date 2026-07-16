# 1
def simple_interest(principal,rate,time):
    interest=(principal*rate*time)/100
    print("simple interest:",interest)
    return interest
simple_interest(40000,1,12)

# 2
def average_numbers():
    n1=23
    n2=98
    n3=44
    avg=(n1+n2+n3)/3
    return avg
result=average_numbers()
print("average numbers:",result)

# 3
def biggest_numbers(a,b,c):
    if a>b and a>c:
        print(a,"is the biggest")
    elif b>a and b>c:
        print(b,"is the biggest")
    else:
        print(c,"is the biggest")
biggest_numbers(43,88,103)

# 4
def vote_valid():
    n=int(input("Enter the age:"))
    if n>=18:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")
vote_valid()
    
