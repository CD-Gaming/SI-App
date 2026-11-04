import datetime;
stock_data = {}
initial_stock = {}
report = {}
log = []
#count = 1;
def space_split(text: str) -> list[str]:
    term = text.split(" ")
    return term

def audit_log(text: str, text2:str, date:datetime) -> list[str]: #works not find a way to remove the milliseconds that show up on the time log
    info = f"{date} : Item ID label {text}  was changed to {text2}"
    log.append(info)
    return log

# main menu loop
while True:
    print("\n=== Inventory Management Menu ===")
    print("1. Record Stock")
    print("2. Update Inventory")
    print("3. Check Stock Levels")
    print("4. Inventory Report")
    print("5. Exit")
    
    choice = input("Enter choice: ")
    
    # option 1: add new stock item
    if choice == "1": #turn this into a while loop so that multiple products can be entered without having to constantly press 1, parameter (-1)
        item_id = input("Create product ID: ") 
        if item_id in stock_data:
            print("Error: Item already exists")
        else:
            name = input("Enter product name: ")
            qty = int(input("Enter quantity: "))
            reorder = int(input("Enter reorder level: "))
            userI = input("Enter expirey date in 'YEAR MONTH DAY'format with spaces: ")
            holder = space_split(userI)
            date = datetime.datetime(int(holder[0]) ,int(holder[1]) ,int(holder[2]))
            stock_data[item_id] = {
                "name": name,
                "quantity": qty,
                "reorder_level": reorder,
            }
#Different so tht they dont mix info?? and so that I can save different versions of this one for weekly
#or monthly reports allowing for difference comparison
            initial_stock[item_id] = { 
                "name": name,
                "quantity": qty,
                "reorder_level": reorder,
                "expiry date" : date
            }

            report[item_id] = {
                "name": name,
                "quantity": qty,
                "reorder_level": reorder,
                "expiry date" : date
            }

            #dont save expiry date to stock levels.
            print("Stock recorded successfully")
            
    # option 2: update existing stock quantity directly
    elif choice == "2":
        item_id = input("Enter product ID to update: ")
        if item_id not in stock_data:
            print("Item not found")
        else:
            new_qty = int(input("Enter new quantity: "))
            time = datetime.datetime.now()
            stock_data[item_id]["quantity"] = new_qty
            report[item_id]["quantity"] = new_qty #for inventory report comparison
            log = audit_log(item_id, new_qty,time)
            print("Inventory updated successfully")
            
    # option 3: view all items and check low stock
    elif choice == "3":
        if not stock_data:
            print("No stock records found")
        else:
            print("\nCurrent Stock Levels:")
            for id, info in stock_data.items():
                status = "Normal"
                if info["quantity"] <= info["reorder_level"]:
                    status = "Low Stock"
                print("ID:", id, "| Name:", info["name"], "| Qty:", info["quantity"], "| Status:", status)

    elif choice == "4":
        print("Initial stock: " )
        for x, y in initial_stock.items():
            print("ID: ", x ,"| Name: ", y["name"], "| Qty: ", y["quantity"], "| Expiry Date: ", y["expiry date"])
        
        print("----------------------------------")
        print(f"Updated stock: ")
        for x, y in report.items():
            print("ID: ", x ,"| Name: ", y["name"], "| Qty: ", y["quantity"], "| Expiry Date: ", y["expiry date"])

        print("----------------------------------")        
        print("Audit Logs: ")
        [print(x) for x in log]

        print("----------------------------------")

    # option 6: leave the program
    elif choice == "5":
        print("Exiting program")
        break
    else:
        print("Invalid choice")

#Info needed (create a seperate dictionary for the report? maybe find a way to store it though)
    #Item amount, 
    #name of the item, 
    #item ID, 
    #expiry date(include expiry date) 
    #get some Ui going somehow- 
    #prompt user to enter company email...submit a request through email? 
    #Set a condition for reorder status to be low, average, out of stock
    #Maybe compare specific products? 
    #A different version is saved for every updated change made to the stock or maybe every few updates??
    #Use a nested dictionary? for multiple reports
    #Change the reports to an unchangeable storage type?
    #Two conditions for stock renewal, Expired or low on product. Make into a function to check? If it is half 
    # of the initial then return a value or warning for restock necesity.
    # Should audit logs also show, when the products are added?
    #implement exception handling



