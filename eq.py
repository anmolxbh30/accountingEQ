class AccountingEquation:
    def __init__(self, assets, liabilities, capital):
        self.assets = assets
        self.liabilities = liabilities
        self.capital = capital

    def calculate(self):
        return self.assets - self.liabilities - self.capital

class Transaction:
    def __init__(self, account, amount, transaction_type):
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type

    def apply_transaction(self, equation):
        if self.transaction_type == "debit":
            if self.account == "assets":
                equation.assets += self.amount
            elif self.account == "liabilities":
                equation.liabilities -= self.amount
            elif self.account == "capital":
                equation.capital -= self.amount
        elif self.transaction_type == "credit":
            if self.account == "assets":
                equation.assets -= self.amount
            elif self.account == "liabilities":
                equation.liabilities += self.amount
            elif self.account == "capital":
                equation.capital += self.amount

print("Welcome to the Accounting Equation Calculator")

equation = AccountingEquation(0, 0, 0)

while True:
    transactions = []

    num_transactions = int(input("Enter the number of transactions: "))

    for i in range(num_transactions):
        account = input("Enter the account (assets, liabilities, or capital): ")
        amount = float(input("Enter the amount: "))
        transaction_type = input("Enter the transaction type (debit or credit): ")

        transaction = Transaction(account, amount, transaction_type)
        transactions.append(transaction)

    for transaction in transactions:
        transaction.apply_transaction(equation)

    result = equation.calculate()

    print("The accounting equation result is:", result)

    another_calculation = input("Would you like to perform another calculation? (y/n) ")
    if another_calculation.lower() == 'n':
        break

print("Thank you for using the Accounting Equation Calculator!")
