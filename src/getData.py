from firebase_config import get_db_ref
expenses_ref = get_db_ref('expenses')

# Fetch all expenses
all_expenses = expenses_ref.get()

'''for key,expense in all_expenses.items(): 
   print("__"*10)
   print(expense["title"])
   print("__"*10)
'''
