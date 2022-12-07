
class ATM:
    def __init__(self, cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
        
        self.person = {
        "cardnumber": self.cardnumber,
        "pin": self.pin
    }
    
    def check_balance(self):
        print("Your balance is 5000")
        
    def cash_withdrawl(self):
        #aaa  
        print("aaa")
              
    def balance_inquiry(self):
        #aaa
        print("aaa")

new_user = ATM(card_number,pin_number)