# 1  positionn parammeters
def employee(eid, ename,salary):
    print(f"employee Id:,{eid}")
    print(f"employee Name:{ename}")
    print(f"employee salary:{salary}")
employee(101,"harshitha",50000)

# 2 `keywords parameters
def employee(ename,eid,salary):
    print(f"employee Name:{ename}")
    print(f"employee salary:{salary}")
    print(f"employee Id:,{eid}")
employee(salary=50000,ename="hari",eid=105)

# 3
def employee(eid,name,salary,companyname='tcs'):
    print(f"employee id:{eid},name:{name},salary:{salary},comapanyname:{companyname}")
employee(103,"john",13000)
employee(105,"harshi",15000,"wipro")

# 4
def g1(*args):
    total=0
    for num in args:
        total+=num
    print(total)
g1(3,7,8)
g1(3,66,5,34,88)

# 5
def student(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
student(id=109,name="harshi",age=20,marks=90)

