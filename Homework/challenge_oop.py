class Account:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return 'Account owner:   {}\nAccount balance: ${}'.format(self.owner, self.balance)

    def deposit(self, amount):
        self.balance += amount

        return 'Deposit Accepted'

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Funds Unavailable!'

        self.balance -= amount

        return 'Withdrawal Accepted'


# 1. Instantiate the class
acct1 = Account('Kolos', 100)
# 2. Print the object
print(acct1)
# 3. Show the account owner attribute
print(acct1.owner)
# 4. Show the account balance attribute
print(acct1.balance)
# 5. Make a series of deposits and withdrawals
print(acct1.deposit(50))
print(acct1.withdraw(75))
print(acct1.withdraw(500))
