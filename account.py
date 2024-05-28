class Account:
    def __init__(self, number, pin, owner_name, owner_address, minimum_balance=0):
        self.number = number
        self.__pin = pin
        self.__balance = 0
        self.owner_name = owner_name
        self.owner_address = owner_address
        self.transactions = []
        self.__overdraft_limit = 0
        self.__interest_rate = 0
        self.__is_frozen = False
        self.__minimum_balance = minimum_balance
        
    def show_balance(self, pin):
        if pin == self.__pin:
            return self.__balance
        else:
            return "Wrong pin"
        Balance
        
    def show_balance(self, pin):
        if pin == self.__pin:
            if self.__is_frozen:
                return "Account is frozen"
            return self.__balance
        else:
            return "Wrong pin"
        
    def view_account_details(self, pin):
        if pin == self.__pin:
            return {
                "Account Number": self.number,
                "Owner Name": self.owner_name,
                "Owner Address": self.owner_address,
                "Balance": self.__balance,
                "Frozen": self.__is_frozen
            }
        else:
            return "Wrong pin"
        
    def change_owner(self, pin, new_owner_name, new_owner_address):
        if pin == self.__pin:
            self.owner_name = new_owner_name
            self.owner_address = new_owner_address
            return "Owner details updated successfully"
        else:
            return "Wrong pin"
        
    def deposit(self, amount):
        if self.__is_frozen:
            return "Account is frozen"
        self.__balance += amount
        self.transactions.append({
            "type": "Deposit",
            "amount": amount,
            "date": datetime.datetime.now()
        })
        return "Deposit successful"
    
    def withdraw(self, amount, pin):
        if pin == self.__pin:
            if self.__is_frozen:
                return "Account is frozen"
            if self.__balance + self.__overdraft_limit - amount >= self.__minimum_balance:
                self.__balance -= amount
                self.transactions.append({
                    "type": "Withdrawal",
                    "amount": amount,
                    "date": datetime.datetime.now()
                })
                return "Withdrawal successful"
            else:
                return f"Withdrawal failed: Minimum balance requirement not met. Minimum balance: {self.__minimum_balance}"
        else:
            return "Wrong pin"
        
    def account_statement(self, pin):
        if pin == self.__pin:
            return {
                "Account Number": self.number,
                "Owner Name": self.owner_name,
                "Balance": self.__balance,
                "Transactions": self.transactions,
                "Frozen": self.__is_frozen
            }
        else:
            return "Wrong pin"
        
    def set_overdraft_limit(self, pin, limit):
        if pin == self.__pin:
            self.__overdraft_limit = limit
            return "Overdraft limit set successfully"
        else:
            return "Wrong pin"
        
    def set_interest_rate(self, pin, rate):
        if pin == self.__pin:
            self.__interest_rate = rate
            return "Interest rate set successfully"
        else:
            return "Wrong pin"
        
    def calculate_interest(self, pin, months):
        if pin == self.__pin:
            interest = self.__balance * (self.__interest_rate / 100) * months
            return interest
        else:
            return "Wrong pin"
        
    def apply_interest(self, pin, months):
        if pin == self.__pin:
            interest = self.calculate_interest(pin, months)
            self.__balance += interest
            self.transactions.append({
                "type": "Interest",
                "amount": interest,
                "date": datetime.datetime.now()
            })
            return "Interest applied successfully"
        else:
            return "Wrong pin"
        
    def freeze_account(self, pin):
        if pin == self.__pin:
            self.__is_frozen = True
            return "Account frozen successfully"
        else:
            return "Wrong pin"
        
    def unfreeze_account(self, pin):
        if pin == self.__pin:
            self.__is_frozen = False
            return "Account unfrozen successfully"
        else:
            return "Wrong pin"
        
    def transaction_history(self, pin):
        if pin == self.__pin:
            return self.transactions
        else:
            return "Wrong pin"
        
    def set_minimum_balance(self, pin, minimum_balance):
        if pin == self.__pin:
            self.__minimum_balance = minimum_balance
            return f"Minimum balance set to {minimum_balance}"
        else:
            return "Wrong pin"
        
    def close_account(self, pin):
        if pin == self.__pin:
            self.__balance = 0
            self.__is_frozen = True
            return "Account closed successfully"
        else:
            return "Wrong pin"
        
        
account = Account(number="123456789", pin="1234", owner_name="John Doe", owner_address="123 Main St")
result = account.close_account(pin="1234")
result = account.close_account(pin="0000")
print(result)