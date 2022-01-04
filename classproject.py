class Atm(object) :
    def __init__ (self, card, number, bank, membertype) :
        self.card=card
        self.number=number
        self.bank=bank
        self.membertype=membertype
    def Withdrawl(self) :
        amount = input("Enter amount here...")
        print("Card Number: " + self.card)
        print("Atm Pin: " + self.number)
        print("Bank Name: " + self.bank)
        print("Member Type: " + self.membertype)
        print("Amount Withdrawn : " +amount)
        print("Withdrawl Successful! Please Wait to get the money.")

    def CheckBalance(self) : 
        print("Your bank balance is 2,000,000")
Card=Atm("231", '9876', 'CITI','Royal Gold')
Card.Withdrawl()