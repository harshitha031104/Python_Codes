class calc:
    def add(self,n1,n2):
        self.addition=self.n1+self.n2
        print(self.addition)
    def add(self,n1,n2,n3):
        self.addition=self.n1+self.n2,self.n3
        print(self.addition)
c1=calc()
c1.add()
c1.add()

# polymorphison
class payment:
    def pay(self):
        print("processing the payments..")
class creditcardpayment(payment):
    def pay(self):
        super().pay()
        print("processing creaditcard payment")
class upipayment(creditcardpayment):
    def pay(self):
        super().pay()
        print("processing upi payment")
c1=creditcardpayment()
c1.pay()
upi=upipayment()
upi.pay()
