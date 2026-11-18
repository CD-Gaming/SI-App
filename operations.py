import datetime
class Operations:

  def __init__(self):
    self.stock_data = {}

  def StockCheck(self, item_id: str) -> bool:
    return item_id in self.stock_data

  def StoreStock(self, item_id: str,name: str, qty: int, reorder: int, expiry_date: datetime.datetime):
    if self.StockCheck(item_id):
      raise KeyError(f"Product ID '{item_id}' already exists.")
    
    if qty < 0 or reorder < 0:
      raise ValueError("Quantity and reorder level cannot be negative.")

    self.stock_data[item_id] = {
        "name": name,
        "quantity": qty,
        "reorder_level": reorder,
        "initial_qty": qty,
        "expiry_date": expiry_date,
    }

  def ViewStock(self) -> list[tuple]:
    """Returns a list of tuples: (id, name, qty, expiry_str, status)"""
    if not self.stock_data:
      return []

    today = datetime.datetime.now()
    stock_list = []

    for item_id, info in self.stock_data.items():
      qty = info["quantity"]
      reorder = info["reorder_level"]
      initial = info.get("initial_qty", qty)
      expiry = info.get("expiry_date")

      status = "Normal"
      if expiry and expiry < today: #First check if expiry exists and then checks if the product is expired based off the expiry date and todays date
        status = "Expired - Restock/Removal Necessary"
      elif qty <= 0:
        status = "Out of Stock"
      elif qty <= reorder:
        status = "Low Stock"
      elif qty <= (initial / 2):
        status = "Average"

      exp_str = expiry.strftime("%d %m %Y") if expiry else "N/A" #shorthand if and day month year format
      stock_list.append((item_id, info["name"], qty, exp_str, status))

    return stock_list

  def UpdateStock(self, item_id: str, new_qty: int, new_expiry: datetime.datetime ):
    if not self.StockCheck(item_id):
      raise KeyError(f"Product ID '{item_id}' does not exist.") #except if the product id doesnt exist
    if new_qty < 0:
      raise ValueError("Quantity cannot be negative.")

    self.stock_data[item_id]["quantity"] = new_qty
    self.stock_data[item_id]["expiry_date"] = new_expiry