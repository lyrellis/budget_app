class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.total = 0

    def __str__(self):
        category_str = f'{self.category:*^30}'
        for transaction in self.ledger:
            amount_as_currency = f'{float(transaction['amount']):.2f}'
            category_str += f'\n{transaction['description'][:23]:<23}{amount_as_currency:>7}'
        category_str += f'\nTotal: {self.total:.2f}'
        return category_str

    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})
        self.total += amount

    def check_funds(self, amount):
        if amount > self.total:
            return False
        else:
            return True

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            self.total -= amount
            return True
        else:
            return False

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': f'Transfer to {category.category}'})
            category.ledger.append({'amount': amount, 'description': f'Transfer from {self.category}'})
            self.total -= amount
            category.total += amount
            return True
        else:
            return False

    def get_balance(self):
        return f'{self.total:.2f}'

def create_spend_chart(categories=None):
    return 'Percentage spent by category'

# Example Input------------------

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
print(clothing)

print(create_spend_chart())