class Category:
    # Initializes category budget
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.total = 0
        self.spent = 0

    # Formats output
    def __str__(self):
        category_str = f'{self.category:*^30}'
        for transaction in self.ledger:
            amount_as_currency = f"{transaction['amount']:.2f}"
            category_str += f"\n{transaction['description'][:23]:<23}{amount_as_currency:>7}"
        category_str += f'\nTotal: {self.total:.2f}'
        return category_str

    # Deposits funds
    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})
        self.total += amount

    # Will be used to check for sufficient funds
    def check_funds(self, amount):
        if amount > self.total:
            return False
        else:
            return True
        
    # Tracks total spending per category
    def tracker(self, amount = 0):
        self.spent += amount
        return self.spent

    # Withdraws from funds (description optional)
    def withdraw(self, amount, description = ''):
        if self.check_funds(amount): # Checks for sufficient funds
            self.ledger.append({'amount': (-1 * amount), 'description': description})
            self.total -= amount
            self.tracker(amount)
            return True
        else:
            return False

    # Transfers funds from one category to another
    def transfer(self, amount, category):
        if self.check_funds(amount): # Checks for sufficient funds
            self.ledger.append({'amount': (-1 * amount), 'description': f'Transfer to {category.category}'})
            category.ledger.append({'amount': amount, 'description': f'Transfer from {self.category}'})
            self.total -= amount
            category.total += amount
            return True
        else:
            return False

    # Gets current balance in self category
    def get_balance(self):
        return self.total


# Create a chart to visualize spending categories
def create_spend_chart(categories):
    
    # Declare some variables
    spending_total = 0
    categories_count = 0
    new_max = 0
    index = 0

    # Calculate total spending
    for category in categories:
        spending_total += category.tracker()
        categories_count += 1

        old_max = len(category.category)
        new_max = max(old_max, new_max)
    
    # Draw chart
    chart = 'Percentage spent by category'
    for i in range(10, -1, -1):
        chart += f'\n{(10 * i):>3}|'
        for category in categories:
            pips = ((100 * category.tracker() / spending_total) // 10) # Calculate percentage spending, translate to number of pips
            if pips >= (i):
                chart += ' o '
            else:
                chart += '   '
        chart += ' '
    chart += '\n    ' + '-'*(3 * categories_count + 1)
    for i in range(new_max):
        chart += f'\n    '
        for category in categories:
            if i < len(category.category):
                chart += f' {category.category[index]} '
            else:
                chart += '   '
        chart += ' '
        index += 1
    return chart
    

# Example Input------------------
'''
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
print(clothing)

print(create_spend_chart([food, clothing]))
'''