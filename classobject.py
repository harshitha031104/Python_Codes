class student:
    def insert(self,sid,name,fee):
        self.sid=sid
        self.name=name
        self.fee=fee
    def printstudent(self):
        print(f"sid:{self.sid},name:{self.name},fee:{self.fee}")
s1=student()
s1.insert(101,"Harshi",25000.00)
s1.printstudent()
s2=student()
s2.insert(102,"yogitha",20000.0)
s2.printstudent()


# 2
class employee:
    def __init__(self,eid,name,salary):
        self.eid=eid
        self.name=name
        self.salary=salary
    def printemployee(self):
        print(f"eid:{self.eid},name:{self.name},salary:{self.salary}")
s1=employee(101,"prasad",50000.0)
s1.printemployee()
s2=employee(102,"Harshi",60000.0)
s2.printemployee()


class student:
    def __init__(self,sid,name,fee):
        self.sid=sid
        self.name=name
        self.fee=fee
    def printstudent(self):
        print(f"{self.sid},{self.name},{self.fee}")
s1=student(501,"Harshi",25000)
s1.printstudent()
s2=student(502,"yogi",30000)
s2.printstudent()

# biggest of three  numbers
class biggestnumber:
    def __init__(self):
        self.n1=int(input("Enter n1 number: "))
        self.n2=int(input("Enter n2 number: "))
        self.n3=int(input("Enter n3 number: "))
    def printbiggestnumber(self):
        if self.n1>self.n2 and self.n1>self.n3:
            print(self.n1,"is the biggest")
        elif self.n2>self.n1 and self.n2>self.n3:
            print(self.n2,"is the biggest")
        else:
            print(self.n3,"is the biggest")
b1=biggestnumber()
b1.printbiggestnumber()
        
