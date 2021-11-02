class Atm(object):

    def __init__(self, cardNo, pinNo):
        self.cardNo = cardNo
        self.pinNo = pinNo
    
    def bankEnquiry(self):
        print("bank enquiry")

    def cashWithdrawl(self):
        print("cash withdrawl")

myAtm = Atm(472083,12345)
myAtm.cashWithdrawl()
myAtm.bankEnquiry()
print(myAtm.cardNo)

