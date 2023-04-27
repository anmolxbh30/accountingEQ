# accountingEQ

In this code, we define two classes: AccountingEquation and Transaction. AccountingEquation is the same as in the previous example, 
while Transaction represents a single transaction with an account, amount, and transaction type (debit or credit). It has a method called apply_transaction 
that takes an instance of the AccountingEquation class and updates its values based on the transaction.
The code then prompts the user to enter the number of transactions, and for each transaction, it prompts them to enter the account, amount, 
and transaction type. It creates an instance of the Transaction class with those values and appends it to a list of transactions.
After all transactions have been entered, the code loops through the list of transactions and applies each one to the AccountingEquation 
object using the apply_transaction method. It then calculates the result of the accounting equation using the calculate method and prints it to the user.
This is just a simple example, but you could build on this code to create a more robust accounting equation calculator app with additional features and functionality.
