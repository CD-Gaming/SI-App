import datetime

class Log:
    def __init__(self):
        self.initial_stock = {}
        self.report = {}
        self.log = []

    def audit_log_store(self, text: str, text2: str, text3: str, date: datetime) -> list[str]:
        self.log = []
        info = f"{date.strftime('%Y-%m-%d %H:%M:%S')} : Item ID label {text} quantity, was changed from {text2} to {text3}"
        self.log.append(info)
        return self.log  
    
    def StoreLog(self, i, n, q, r, d):
        self.initial_stock[i] = {  
            "name": n,
            "quantity": q,
            "reorder_level": r,
            "expiry date": d
        }
               
        self.report[i] = {
            "name": n,
            "quantity": q,
            "reorder_level": r,
            "expiry date": d
        }
        
    def UpdateLog(self, i, q, d):
        id = i
        new_qty = q
        new_date = d
        old_qty = self.report[id]["quantity"]
        time = datetime.datetime.now()
        
        self.log = self.audit_log_store(id, old_qty, new_qty, time)
        self.report[id]["quantity"] = new_qty 
        self.report[id]["expiry date"] = new_date 

    def ShowLog(self):
        today = datetime.datetime.now()

        print("Initial stock: ") 
        for x, y in self.initial_stock.items():
            print("ID: ", x, "| Name: ", y["name"], "| Qty: ", y["quantity"], "| Expiry Date: ", y["expiry date"].strftime('%d %m %Y'))
        
        print("----------------------------------")
        print(f"Updated stock (Report): ")
        for x, y in self.report.items():
            qty = y["quantity"]
            reorder = y["reorder_level"]
            expiry = y["expiry date"]
            
            status = "Normal"
            if expiry and expiry < today:
                status = "Expired - Restock/Removal Necessary"
            elif qty <= 0:
                status = "Out of Stock"
            elif qty <= (qty / 2): 
                status = "Average"
            elif qty <= reorder:
                status = "Low Stock"

            print("ID:", x, "| Name:", y["name"], "| Qty:", qty, "| Expiry Date:", expiry.strftime('%d %m %Y'), "| Status:", status)

        print("----------------------------------")        
        print("Audit Logs: ")
        for x in self.log:
            print(x)

        print("----------------------------------")
