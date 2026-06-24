char=input("Enter character:")
if ('A'<=char<='z') or ('a'<=char<='z'):
    print("alphabets")
elif '0'<=char<='9':
    print("digit")
else:
    print("special character") 
    
    
num1=34
num2=54
num3=78
if num1>num2 and num1>num2:
    print("biggest value:",num1)
elif num2>num1 and num2>num3:
    print("biggest value:",num2)
else:
    print("biggest value:",num3)
