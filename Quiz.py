score=0
# Question 1
ans=input("1.What keyword is used to define a function in Python?")
if ans.lower()=="def":
    score+=1
# Question 2
ans=input("2.Which function is used to display output in Python?")
if ans.lower()=="print":
    score+=1
# Question 3
ans=input("3.What symbol is used for comments in Python?")
if ans=="#":
    score+=1
# Question 4
ans=input("4.Which data type is used for whole numbers?")
if ans.lower()=="int":
    score += 1
# Question 5
ans=input("5.Which function is used to take user input?")
if ans.lower()=="input":
    score+=1
# Final Result
print("\nQuiz Completed!")
print("Your Score:",score,"/5")
if score==5:
    print("Excellent!")
elif score>=3:
    print("Good Job!")
else:
    print("Keep Practicing!")
