#How to Run:
#------------
#1. Make sure you have Python installed (Python 3.x).
#2. Save this file as `expense_tracker.py`.
#3. Open a terminal or command prompt.
#4. Run the program with the command:

#What You Learn from This Program:
#----------------------------------
#- How to create a basic CLI (Command Line Interface) app in Python.
#- How to take user input and validate it.
#- How to use file operations to read and write data (`open`, `readlines`, `write`).
#- Basic error handling using try-except blocks.
#- Working with string manipulation and formatting.
#- Structuring code with functions for better readability and maintenance.
#"""










import os
from datetime import datetime

def show_menu():
    print("\nWelcome to your Expense Tracker!")
    print("\nPlease choose an option:")
    print("1. Add an expense")
    print("2. View expenses")
    print("3. View total spent")
    print("4. View totals by category")
    print("5. Exit")

def add_expense():
    item = input("Enter item name (e.g., Coffee): ").strip()
    if not item:
        print("Item name cannot be empty.")
        return

    category = input("Enter category (e.g., Food, Travel, Misc): ").strip()
    if not category:
        print("Category cannot be empty.")
        return

    try:
        amount = float(input("Enter amount spent (e.g., 150): "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    date_str = datetime.now().strftime("%Y-%m-%d")
    with open("expenses.txt", "a") as file:
        file.write(f"{date_str},{item},{category},{amount}\n")
    print("Expense added successfully!")

def view_expenses():
    if not os.path.exists("expenses.txt"):
        print("No expense file found.")
        return

    with open("expenses.txt", "r") as file:
        lines = file.readlines()
        if not lines:
            print("No expenses found.")
            return

        print("\nYour Expenses:")
        for i, line in enumerate(lines, 1):
            parts = line.strip().split(",")
            if len(parts) != 4:
                continue
            date_str, item, category, amount = parts
            print(f"{i}. [{date_str}] {item} ({category}) - ₹{float(amount):.2f}")

def view_total_spent():
    total = 0
    if not os.path.exists("expenses.txt"):
        print("No expense file found.")
        return

    with open("expenses.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) != 4:
                continue
            try:
                amount = float(parts[3])
                total += amount
            except ValueError:
                continue
    print(f"Total spent: ₹{total:.2f}")

def view_totals_by_category():
    if not os.path.exists("expenses.txt"):
        print("No expense file found.")
        return

    category_totals = {}
    with open("expenses.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) != 4:
                continue
            _, _, category, amount_str = parts
            try:
                amount = float(amount_str)
                category_totals[category] = category_totals.get(category, 0) + amount
            except ValueError:
                continue

    if not category_totals:
        print("No valid expenses found.")
        return

    print("\nTotal spent by category:")
    for category, total in category_totals.items():
        print(f"{category}: ₹{total:.2f}")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_total_spent()
        elif choice == "4":
            view_totals_by_category()
        elif choice == "5":
            print("Goodbye! Have a very nice day.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
