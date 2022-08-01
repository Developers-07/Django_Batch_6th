
from customer_implement import CustomerImplement
from bank_account import BankAccount

c1 = CustomerImplement("Zishan","01752188022","zishanc901@gmail.com","Dhaka")
c2 = CustomerImplement("Razib","01921819801","razibul15-11649@diu.edu.bd","Rangpur")

print(c1)
print(c2)

acc = BankAccount("Faruk","01732994411","faruk15-11737@diu.edu.bd","Nilfamari",100000,250000,75000)

print("Balance =",acc.get_balance()," Deposit taka =",acc.get_deposit()," Final Amount I have =",acc.get_present_amount())


