import dz_bank

class CheckingAccount(dz_bank.BankAccount):
    def __init__(self, withdraw, deposit, ans):
        dz_bank.BankAccount.__init__(self, 18000, "Vikroriia") 
        self.withdraw = withdraw
        self.deposit = deposit
        if ans == "Т":
            print(f"Грошей на депозиті - {self.deposit}\nБаланс - {self.balance}\nВласник - {self.owner}\n")
        else:
            pass

class SavingsAccount(dz_bank.BankAccount):
    def __init__(self, withdraw, deposit):
        self.withdraw = withdraw
        self.deposit = deposit

ans = input("Перевірити банківський рахунок? (Т/Н) - ")
CheckingAccount2 = CheckingAccount(1000, 5600, ans)
SavingsAccount2 = SavingsAccount(1000, 5600)