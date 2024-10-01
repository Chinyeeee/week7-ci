class Current_interest:
    def get_rate():
        pass

class BankAccount:
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name
    
    def deposit(self, amount):
        if type(amount) not in [int, float]:
            raise TypeError("Invalid amount type")
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            raise Exception("Insufficient funds")
        self.balance -= amount

    def compute_interest(self, current_interest):
        return current_interest.get_rate() * self.balance
