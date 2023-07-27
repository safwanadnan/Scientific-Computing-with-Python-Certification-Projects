class Category:
  """
  Represents a budget category.

  Attributes:
  - name: The name of the category.
  - ledger: A list of dictionary entries representing transactions.

  Methods:
  - deposit(amount, description=""): Adds a deposit transaction to the ledger.
  - withdraw(amount, description=""): Adds a withdrawal transaction to the ledger if sufficient funds are available.
  - get_balance(): Calculates and returns the current balance of the category.
  - transfer(amount, category): Transfers funds from the current category to another category.
  - check_funds(amount): Checks if there are sufficient funds in the category to make a withdrawal.
  - __str__(): Returns a string representation of the category, including the ledger transactions and total balance.
  """

  def __init__(self, name):
    """
    Initializes a Category object with a name and an empty ledger.
    """
    self.name = name
    self.ledger = []

  def deposit(self, amount, description=""):
    """
    Adds a deposit transaction to the ledger.

    Args:
    - amount: The amount to be deposited.
    - description: (optional) The description of the deposit transaction.
    """
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    """
    Adds a withdrawal transaction to the ledger if sufficient funds are available.

    Args:
    - amount: The amount to be withdrawn.
    - description: (optional) The description of the withdrawal transaction.

    Returns:
    - True: If the withdrawal is successful.
    - False: If there are insufficient funds to make the withdrawal.
    """
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False

  def get_balance(self):
    """
    Calculates and returns the current balance of the category.

    Returns:
    - The current balance of the category.
    """
    balance = 0
    for item in self.ledger:
      balance += item["amount"]
    return balance

  def transfer(self, amount, category):
    """
    Transfers funds from the current category to another category.

    Args:
    - amount: The amount to be transferred.
    - category: The target category to receive the transfer.

    Returns:
    - True: If the transfer is successful.
    - False: If there are insufficient funds to make the transfer.
    """
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {category.name}")
      category.deposit(amount, f"Transfer from {self.name}")
      return True
    return False

  def check_funds(self, amount):
    """
    Checks if there are sufficient funds in the category to make a withdrawal.

    Args:
    - amount: The amount to be checked.

    Returns:
    - True: If there are sufficient funds.
    - False: If there are insufficient funds.
    """
    return amount <= self.get_balance()

  def __str__(self):
    """
    Returns a string representation of the category, including the ledger transactions and total balance.

    Returns:
    - A formatted string representing the category.
    """
    title = f"{self.name:*^30}\n"
    items = ""
    total = 0
    for item in self.ledger:
      description = item["description"][:23].ljust(23)
      amount = "{:.2f}".format(item["amount"]).rjust(7)
      items += f"{description}{amount}\n"
      total += item["amount"]
    output = title + items + "Total: {:.2f}".format(total)
    return output


def create_spend_chart(categories):
  """
  Creates a spending chart showing the percentage spent by each category.

  Args:
  - categories: A list of Category objects representing different budget categories.

  Returns:
  - A string representing the spending chart.
  """
  # Calculate total withdrawals for all categories
  total_withdrawals = sum(
    abs(item['amount']) for category in categories for item in category.ledger
    if item['amount'] < 0)

  category_names = [category.name for category in categories]
  spent_percentages = [
    int((sum(
      abs(item['amount'])
      for item in category.ledger if item['amount'] < 0) / total_withdrawals) *
        10) * 10 for category in categories
  ]

  chart = "Percentage spent by category\n"
  for i in range(100, -10, -10):
    chart += str(i).rjust(3) + "| "
    for percentage in spent_percentages:
      if percentage >= i:
        chart += "o  "
      else:
        chart += "   "
    chart += "\n"

  chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

  max_category_name_length = max([len(name) for name in category_names])

  for i in range(max_category_name_length):
    chart += "     "
    for name in category_names:
      if i < len(name):
        chart += name[i] + "  "
      else:
        chart += "   "
    if i < max_category_name_length - 1:
      chart += "\n"

  return chart
