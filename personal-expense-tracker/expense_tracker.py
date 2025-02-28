'''
1. Add an expense:

Create a function to prompt the user for expense details. Ensure you ask for:
The date of the expense in the format YYYY-MM-DD
The category of the expense, such as Food or Travel
The amount spent
A brief description of the expense
Store the expense in a list as a dictionary, where each dictionary includes the date, category, amount, and description as key-value pairs
Example: {'date': '2024-09-18', 'category': 'Food', 'amount': 15.50, 'description':'Lunch with friends'}

'''
expenses = []

def getExpenseDetails():
    expense_date = input("Enter your expense date in the below format YYYY-MM-DD : ")
    print("Entered date is  : ",expense_date)
    expense_category = input("Enter category of the expense, such as Food or Travel:")
    print("Entered Category is: " + expense_category)
    expense_amount = input("Enter the amount spent:")
    print("Entered Category is: " + expense_category)
    expense_description = input("Enter the description of the expense:")
    print("Entered Description is: " + expense_description)
    return dict(date=expense_date,category=expense_category,amount = expense_amount, description = expense_description)
    

"""
    **2. View expenses:**      
        * Write a function to retrieve and display all stored expenses
            - [  ] Ensure the function loops through the list of expenses and displays the date, category, amount, and description for each entry
        * Validate the data before displaying it  
            - [  ] If any required details (date, category, amount, or description) are missing, skip the entry or notify the user that it’s incomplete
"""
def viewExpenses():
    for x in expenses:
        print(x)



while True:
    inpu = input('Dpo you wish to enter an expense ? (y or n)')
    if inpu == 'y':
        expenses.append(getExpenseDetails())
        continue;
    else:
        break;

if len(expenses)>0:
    viewExpenses()
