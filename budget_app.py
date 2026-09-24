class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    #Deposit to the category's budget
    def deposit(self, amount, description=''):
        try:
            if amount <= 0:
                raise ValueError('Please enter a valid amount of money.')
            else:
                self.ledger.append({'amount': amount, 'description': description})
        except TypeError:
            raise TypeError('The amount should be number.')

    #Withdraw from the category's budget
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            raise ValueError('You dont have sufficient funds in this category to withdraw.')

    #Checks the category's balance
    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction['amount']
        return balance

    #Checks whether you have enough money to withdraw
    def check_funds(self, amount):
        try:
            if amount > self.get_balance() or amount <= 0:
                return False
            else:
                return True
        except TypeError:
                raise TypeError('The amount should be number.')       

    #Transfer money between categories
    def transfer(self, amount, receiver):
        try:
            if self.check_funds(amount):
                self.withdraw(amount, f'Transfer to {receiver.name}')
                receiver.deposit(amount, f'Transfer from {self.name}')
                return True
            else:
                raise ValueError('You dont have sufficient funds in this category to perform a transfer.')
        except AttributeError:
            raise AttributeError('Please refer to a variable when performing a transfer.')

    #Outcome when you try to print a category
    def __str__(self):
        lines = ''
        for transaction in self.ledger:
            lines += f'{transaction["description"]:<23.23}{format(float(transaction["amount"]), ".2f"):>7}\n'
        return f"{self.name:*^30}\n{lines}Total: {self.get_balance()}"

#Creates the spending chart
def create_spend_chart(categories):
    chart = 'Percentage spent by category\n'
    total_spent = 0

    #Sums up the total money spent on this category
    for category in categories:
        for transaction in category.ledger:
            if transaction['amount'] < 0:
                total_spent += abs(transaction['amount'])

    #Assigns the 'o's on the chart
    for i in range(100, -10, -10):
        percentages = ''.join(
            render_percentage(calculate_percentages(category, total_spent), i)
            for category in categories
        )
        chart += f"{i:>3}|{percentages} \n"

    max_length = max(len(category.name) for category in categories) #Finds the longest name among the given categories 
    chart += f"    {'---'*len(categories)}-\n"

    #Lays out the names of the categories vertically
    for i in range(max_length):
        line = [category.name.ljust(max_length)[i] for category in categories]
        chart += f"     {'  '.join(line)}  \n"
    return chart.rstrip('\n')

#Calculates the percentage of spending of every category 
def calculate_percentages(category, total):
    spent = 0
    for transaction in category.ledger:
        if transaction['amount'] < 0:
            spent += abs(transaction['amount'])
    return int(spent / total * 100 // 10) * 10 #Floors to the nearest 10

def render_percentage(spent_pc, i):
    if spent_pc >= i:
        return ' o '
    else:
        return '   '

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
groceries = Category('Groceries')
groceries.deposit(1000, 'initial deposit')
groceries.withdraw(190.15, 'groceries')
groceries.withdraw(15.89, 'restaurant and more groceries for dessert')
groceries.transfer(50, clothing)
print(food)

test = create_spend_chart([food, groceries])
print(test)