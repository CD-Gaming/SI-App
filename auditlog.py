import datetime
class Log:

  def __init__(self):
    self.initial_stock = {}
    self.report = {}
    self.log = []

  def audit_log_store(
      self, item_id: str, old_qty: int, new_qty: int, date: datetime.datetime
  ) -> list[str]:
    info = (
        f"{date.strftime('%Y-%m-%d %H:%M:%S')} : Item ID '{item_id}' "
        f"quantity changed from {old_qty} to {new_qty}"
    )
    self.log.append(info)
    return self.log

  def StoreLog(self, item_id: str,  name: str,  qty: int, reorder: int,  expiry_date: datetime.datetime, ):
    entry = {
        "name": name,
        "quantity": qty,
        "initial_qty": qty,
        "reorder_level": reorder,
        "expiry_date": expiry_date,
    }
    self.initial_stock[item_id] = entry.copy()
    self.report[item_id] = entry.copy()

  def UpdateLog(self, item_id: str, new_qty: int, new_date: datetime.datetime ):
    if item_id not in self.report:
      raise KeyError(f"Product ID '{item_id}' not found in audit report.")

    old_qty = self.report[item_id]["quantity"]
    now = datetime.datetime.now()

    self.audit_log_store(item_id, old_qty, new_qty, now)
    self.report[item_id]["quantity"] = new_qty
    self.report[item_id]["expiry_date"] = new_date

  def ShowLog(self) -> dict:
   # """Returns structured tuples for initial stock, updated report, and audit logs."""
    today = datetime.datetime.now()

    initial_list = []
    for item_id, y in self.initial_stock.items():
      exp_str = y["expiry_date"].strftime("%d %m %Y")
      initial_list.append((item_id, y["name"], y["quantity"], exp_str))

    report_list = []
    for item_id, y in self.report.items():
      qty = y["quantity"]
      initial = y.get("initial_qty", qty)
      reorder = y["reorder_level"]
      expiry = y["expiry_date"]

      status = "Normal"
      if expiry and expiry < today:
        status = "Expired - Restock/Removal Necessary"
      elif qty <= 0:
        status = "Out of Stock"
      elif qty <= reorder:
        status = "Low Stock"
      elif qty <= (initial / 2):
        status = "Average"

      exp_str = expiry.strftime("%d %m %Y")
      report_list.append((item_id, y["name"], qty, exp_str, status))

    return {
        "initial": initial_list,
        "report": report_list,
        "logs": list(self.log),
    }
