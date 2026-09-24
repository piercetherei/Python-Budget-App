# Python-Budget-App
An app that can be used to track your budget/spendings by categories, featuring a simple console chart that can be created to visualize your spendings.

Instructions:
```You can create a category by assigning an instance of the Category class to a variable.
To deposit, use the .deposit(amount, description) method.
To withdraw, use the .withdraw(amount, description) method.
To transfer money between categories, use the .transfer(amount, category) method on the category you wanna transfer FROM, where the category argument should be a variable name and not a string.
To check the balance of a category, use the .get_balance() method.
Printing a category instance outputs a log of all the relevant transactions. 
You can create a simple chart by assigning the output of the function create_spend_chart(categories) to a variable and then printing it, where the categories variable is a list containing the instances of the categories you wanna see in the chart.

Example:

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

Output:

*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
Percentage spent by category
100|       
 90|       
 80|       
 70|    o  
 60|    o  
 50|    o  
 40|    o  
 30|    o  
 20| o  o  
 10| o  o  
  0| o  o  
    -------
     F  G  
     o  r  
     o  o  
     d  c  
        e  
        r  
        i  
        e  
        s  
```
