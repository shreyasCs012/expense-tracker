from firebase_config import account_transaction, account_type, uncatego,catego
from firebase_admin import firestore

def addToTransac(UpiRef:str,**data):
    doc=account_transaction.document(UpiRef)
    doc.set(data)

def addToUncategorized(Key:str,fieldRef):
  uncatego.set({Key: fieldRef}, merge=True)


def createSection(type: str):
    doc = catego.get()
    if doc.exists:
        data = doc.to_dict()
        if type not in data:  # field doesn't exist
            catego.update({type: []})   # initialize as empty list
            print(f"Created empty list for field '{type}'")
        else:
            print(f"Field '{type}' already exists")
    else:
       return

def addToCatog(type: str, KeyRefs):
    catego.update({
        type: firestore.ArrayUnion([KeyRefs])  # <- always a list
    })
    deletdoc(KeyRefs)


def checkDocType(key: str):
    return account_type.document(key).get().exists
   
def getAmt(key: str):
    doc_ref = account_type.document(key)
    doc = doc_ref.get()
    if doc.exists:
        data = doc.to_dict()
        return data.get("amt")   # safer than data["amt"]
    return None

def addToType(Key: str, **data):
    account_type.document(Key).set(data)

def GetRef(key:str):
    return account_type.document(key)

def deletdoc(key):
    doc_ref = uncatego.get(key)
    doc_ref.delete()
'''
    transaction -> every transaction 
                    document is upi ref and frild contians
                                             (name,amt,key=True/False,date)   
    un/catagorized->transaction which are catagorized and not catagorized
                    the uncatog document will have transaction whoes fild has catog has false
                    and catog wil have fild like food and bev, ent, travell which has a list which stores refrence to the document in Type Catogori
    Type - > Document is key and field and the amt is changed here 

    importent thing is :
      generate key 
      add same key to the name 
      cal amount and push it to the types with the same key 
      so the catog will automatically point to the types 
      to form new catog just add a new list to the catog doc
'''
