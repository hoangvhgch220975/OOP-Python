class PersonalBudgetManager:
    def __init__(self):
        self.expenses = {}
        self.budget = 0

    def display_menu(self):
        print("Personal Budget Manager Menu:")
        print("1. Log expense")
        print("2. Show expense summary by category")
        print("3. Set monthly budget")
        print("4. Check budget balance")
        print("5. Quit")

    def log_expense(self):
        amount = float(input("Enter the expense amount: $"))
        category = input("Enter the expense category: ")
        date = input("Enter the expense date (MM/DD/YYYY): ")

        if category not in self.expenses:
            self.expenses[category] = []

        self.expenses[category].append({"amount": amount, "date": date})
        print("Expense logged successfully!")

    def show_expense_summary(self):
        category = input("Enter the category to show summary: ")
        if category in self.expenses:
            total_spent = sum(expense["amount"] for expense in self.expenses[category])
            print(f"Total spent in {category}: ${total_spent}")
        else:
            print(f"No expenses logged for {category}.")

    def set_monthly_budget(self):
        self.budget = float(input("Enter your monthly budget amount: $"))
        print("Monthly budget set successfully!")

    def check_budget_balance(self):
        total_expenses = sum(sum(expense["amount"] for expense in expenses) for expenses in self.expenses.values())
        balance = self.budget - total_expenses

        print(f"Total expenses: ${total_expenses}")
        print(f"Monthly budget: ${self.budget}")
        
        if balance >= 0:
            print(f"You are under budget by ${balance:.2f}")
        else:
            print(f"You are over budget by ${abs(balance):.2f}")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.log_expense()
            elif choice == "2":
                self.show_expense_summary()
            elif choice == "3":
                self.set_monthly_budget()
            elif choice == "4":
                self.check_budget_balance()
            elif choice == "5":
                print("Quitting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


# Run the Personal Budget Manager
budget_manager = PersonalBudgetManager()
budget_manager.run()
