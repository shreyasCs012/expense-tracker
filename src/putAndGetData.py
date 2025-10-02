from firebase_config import account_doc, account_type, account_uncategorized
from firebase_admin import firestore

def addTo

'''
account_doc -> it records all transactions
               its document is Upi Ref and field is dict

account_un_and_categorized-> it records all uncategorized and catogorized
                             2 documents and uncategorized feild is upiRef but in catogorized feild is name
                               account_un_and_categorized-> uncategorized ->"541284546","846586546"
                                          |
                                          v
                            {"name":["pure pulp","amul"], "catog":"food and bev"}, {"name":"bmtc bus", "catog":"travell"}
account_type-> It records the data in a catogorized fashon and this is shown to the user
                document is 
                                                
'''
