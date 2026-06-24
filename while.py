# program to check the number contains zero or not
n=321875
temp=n
while temp>0:
    if temp%10==0:
        print("Number contains 0")
        break
    temp//=n
else:
    print("Number does not contain 0")
    
#program to find the average of all digits in the given number
n=4563
temp=n
sum_digits=0
count=0
while temp>0:
    digit=temp%10
    sum_digits+=digit
    count+=1
    temp//=10
average=sum_digits / count
print("Average of digits =", average)

#program to find the second largest digit in the given number
