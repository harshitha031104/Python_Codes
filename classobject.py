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
