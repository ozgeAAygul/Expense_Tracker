class Expense:
  def __init__(self, amount, category, description):
    self.amount = amount
    self.category = category
    self.description = description

  def __str__(self):
    return f"You spent {self.amount} on {self.description} from {self.category}"

class ExpenseTracker:
  def __init__(self):
    self.expense = []

  def add_expense(self, expense):
    self.expense.append(expense)

  def list_expenses(self):
    if not self.expense:
      print("There is no expense")
      return

    print("\nList of Expenses:")
    for ex in self.expense:
      print(ex)
    print()
  
  def total_expense(self):
    if not self.expense:
      print("There is no expense!")
      return
    total = 0
    for ex in self.expense:
      total += ex.amount
    return f"Your total expense is {total}"  
  
  def filter_by_category(self, category):
    filtered = [ex for ex in self.expense if ex.category == category]
    if not filtered :
      print("No expenses found in this category.")
      return
    print(f"\nExpenses in category '{category}':")
    for ex in filtered:
      print(ex)
    print()
    

trac = ExpenseTracker()
while True:
  choice = input("1-Add expense, 2-List expenses, 3-Learn total expense, 4-Filter by category 5-Quit")
  if choice == "":
    continue
  elif choice == "1":
    amount = int(input("Enter the amount:"))
    category = input("Enter the category:")
    description = input("Enter the description:")
    trac.add_expense(Expense(amount, category, description))
    print("Added.")
  elif choice == "2":
    trac.list_expenses()
  elif choice == "3":
    print(trac.total_expense())
  elif choice == "4":
    category = input("Enter the category:")
    trac.filter_by_category(category)
  elif choice == "5":
    break



  
