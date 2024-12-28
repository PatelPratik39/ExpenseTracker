from expense import Expense


def main():
    print(f" 🎯 Running the App")
    
    # Get user input for expense
    expense = get_user_expense()
    print(expense)
    
    # Write their expense to a file
    save_expense_to_file()
    
    # Read File and summerize expenses.
    summerize_expense()

def get_user_expense():
    print(f" Getting User Expenses ")
    expense_name = input("Enter Expense Name : ")
    expense_amount = float(input("Enter Expense Amount : "))
    # print(f"You have entered {expense_name}, {expense_amount}")
    
    expense_categories = [
        "🍕 Food", "🏡 Home", "💼 Work", "🎉 Fun", "✨ Misc",
    ]
    while True:
        print("Select a Category : ")
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
        break

def save_expense_to_file():
    print(f" Saving User Expenses ")
    

def summerize_expense():
    print(f" Summerizing User Expenses ")
    

if __name__ == "__main__":
    main()

