class Expense:
    def __init__(self, date, description, amount, category):
        self.date = date
        self.description = description
        self.amount = amount
        self.category = category

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories  = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def print_categories(self):
        print("Categories: ")
        for i, category in enumerate(self.categories, start=1):
            print(f"{i}. {category}")
    
    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            print("Expense removed successfully.")
        else:
            print("Invalid expense index.")

    def view_expenses(self):
        if len(self.expenses) == 0:
            print("No expenses found.")
        else:
            print("Expense List:")
            for i, expense in enumerate(self.expenses, start=1):
                print(f"{i}. Date: {expense.date}, Description: {expense.description}, Amount: {expense.amount}, Category: {expense.category}")

    def total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total Expenses: ${total:.2f}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. Create a Category")
        print("4. View All Expenses")
        print("5. Total Expenses")
        print("6. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            description = input("Enter the desciption: ")
            amount = float(input("Enter the amount ($): "))
            tracker.print_categories()
            category = int(input("Enter a category number: ")) - 1
            expense = Expense(date, description, amount, tracker.categories[int(category)])
            tracker.add_expense(expense)
            print("Expense added successfully.")
        elif choice == "2":
            index = int(input("Enter the expense index to remove: ")) - 1
            tracker.remove_expense(index)
        elif choice == "3":
            category_name = input("Enter category name: ")
            tracker.categories.append(category_name)
            print("Category added sucessfully.")
        elif choice == "4":
            tracker.view_expenses()
        elif choice == "5":
            tracker.total_expenses()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


