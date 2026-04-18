# op_masala

class BankHisob:
    def __init__(self, ism, balans, karta_raqam):
        self.ism = ism
        self.balans = balans
        self.karta_raqam = karta_raqam

    def deposit(self, amount):
        self.balans += amount
        return f"Yangi balans: {self.balans}"

    def withdraw(self, amount):
        if self.balans >= amount:
            self.balans -= amount
            return f"Yechildi. Qolgan balans: {self.balans}"
        else:
            return "Yetarli mablag‘ yo‘q"

    def check_balance(self):
        return f"Hozirgi balans: {self.balans}"



account1 = BankHisob("Ali", 100000, "8600123412341234")

print(account1.deposit(50000))
print(account1.withdraw(120000))
print(account1.check_balance())
