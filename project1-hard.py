import pandas as pd

class Expense:
    def __init__(self, category, amount, date):
        self.category = category
        self.amount = amount
        self.date = date

class ExpenseManager:
    def __init__(self):
        self.df = pd.DataFrame(columns=['Category', 'Amount', 'Date'])

    def add_expense(self, expense):
        self.df.loc[len(self.df)] = [expense.category, expense.amount, expense.date]

    def view_expenses(self):
        print(self.df)

    def category_summary(self, category):
        total = self.df[self.df['Category'] == category]['Amount'].sum()
        print(f"Total amount for category '{category}': {total}")

    def save_to_csv(self, filepath):
        self.df.to_csv(filepath, index=False)

    def load_from_csv(self, filepath):
        self.df = pd.read_csv(filepath)

manager = ExpenseManager()

# Add new expenses
e1 = Expense("Food", 15.5, "2025-07-29")
e2 = Expense("Transport", 6.75, "2025-07-30")

manager.add_expense(e1)
manager.add_expense(e2)

# View all expenses
manager.view_expenses()

# View summary
manager.category_summary("Food")

# Save to CSV
manager.save_to_csv("expenses.csv")

# Load from CSV
manager.load_from_csv("expenses.csv")