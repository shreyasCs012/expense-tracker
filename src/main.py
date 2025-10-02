from getData import all_expenses
from extraction import getdetail
from putAndGetData import *
for key, expense in all_expenses.items():
    getdetail(expense["title"])

CreateSec("Food and bev")
CreateSec("travel")



