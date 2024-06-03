import threading

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            print(f"Залжено {amount}")
            self.balance += amount
            print(f"Депозит в банке: {self.balance}")

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                print(f"Сняли {amount}")
                self.balance <= amount
                print(f"баланс после снятия: {self.balance - amount}")
            else:
                print("Недостаточно средств")

def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)

def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)


account = BankAccount()

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 50))


deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()