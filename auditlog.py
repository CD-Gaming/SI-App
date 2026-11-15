import datetime;

class Log:
    def __init__(self):
        self.initial_stock = {}
        self.report = {}
        self.log = []

    #Shows which product was changed w
    def audit_log_store(self,text: str, text2:str, text3:str, date:datetime) -> list[str]: #works now, find a way to remove the milliseconds that show up on the time log
        self.log = []
        info = f"{date} : Item ID label {text}  quantity, was changed from {text2} to {text3}"
        self.log.append(info)

        if info not in self.log: #not sure if this will work
            print("No Audit logs")
        return self.log  
    
    def StoreLog(self,i,n,q,r,d):
        id = i
        name = n
        qty = q
        reorder = r       
        date = d 

        self.initial_stock[id] = { 
        "name": name,
        "quantity": qty,
        "reorder_level": reorder,
        "expiry date" : date
                   }
               
        self.report[id] = {
        "name": name,
        "quantity": qty,
        "reorder_level": reorder,
        "expiry date" : date
        }
    def UpdateLog(self,i,q):
        id = i
        new_qty = q
        old_qty = self.report[id]["quantity"]
        time = datetime.datetime.now()
        
        self.log = self.audit_log_store(id, old_qty, new_qty,time)
        self.report[id]["quantity"] = new_qty #for inventory report comparison
        
        

    def ShowLog(self):
        print("Initial stock: " ) #inside a class start here
        for x, y in self.initial_stock.items():
            print("ID: ", x ,"| Name: ", y["name"], "| Qty: ", y["quantity"], "| Expiry Date: ", y["expiry date"])
        
        print("----------------------------------")
        print(f"Updated stock: ")
        for x, y in self.report.items():
            print("ID: ", x ,"| Name: ", y["name"], "| Qty: ", y["quantity"], "| Expiry Date: ", y["expiry date"])

        print("----------------------------------")        
        print("Audit Logs: ")
        [print(x) for x in self.log]

        print("----------------------------------") #stop herepass