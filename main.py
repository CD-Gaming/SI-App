#Inventory Management App
import datetime
from operations import Operations
from auditlog import Log

Op = Operations()
Lg = Log()

def space_split(text: str) -> list[str]: 
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
    print("===================================")
    
    choice = input("Enter choice: ")
    
    # option 1: add new stock item
    if choice == "1":
        item_id = input("Create product ID: ") 
       
        exist = Op.StockCheck(item_id)

        if exist == False:
            name = input("Enter product name: ")
            
            try:
                qty = int(input("Enter quantity: "))
                reorder = int(input("Enter reorder level: ")) 
                userI = input("Enter expiry date 'DAY MONTH YEAR' format with spaces: ")
                holder = space_split(userI)
                date = datetime.datetime(int(holder[2]), int(holder[1]), int(holder[0]))
               
                Lg.StoreLog(item_id, name, qty, reorder, date)
                Op.StoreStock(item_id, name, qty, reorder, date)
            except ValueError:
                print("Error: Please enter valid numbers.")
            except IndexError:
                print("Error: Please enter the date with day, month, and year separated by spaces.")
        else:
            print("Error: Item already exists")
            
    # option 2: update existing stock quantity and expiry date
    elif choice == "2":
        item_id = input("Enter product ID to update: ")
       
        exist = Op.StockCheck(item_id)
        
        if exist == False: 
            print("Item not found")
        else:
            try:
                new_qty = int(input("Enter new quantity: "))
                userI = input("Update expiry date 'DAY MONTH YEAR' format with spaces: ")
                holder = space_split(userI)
                new_date = datetime.datetime(int(holder[2]), int(holder[1]), int(holder[0]))
                
                Op.UpdateStock(item_id, new_qty, new_date)
                Lg.UpdateLog(item_id, new_qty, new_date)   
                print("Inventory updated successfully")
            except ValueError:
                print("Error: Please enter valid numbers.")
            except IndexError:
                print("Error: Please enter the date with day, month, and year separated by spaces.")
            
    # option 3: view all items and check status
    elif choice == "3":
        Op.ViewStock()

    elif choice == "4":
        Lg.ShowLog()

#     elif choice == "5":
#         c_name = input("Please enter the name of the company")
#         contact = input("Please enter the email that the request should be sent to")
#         amt = input("Please input the amount of required stock")

    elif choice == "6":
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
    
     #Maybe compare specific products? 
     #A different version is saved for every updated change made to the stock or maybe every few updates??
     #Use a nested dictionary? for multiple reports
     #Change the reports to an unchangeable storage type?
   
     #Should audit logs also show, when the products are added?
    
     #Allow for all variables to be change able for the Update section?
