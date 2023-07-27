# Budget App Project

Welcome to the **Budget App** project from the **Scientific Computing with Python** course offered by freeCodeCamp. In this project, you will complete the `Category` class in `budget.py`, which allows you to manage budget categories like food, clothing, and entertainment. The class will handle deposits, withdrawals, transfers, balance calculation, and more.

## Project Description

The `Category` class should have the following methods:

1. `deposit(amount, description="")`: Adds a deposit to the category's ledger.
2. `withdraw(amount, description="")`: Adds a withdrawal (negative amount) to the category's ledger. Returns `True` if the withdrawal took place, and `False` otherwise.
3. `get_balance()`: Returns the current balance of the budget category based on deposits and withdrawals.
4. `transfer(amount, destination_category)`: Transfers an amount from one category to another. Returns `True` if the transfer took place, and `False` otherwise.
5. `check_funds(amount)`: Checks if there are enough funds to perform a withdrawal or transfer.

The budget object will be printed as follows:

```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

Additionally, you will create a function called `create_spend_chart` (outside of the class) that takes a list of categories as an argument and returns a string representing a bar chart showing the percentage spent in each category.

The bar chart should be made using the "o" character and should be rounded down to the nearest 10. The category names should be written vertically below the bars, and there should be a title at the top saying "Percentage spent by category."

## Development and Testing

- Write your code in `budget.py`. For development, you can use `main.py` to test your `Category` class. Click the "run" button, and `main.py` will run.
- The unit tests for this project are in `test_module.py`. We imported the tests from `test_module.py` to `main.py` for your convenience. The tests will run automatically whenever you hit the "run" button.

Let's manage our budget categories and visualize the spending with Python! Happy coding!
