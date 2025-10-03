from putAndGetData import *

def passData(txn_type:str,**data):
    addToTransac(data["upiref"],**data)
    if txn_type == "-":
        if not checkDocType(data["key"]):
             data["amt"]=0-data["amt"]
        else:
             data["amt"]= getAmt(data["key"])-data["amt"]
    elif txn_type == "+":
        if checkDocType(data["key"]):
            data["amt"]= getAmt(data["key"])+data["amt"]
    else:
        return
    addToType(data["key"],**data)

    if data["catego"]:
        addToCatog("hi",GetRef(data["key"]))
    else:
        addToUncategorized(data["key"],GetRef(data["key"]))
