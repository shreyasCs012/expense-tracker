from putAndGetData import *
# Lookup function
def putData(Name,operation,**listdata):
      if Name is None and any(v is None for v in listdata.values()):
           return
      elif not getName(Name):
           if operation == '-':
             listdata["amt"]=0-listdata["amt"]
           AddTouncategorized(listdata["UpiRef"],**listdata)
      elif getName(Name):
             listdata["amt"]=updateRate(Name,operation,listdata["amt"])
             AddFeed(Name,**listdata)
      
def updateRate(Name_number, operation:str,amt:int):
    data=getName(Name_number)
    if operation == "+":
         return data["amt"]+amt
    else :
         return data["amt"]-amt

    


    
'''

catog_index={
   
}
catog={
   "food & beverage" = {
        "pure pulp" = [100, AC524621]
        "amul" = [130, AC54236]
    }
    "movie" = {
    }
}
'''