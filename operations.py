class Operations: #Overloading doesnt exist for python
    def __init__(self): #Initialization
        self.stock_data = {} 
        self.log = []
    
    def StockCheck(self,i): #to check if the item is already in the system
        id = i
        if id in self.stock_data: 
            return True
        return False
    
    
    def StoreStock(self,i,n,q,r): #Python requires the use of self to know that it should access its own variables
        id = i
        name = n
        qty = q
        reorder = r 
                   
        self.stock_data[id] = {
            "name": name,
            "quantity": qty,
            "reorder_level": reorder,
            }

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

    def UpdateStock(self,i,q):
        id = i
        new_qty = q
        self.stock_data[id]["quantity"] = new_qty
        
        

        
   
    