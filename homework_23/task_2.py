"""
2. შექმენით კლასი BankAccount, რომელსაც ექნება შემდეგი protected ველები:
• _balance (ანგარიშის ბალანსი)
კლასს უნდა ჰქონდეს შემდეგი მეთოდები:
1. კონსტრუქტორი, რომელიც იღებს საწყის ბალანსს.
2. მეთოდი deposit(amount), რომელიც ამატებს თანხას ბალანსზე.

3. მეთოდი withdraw(amount), რომელიც ამცირებს ბალანსს. თუ თანხა საკმარისი არ არის, 
უნდა დაბეჭდოს შეტყობინება: “საკმარისი თანხა არ არის” და არ შეცვალოს ბალანსი.
4. მეთოდი get_balance(), რომელიც აბრუნებს ბალანსს.
დავალება:
შექმენით ერთი ობიექტი კლასიდან BankAccount, შეიტანეთ მასში თანხა, გამოტანეთ თანხა 
და დააკვირდით, როგორ მუშაობს ენკაფსულაცია.
"""

class BankAccount:
    def __init__(self,balance = 0):
        self._balance = balance
        
    @property
    def balance(self):
       return self._balance
   
    def deposit(self,amount):
        if amount > 0:
            self._balance += amount
            print(f"amount {amount} : new balance {self._balance}")
        else:
            print("amount must be positive")
            
    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f"Withdraw {amount}. New balance: {self._balance}")
        else:
            print("insufficient fund")
    
    def get_balance(self):
        return self._balance
def main():
    bank = BankAccount(100)
    bank.deposit(200)
    bank.withdraw(400)
    
    print(f"Existing balance using property - {bank.balance}")
    print(f"Existing balance using getbalance method - {bank.get_balance()}")
  
if __name__ == "__main__":
    main()