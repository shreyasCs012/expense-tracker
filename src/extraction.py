import re
from catogorize import passData
import hashlib

def generatKey(name: str) -> str:
    return hashlib.sha1(name.encode()).hexdigest()[:10]

catog={}
def getdetail(sms: str):
    sms = sms.lower()

    # ---- Find name (after "to" or "from") ----
    name = None
    name_match = re.search(r"\b(?:to|from)\s+((?:\S+\s+){0,1}\S+)", sms)
    if name_match:
        name = name_match.group(1).strip()

    # ---- Find price (after Rs./INR) ----
    price = None
    price_match = re.search(r"(?:rs\.?|inr)\s*([0-9]+(?:\.[0-9]{1,2})?)", sms)
    if price_match:
        price = float(price_match.group(1))

    # ---- Find account/ref number ----
    acc = None
    acc_match = re.search(r"(?:ref no|reference id)\s*([0-9]+)", sms)
    if acc_match:
        acc = acc_match.group(1)
    # ---- Check if debit/credit ----
    txn_type = None
    if "debited" in sms:
        txn_type = "-"
    elif "credited" in sms:
        txn_type = "+" 
    catog["upiref"]=acc
    catog["amt"]=price
    catog["name"]=name
    catog["key"]=generatKey(name)
    catog["catego"]=False
    passData(txn_type,**catog)
# ---- Example usage ----
'''
for key, expense in all_expenses.items():
    elelist = getdetail(expense["title"])
    print(f"Name: {elelist[0]}")
    print(f"Price: {elelist[1]}")
    print(f"Ref No: {elelist[2]}")
    print(f"Type: {elelist[3]}")
    print("-" * 30)
'''

