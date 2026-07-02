# 1 Find the length of a tuple.
t = (10, 20, 30, 40, 50)
print(len(t))

# 2 Check whether a given value exists in a tuple.
t = (5, 10, 15, 20)
if 15 in t:
    print("True")
else:
    print("False")
    
    
# using loop
t = (5, 10, 15, 20)
val=False
for  i in t:
    if i==15:
        val=True
        break
if val:
    print("present")
else:
    print("not present")


#  Convert a tuple into a list, add a new element, and convert it back to a tuple.
t=(1,3,5,7,9)
lst=list(t)
lst.append(11)
t=tuple(lst)
print(t)
