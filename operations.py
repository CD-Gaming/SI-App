import datetime

class Operations:
    def __init__(self):
        self.stock_data = {} 
        self.log = []
    
    def StockCheck(self, i):
        id = i
        if id in self.stock_data: 
            return True
        return False
    
    def StoreStock(self, i, n, q, r, d):
        id = i
        name = n
        qty = q
        reorder = r 
        expiry_date = d
                 
        self.stock_data[id] = {
            "name": name,
            "quantity": qty,
            "reorder_level": reorder,
            "initial_qty": qty, 
            "expiry_date": expiry_date,
        }

        print("Stock recorded successfully")
    
    def ViewStock(self):
        if not self.stock_data:
            print("No stock records found")
        else:
            print("\nCurrent Stock Levels:")
            today = datetime.datetime.now()
            
            for id, info in self.stock_data.items():
                qty = info["quantity"]
                reorder = info["reorder_level"]
                initial = info.get("initial_qty", qty)
                expiry = info.get("expiry_date")
                
                status = "Normal"
                
                if expiry and expiry < today:
                    status = "Expired - Restock/Removal Necessary"
                elif qty <= 0:
                    status = "Out of Stock"
                elif qty <= (initial / 2):
                    status = "Average"
                elif qty <= reorder:
                    status = "Low Stock"
                    
                print("ID:", id, "| Name:", info["name"], "| Qty:", qty, "| Status:", status) 

    def UpdateStock(self, i, q, d):
        id = i
        self.stock_data[id]["quantity"] = q
        self.stock_data[id]["expiry_date"] = d
        

        
   
    
