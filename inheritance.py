# single level inheritance
class Animal:
    def eat(self):
        print("All animals are eating biryani...")
class tiger(Animal):
    def hunt(self):
        print("Tiger hunting deer eat flush... ")
a1=Animal()
a1.eat()
t1=tiger()
t1.eat()
t1.hunt()

class student:
    def insertstudent(self,sid,name,courseName,fee):
        self.sid=sid
        self.name=name
        self.courseName=courseName
        self.fee=fee
    def printstudent(self):
        print(self.sid,self.name,self.courseName,self.fee)
class result(student):
    def insertmarks(self,s1,s2,s3):
        self.s1=s1
        self.s2=s2
        self.s3=s3
    def printresult(self):
        print(self.s1)
        print(self.s2)
        print(self.s3)
        self.total=self.s1+self.s2+self.s3
        self.avg=self.total/3
        print(self.total,"and",self.avg)
        if self.avg>=70:
            print("A grade")
        elif self.avg>=60:
            print("b grade")
        elif self.avg>50:
            print("C grade")
        else:
            print("D grade")
        if self.s1>=35 and self.s2>35 and self.s3>=35:
            print("Pass")
        else:
            print("Fail")
r1=result()
r1.insertstudent(111,"Harshi","python",2500.00)
r1.insertmarks(90,70,37)
r1.printstudent()
r1.printresult()

# 2 multi level inheritance
class  vivo1:
    def call(self):
        print("making a call...")
    def sms(self):
        print("sending msg...")
class vivo2(vivo1):
    def radio(self):
        print("play mp3 music..")
class vivo3(vivo2):
    def youtube(self):
        print("playing videos and audio with youtube...")
    def word_doc(self):
        print("read aa word document..")
v1=vivo1()
v1.call()
v1.sms()
print("----------------vivo2---------------")
v2=vivo2()
v2.call()
v2.sms()
v2.radio()
print("-----------vivo3-----------")
v3=vivo3()
v3.call()
v3.sms()
v3.radio()
v3.youtube()
v3.word_doc()


# 3 hierachical inhertance
class mi:
    def call(self):
        print("Making a call....")
class mi1(mi):
    def sms(self):
        print("sending sms...")
class mi2(mi):
    def radio(self):
        print("play radio music....")
m1=mi1()
m1.call()
m1.sms()
print("========mi1======")
m2=mi2()
m2.call()
m2.radio()
print("=======mi2==========")


# 4 multiple inheritance
class father:
    def birth(self):
        print("father birth year 1990")
class mother:
    def birthday(self):
        print("mother birthday in november")
class child(father,mother):
    def age(self):
        print("age of the child")
ch1=child()
ch1.birth()
ch1.birthday()
ch1.age()


# 5 hybrid inheritance
class laptop1:
    def asus(self):
        print("useful for gaming..")
class laptop2(laptop1):
    def hp(self):
        print("useful for coding..")
class laptop3(laptop1):
    def lenovo(self):
        print("working useful for both..")
class laptop4(laptop2,laptop3):
    def dell(self):
        print("useful for storage..")
l1=laptop2()
l1.asus()
l1.hp()
print("--------laptop1--------")
l2=laptop3()
l2.asus()
l2.lenovo()
print("=======laptop2=========")
l3=laptop4()
l3.hp()
l3.lenovo()
l3.dell()
print("========laptop3=========")


# super variable
class person:
    def __init__(self):
        self.name="Rambabu"
class customer(person):
    def __init__(self):
        super().__init__()
        self.parent_name=self.name
        self.name="Harshi"
    def display(self):
        print("parent_name:",self.parent_name)
        print("child name:",self.name)
c1=customer()
c1.display()


class person:
    def __init__(self,pid,name):
        self.pid=pid
        self.name=name
class customer(person):
    def __init__(self,pid,name,age,gender):
        super().__init__(pid,name)
        self.age=age
        self.gender=gender
    def display(self):
        print(self.pid,self.name,self.age,self.gender)
c1=customer(101,"prasad",23,"male")
c1.display()
c2=customer(111,"ram",30,"male")
c2.display()

# super method
class person:
    def display(self):
        print("this is a super class method")
class customer(person):
    def display(self):
        super().display
        print("This is a sub class method")
c1=customer()
c1.display()
        

