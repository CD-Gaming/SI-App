import datetime;
from operations import Operations;
stock_data = {}
initial_stock = {}
report = {}
log = []
Op = Operations()
def space_split(text: str) -> list[str]: #splits text into seperate parts based on spaces
            term = text.split(" ")
            return term
# main menu loop
while True:
    print("\n=== Inventory Management Menu ===")
    print("1. Record Stock")
    print("2. Update Inventory")
    print("3. Check Stock Levels")
    print("4. Inventory Report")
    print("5. Contact Business")
    print("6. Exit")
    
    choice = input("Enter choice: ")
    
    # option 1: add new stock item
    if choice == "1": #turn this into a while loop so that multiple products can be entered without having to constantly press 1, parameter (-1)
        item_id = input("Create product ID: ") 
       
        exist = Op.StockCheck(item_id)

        if exist == False:
            name = input("Enter product name: ")
            qty = int(input("Enter quantity: "))
            reorder = int(input("Enter reorder level: ")) #numeric value
            userI = input("Enter expirey date in 'YEAR MONTH DAY'format with spaces: ")
            holder = space_split(userI)
            date = datetime.datetime(int(holder[0]) ,int(holder[1]) ,int(holder[2]))
           
            Op.StoreStock(item_id,name,qty,reorder,date)
            
    # option 2: update existing stock quantity directly
#     elif choice == "2":
#         item_id = input("Enter product ID to update: ")
#         if item_id not in stock_data: #Inside a class start here
#             print("Item not found")
#         else:
#             new_qty = int(input("Enter new quantity: "))
#             time = datetime.datetime.now()
#             stock_data[item_id]["quantity"] = new_qty
#             report[item_id]["quantity"] = new_qty #for inventory report comparison
#             log = audit_log(item_id, new_qty,time)
#             print("Inventory updated successfully") #Stop here
            
#     # option 3: view all items and check low stock
    elif choice == "3":
        if not stock_data: #inside a class start here
            print("No stock records found")
        else:
            print("\nCurrent Stock Levels:")
            for id, info in stock_data.items():
                status = "Normal"
                if info["quantity"] <= info["reorder_level"]:
                    status = "Low Stock"
                print("ID:", id, "| Name:", info["name"], "| Qty:", info["quantity"], "| Status:", status) #stop here

#     elif choice == "4":
#         print("Initial stock: " ) #inside a class start here
#         for x, y in initial_stock.items():
#             print("ID: ", x ,"| Name: ", y["name"], "| Qty: ", y["quantity"], "| Expiry Date: ", y["expiry date"])
        
#         print("----------------------------------")
#         print(f"Updated stock: ")
#         for x, y in report.items():
#             print("ID: ", x ,"| Name: ", y["name"], "| Qty: ", y["quantity"], "| Expiry Date: ", y["expiry date"])

#         print("----------------------------------")        
#         print("Audit Logs: ")
#         [print(x) for x in log]

#         print("----------------------------------") #stop here

#     elif choice == "5":
#         c_name = input("Please enter the name of the company")
#         contact = input("Please enter the email that the request should be sent to")
#         amt = input("Please input the amount of required stock")
#     # option 6: leave the program
    elif choice == "5":
        print("Exiting program")
        break
    else:
        print("Invalid choice")

# #Info needed (create a seperate dictionary for the report? maybe find a way to store it though)
#     #Item amount, 
#     #name of the item, 
#     #item ID, 
#     #expiry date(include expiry date) 
#     #get some Ui going somehow- 
#     #prompt user to enter company email...submit a request through email? 
#     #Set a condition for reorder status to be low, average, out of stock
#     #Maybe compare specific products? 
#     #A different version is saved for every updated change made to the stock or maybe every few updates??
#     #Use a nested dictionary? for multiple reports
#     #Change the reports to an unchangeable storage type?
#     #Two conditions for stock renewal, Expired or low on product. Make into a function to check? If it is half 
#     # of the initial then return a value or warning for restock necesity.
#     # Should audit logs also show, when the products are added?
#     #implement exception handling



