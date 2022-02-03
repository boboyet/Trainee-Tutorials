#Banking system with Oop ----- done
#Parent class: user ------ done
#Holds details about user 
#Has a functioin to show user details 
#Child class: Bank
#Stores details about account balance 
#Stores details about amount
# Allows for deposits, withdraw, view_balance


#PARENT CLASS
class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
     
    def show_details(self):
        print("Personal Details")
        print("")
        print("Name", self.name)
        print("Age", self.age)
        print("Gender", self.gender)

#CHILD CLASS
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("Account balance has been updated : $", self.balance)

    def withdraw(self):
        amount = float(input("Enter amount to be deposited: "))
        if amount > self.balance :
            print("Insufficient Funds | Available Balance : $", self.balance)
        else :
            self.balance -= amount
            print("Account Bakance is Updated : $", self.balance)

    def view_balance(self):
        self.show_details()
        print("Your Account Bakance : $", self.balance)




