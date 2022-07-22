#Parent class :user
#Hold details about an user
#Has a function to show user details
#child class :bank
#Store details about the account balance
#Stores details about the amount
#Allow for deposits,withdraw,view_balance


#Parent Class
class user():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def show_details(self):
        print("Personal Details")
        print("")
        print("Name ",self.name)
        print("age     ", self.age)
        print("gender", self.gender)

#Child Class

class Bank(user):
     def __init__(self,name,age,gender):
          super().__init__(name,age,gender)
          self.balance=0

     def deposit(self,amount):
         self.amount  =  amount
         self.balance  = self.balance+self.amount
         print("Account balance has been updated: Rs.",  self.balance)

     def withdraw(self,amount):
         self.amount = amount
         if self.amount > self.balance:
             print("Insufficient Balance ! Available Balance: Rs.",  self.balance)
         else:
             self.balance = self.balance - self.amount
             print(" Account Balance Has been Updated: Rs.", self .balance)


     def view_balance(self):
             self.show_details()
             print(" Account Balance Has been Updated: Rs.", self .balance)
  
     
          
        



         
        
        
        
