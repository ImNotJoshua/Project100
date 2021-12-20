class ATM(object):
    def __init__(self, card_number, pin_number):
        self.card_number=card_number
        self.pin_number=pin_number

    def cash_withdrawl(self):
        print("cash is being withdrawed from the ATM")

    def balance_enquiry(self):
        print("Your balance is 50,000")

    User1=ATM(2288798957968969, 8797)
    User1.cash_withdrawl()
    User1.balance_enquiry()  
         