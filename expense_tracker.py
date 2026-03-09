
# expense_tracker.py

expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food/Travel/Other): ")
    date = input("Enter date (DD-MM-YYYY): ")
    expenses.append({"amount": amount, "category": category, "date": date})
    print("Expense added!\n")

def show_expenses():
    if not expenses:
        print("No expenses yet!\n")
        return
    print("\nAll Expenses:")
    for i, exp in enumerate(expenses):
        print(f"{i+1}. {exp['date']} | {exp['category']} | {exp['amount']}")
    print()

def total_spent():
    total = sum(exp['amount'] for exp in expenses)
    print(f"Total spent: {total}\n")

def main():
    while True:
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Total Spent")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            show_expenses()
        elif choice == '3':
            total_spent()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.\n")

if __name__ == "__main__":
    main() 



