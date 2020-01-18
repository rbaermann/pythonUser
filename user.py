class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0
    
    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdraw(self, amount):
        if((self.balance - amount) >= 0):
            self.balance -= amount
        else:
            print(f'{self.name} has insufficient funds')
        return self

    def display_user_balance(self):
        return(f'User: {self.name}, Balance: {self.balance}')

    def transer_money(self, recipient, amount):
        if((self.balance - amount) >= 0):
            self.balance -= amount
            recipient.balance += amount
            return (f'User {self.name}, Balance: {self.balance}, User: {recipient.name}, Balance: {recipient.balance}')
        else:
            return f'{self.name} has insufficient funds'

urgot = User('Urgot')
tryndamere = User('Tryndamere')
teemo = User('Teemo')

print(teemo.make_deposit(100).make_deposit(200).make_deposit(300).make_withdraw(150).display_user_balance())

print(tryndamere.make_deposit(500).make_deposit(290).make_withdraw(10).make_withdraw(79).display_user_balance())

print(urgot.make_deposit(900).make_withdraw(500).make_withdraw(300).make_withdraw(300).display_user_balance())

print(urgot.transer_money(teemo, 50))