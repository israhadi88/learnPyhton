class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []
   
   #deposit method 
    def deposit(self,amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
    #withdrawl method
    def withdraw(self,amount,description=""):
       current_balance = sum(item["amount"] for item in self.ledger)
       if amount <= current_balance:
        self.ledger.append({"amount": -amount, "description": description})
        return True
       return False 
    def transfer(self, amount, category_instance):
        if self.withdraw(amount, f"Transfer to {category_instance.name}"):
            category_instance.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
    #get_balance method
    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True
    def __str__(self):
        title = f"{self.name:*^30}\n"
        items =""
        for item in self.ledger:
            desc = f"{item['description'][:23]:<23}"
            amt = f"{item['amount']:>7.2f}"
            items += f"{desc}{amt}\n"
            
        total = f"Total: {self.get_balance():.2f}"
        
        return title + items + total

def create_spend_chart(categories):
    spent_amounts = []
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"]) # abs() mengubah -20 menjadi 20
        spent_amounts.append(spent)
    
    total_spent = sum(spent_amounts)
    
    percentages = []
    for spent in spent_amounts:
        if total_spent > 0:
            percent = int((spent / total_spent * 100) / 10) * 10
        else:
            percent = 0
        percentages.append(percent)
    chart = "Percentage spent by category\n"
    
    for y_axis in range(100, -1, -10):
        chart += f"{y_axis:>3}| "
        
        for percent in percentages:
            if percent >= y_axis:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(category.name) for category in categories)
    
    for i in range(max_len):
        chart += "     " 
        for category in categories:
          
            if i < len(category.name):
                chart += f"{category.name[i]}  "
            else:
                chart += "   " 
        if i < max_len - 1:
            chart += "\n"
            
    return chart
    
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(60, "groceries")

clothing = Category("Clothing")
clothing.deposit(500, "initial deposit")
clothing.withdraw(30, "baju")

auto = Category("Auto")
auto.deposit(500, "initial deposit")
auto.withdraw(10, "bensin")

# Panggil fungsi dengan memasukkan list berisi objek kategori
print(create_spend_chart([food, clothing, auto]))