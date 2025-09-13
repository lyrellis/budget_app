#class Ledger:
#    def __init__(self, category)
#        self.ledger = category

class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.total = 0

    def __str__(self):
        category_str = f'{self.category:*^30}'
        for transaction in self.ledger:
            amount, description = transaction
            amount_as_currency = f'{float(amount):.2f}'
            category_str += f'\n{description[:23]:<23}{amount_as_currency:>7}'
        category_str += f'\nTotal: {self.total:.2f}'
        return category_str

    def deposit(self, amount, description = ''):
        self.ledger.append((amount, description))
        self.total += amount

    def withdraw(self, amount, description = ''):
        self.ledger.append((f'-{amount}', description))
        self.total -= amount

    def get_balance(self):
        pass

    def transfer(self, amount, category):
        self.ledger.append((f'-{amount}', f'Transfer to {category.category}'))
        category.ledger.append((amount, f'Transfer from {self.category}'))
        self.total -= amount
        category.total += amount

    def check_funds(self):
        pass

def create_spend_chart(categories):
    pass

# Example Input------------------

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
print(clothing)