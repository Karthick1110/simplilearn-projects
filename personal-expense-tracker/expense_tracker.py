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
expenses_questionare = dict(expense_date="Enter your expense date in the below format YYYY-MM-DD : ",
                            expense_category="Enter category of the expense, such as Food or Travel:",
                            expense_amount="Enter the amount spent:",
                            description="Enter the description of the expense:")
total_budget=0;
total_expense=0;

def getExpenseDetails():
    global total_expense;
    store_values = {}
    for key in expenses_questionare:
        values = input(expenses_questionare[key])
        if len(values)>0:
            if key == 'expense_amount':
                total_expense = total_expense + int(values)
            store_values.update({key:values})
        else:
            print("Invalid / Empty values, please enter your input again")
            values = input(expenses_questionare[key])
    print(store_values)
    return dict(store_values)

"""
    **2. View expenses:**      
        * Write a function to retrieve and display all stored expenses
            - [  ] Ensure the function loops through the list of expenses and displays the date, category, amount, and description for each entry
        * Validate the data before displaying it  
            - [  ] If any required details (date, category, amount, or description) are missing, skip the entry or notify the user that it’s incomplete
"""
expenses_key = ('date','category','amount','description')
def viewExpenses():
   counter = 0;
   for iterate_expense in expenses:
       counter = counter+1
       print(f'Expense Id'.ljust(13),f' : {counter}')
       for key in iterate_expense:
            print(f'{key}'.ljust(20),f' : {iterate_expense[key]}')

def setExpense():
    inpu = 'y'
    while True:
        if inpu == 'y':
            expenses.append(getExpenseDetails())
            inpu = input('Do you wish to enter an expense ? (y or n) ')
            continue;
        else:
            break;

"""
    3. Set and track the budget:
        • Create a function that allows the user to input a monthly budget. Prompt the
        user to:
            o  Enter the total amount they want to budget for the month
        Create another function that calculates the total expenses recorded so far
            o  Compare the total with the user’s monthly budget
            o  If the total expenses exceed the budget, display a warning (Example:
        You have exceeded your budget!)
            o  If the expenses are within the budget, display the remaining balance
        (Example: You have 150 left for the month)
"""

def setAndTrackBudget():
    global total_budget;
    values = int(input("Enter your your total budget for the month : "))
    ## 
    total_budget = values
    compareBudget()

def compareBudget():
    if (total_expense > total_budget):
        print("Warning : your total expense is greater than your monthly buget",end='\n')
    else:
        print(f'you have {total_budget-total_expense} left for the month',end='\n')

"""
save expense in the excel
"""

def saveExpense():
    f = open('./personal-expense-tracker/hello.csv','w+')
    for iterate_expense in expenses:
       for i,key in enumerate(iterate_expense):
            if i>=3:
                f.write(iterate_expense[key])
            else:
                f.write(iterate_expense[key] + ',')    
    f.close

def readExpenses():
    fread= open('./personal-expense-tracker/hello.csv','r')
    lines = fread.readlines()
    for z in lines:
        literals = z.split(',')
        expenses.append(dict(expense_date=literals[0],expense_category = literals[1],expense_amount=literals[2],description = literals[3]))

def interactiveMenu():
        x=0;
        readExpenses()
        while x!=5:
            print("\nEnter the following option to continue:" ," Add expense".ljust(5),':', 1,
                  ", View expenses".ljust(5),':', 2,
                  ", Track budget".ljust(5),':', 3,
                  ", Save Expenses ".ljust(5), ':', 4,", Exit ".ljust(5),':', 5)
            x = int(input("\tChoose the option : "))
            if x == 1:
                setExpense()
            elif x ==2:
                viewExpenses()
            elif x == 3:
                setAndTrackBudget()
            elif x ==4:
                saveExpense()
            else:
                print("Thank you for choosing our program..")

if __name__ == "__main__":
    interactiveMenu()


"""
    expenses.append(dict(date='2024-09-18',category='Food',amount=15.50))
    setExpense()
    viewExpenses()
    setAndTrackBudget()
"""