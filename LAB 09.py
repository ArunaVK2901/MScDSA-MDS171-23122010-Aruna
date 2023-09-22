import csv

class ExpenseTracker:

    def __init__(self):
        self.transactions = {
            "Expense": [],
            "Income": []
        }

    def storeTransaction(self, type, category, cost, description, date):
        transaction = {
            "Category": category,
            "Cost": cost,
            "Description": description,
            "Date": date,
        }
        if type == "Expense":
            self.transactions['Expense'].append(transaction)
        else:
            self.transactions['Income'].append(transaction)
        return True

    def viewTransactions(self):
        print("INCOME")
        for income in self.transactions['Income']:
            print(income)

        print("EXPENSES")
        for expense in self.transactions['Expense']:
            print(expense)

    def total_income_expense(self):
        print("Total Income")
        totalIncome = 0
        for income in self.transactions['Income']:
            totalIncome += income["Cost"]
        print(totalIncome)
        print("Total Expense")
        totalExpense = 0
        for expense in self.transactions['Expense']:
            totalExpense += expense["Cost"]
        print(totalExpense)

    def save_to_csv(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["Type", "Category", "Cost", "Description", "Date"])
            writer.writeheader()
            for income in self.transactions['Income']:
                writer.writerow({"Type": "Income", **income})
            for expense in self.transactions['Expense']:
                writer.writerow({"Type": "Expense", **expense})

    def load_from_csv(self, filename):
        self.transactions = {
            "Expense": [],
            "Income": []
        }
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Type"] == "Expense":
                    self.storeTransaction("Expense", row["Category"], float(row["Cost"]), row["Description"], row["Date"])
                elif row["Type"] == "Income":
                    self.storeTransaction("Income", row["Category"], float(row["Cost"]), row["Description"], row["Date"])

def main():
    myTransactions = ExpenseTracker()

    # Load data from a CSV file (if it exists)
    try:
        myTransactions.load_from_csv("transactions.csv")
        print("Data loaded successfully from 'transactions.csv'.")
    except FileNotFoundError:
        print("No previous data found. Starting with an empty tracker.")

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Add Income")
        print("3. View Transactions")
        print("4. Export to CSV")
        print("5. Show Total Income and Expense")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == "1":
            category = input("Enter expense category: ")
            cost = float(input("Enter expense amount: "))
            description = input("Enter expense description: ")
            date = input("Enter date (YYYY-MM-DD): ")
            myTransactions.storeTransaction("Expense", category, cost, description, date)
            print("Expense added successfully.")

        elif choice == "2":
            category = input("Enter income source: ")
            cost = float(input("Enter income amount: "))
            description = input("Enter income description: ")
            date = input("Enter date (YYYY-MM-DD): ")
            myTransactions.storeTransaction("Income", category, cost, description, date)
            print("Income added successfully.")

        elif choice == "3":
            myTransactions.viewTransactions()

        elif choice == "4":
            myTransactions.save_to_csv("transactions.csv")
            print("Data exported to 'transactions.csv'.")

        elif choice == "5":
            myTransactions.total_income_expense()

        elif choice == "6":
            break

if __name__ == "__main__":
    main()