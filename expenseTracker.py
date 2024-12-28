from expense import Expense


def main():
    print(f" 🎯 Running the Expense Tracker App !!")
    expense_file_path = "expense.csv"
    
    # Get user input for expense
    expense = get_user_expense()
    print(expense)
    
    # Write their expense to a file
    # save_expense_to_file(expense,expense_file_path)
    
    # Read File and summerize expenses.
    summerize_expense(expense_file_path)

def get_user_expense():
    print(f"Getting User Expenses ")
    expense_name = input("Enter Expense Name : ")
    expense_amount = float(input("Enter Expense Amount : "))
    # print(f"You have entered {expense_name}, {expense_amount}")
    
    expense_categories = [
        "🍕 Food", "🏡 Home", "💼 Work", "🎉 Fun", "✨ Misc",
    ]
    while True:
        print("Select a Category:")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i + 1}. {category_name}")
        
        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range} : ")) - 1
        
        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index] 
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print("Invalid category. Please try again!")


def save_expense_to_file(expense: Expense, expense_file_path):
    print(f" Saving User Expenses : {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name.strip()}, {expense.amount:.2f}, {expense.category.strip()}\n")
    

def summerize_expense(expense_file_path):
    print(f"🎯 Summerizing User Expenses : ")
    expenses: list[Expense] = []
    
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = map(str.strip, line.strip().split(","))
            print(expense_name, expense_amount, expense_category)
            line_expense = Expense(name = expense_name, amount = float(expense_amount), category = expense_category)
            expenses.append(line_expense)
    
    # dictionary
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    print(amount_by_category)
    
    print("Expenses By Category : ")
    for key, amount in amount_by_category.items():
        print(f"    {key}: ${amount:.2f}")

if __name__ == "__main__":
    main()

