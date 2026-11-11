import datetime;
class Operations: #Overloading doesnt exist for python
    stock_data = {}
    initial_stock = {} 
    report = {}
    log = [] #might not need this?
   
    def __init__(self): #Initialization
        self.stock_data = {}
        self.initial_stock = {}
        self.report = {}
        self.log = []
  
    def audit_log_store(text: str, text2:str, date:datetime) -> list[str]: #works now, find a way to remove the milliseconds that show up on the time log
        log = []
        info = f"{date} : Item ID label {text}  was changed to {text2}"
        log.append(info)
        return log  
    
    def StockCheck(self,i): #to check if the item is already in the system
        item_id = i
        if item_id in self.stock_data: 
            print("Error: Item already exists")
            return True
        return False
    
    
    def StoreStock(self,i,n,q,r,d): #Python requires the use of self to know that it should access its own variables
        item_id = i
        name = n
        qty = q
        reorder = r
        
        date = d   
        
            
        self.stock_data[item_id] = {
            "name": name,
            "quantity": qty,
            "reorder_level": reorder,
            }
        #Different so tht they dont mix info?? and so that I can save different versions of this one for weekly
        #or monthly reports allowing for difference comparison
        self.initial_stock[item_id] = { 
            "name": name,
            "quantity": qty,
            "reorder_level": reorder,
            "expiry date" : date
            }
        
        self.report[item_id] = {
            "name": name,
            "quantity": qty,
            "reorder_level": reorder,
            "expiry date" : date
            }
        
                    #dont save expiry date to stock levels.
        print("Stock recorded successfully")
    
    def ViewStock(self):
        if not self.stock_data: #inside a class start here
            print("No stock records found")
        else:
            print("\nCurrent Stock Levels:")
            for id, info in self.stock_data.items():
                status = "Normal"
                if info["quantity"] <= info["reorder_level"]:
                    status = "Low Stock"
                print("ID:", id, "| Name:", info["name"], "| Qty:", info["quantity"], "| Status:", status) #stop here 
        

        
   
    