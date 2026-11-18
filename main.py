import datetime
import re
import smtplib
from email.message import EmailMessage
from tkinter import *
from tkinter import messagebox
from auditlog import Log
from operations import Operations

window = Tk()
window.geometry("720x500")
window.title("Inventory Management App")

Op = Operations()
Lg = Log()

# Persistent Top Header
Label(
    window,
    text="Inventory Management System",
    font=("Sans", 24, "bold"),
    fg="#0F0D05",
    relief=RAISED,
    bd=2,
    width=32,
).pack(pady=10)

# Container frame that gets swapped out when navigating between sections
container = Frame(window)
container.pack(fill=BOTH, expand=True, padx=20, pady=10) #automatically fills the window for the relevant widgets to be placed


def clear_container():
  for widget in container.winfo_children(): #loops through all currently created widgets or app components
    widget.destroy() #removes all widgets from the current frame in the window


def parse_date(date_str: str) -> datetime.datetime: #Parse entered date, so that it can be input into the datetime class
  """Parses 'DD MM YYYY' into a datetime object with strict validation."""
  cleaned = date_str.strip()
  try:
    return datetime.datetime.strptime(cleaned, "%d %m %Y")
  except ValueError:
    raise ValueError(
        "Invalid date format. Please use 'DD MM YYYY' (e.g., 25 12 2026)."
    )


def mainMenu():
  clear_container()

  Label(
      container,
      text="Main Menu",
      font=("Sans", 18),
      fg="#0F0D05",
      relief=RIDGE,
      bd=1,
      width=30,
  ).pack(pady=10)

  buttons = [
      ("Record Stock", recordS),
      ("Update Stock", updateS),
      ("Check Stock Levels", checkS),
      ("Inventory Report", stockR),
      ("Contact Business", contact),
      ("Exit", window.destroy),
  ]

  for text, cmd in buttons:
    Button(container, text=text, width=40, font=("Sans", 11), command=cmd).pack(pady=5)


def recordS():
  clear_container()

  Label(
      container,
      text="Record New Product",
      font=("Sans", 16, "bold"),
      relief=RIDGE,
      bd=1,
      width=30,
  ).grid(row=0, column=0, columnspan=3, pady=10)

  Label(container, text="Product ID:").grid(row=1, column=0, sticky=W, pady=5)
  proEntry = Entry(container, width=25)
  proEntry.grid(row=1, column=1, pady=5)

  def check():
    item_id = proEntry.get().strip()
    if not item_id:
      messagebox.showwarning("Input Required", "Please enter a Product ID.")
      return
    if Op.StockCheck(item_id):
      messagebox.showerror(
          "Duplicate ID", f"Product ID '{item_id}' already exists!"
      )
    else:
      messagebox.showinfo("Available", f"Product ID '{item_id}' is available.")

  Button(container, text="Check ID", width=15, command=check).grid(
      row=1, column=2, padx=5
  )

  Label(container, text="Product Name:").grid(row=2, column=0, sticky=W, pady=5)
  nameEntry = Entry(container, width=25)
  nameEntry.grid(row=2, column=1, pady=5)

  Label(container, text="Product Amount:").grid(
      row=3, column=0, sticky=W, pady=5
  )
  amtEntry = Entry(container, width=25)
  amtEntry.grid(row=3, column=1, pady=5)

  Label(container, text="Reorder Level:").grid(row=4, column=0, sticky=W, pady=5)
  reorderEntry = Entry(container, width=25)
  reorderEntry.grid(row=4, column=1, pady=5)

  Label(container, text="Expiry Date (DD MM YYYY):").grid(
      row=5, column=0, sticky=W, pady=5
  )
  dateEntry = Entry(container, width=25)
  dateEntry.grid(row=5, column=1, pady=5)

  def submit():
    try:
      item_id = proEntry.get().strip()
      name = nameEntry.get().strip()
      raw_qty = amtEntry.get().strip()
      raw_reorder = reorderEntry.get().strip()
      raw_date = dateEntry.get().strip()

      if not all([item_id, name, raw_qty, raw_reorder, raw_date]):
        raise ValueError("All fields are required.")

      qty = int(raw_qty)
      reorder = int(raw_reorder)
      expiry_dt = parse_date(raw_date)

      Op.StoreStock(item_id, name, qty, reorder, expiry_dt)
      Lg.StoreLog(item_id, name, qty, reorder, expiry_dt)

      messagebox.showinfo("Success", f"Product '{name}' recorded successfully!")
      for entry in (proEntry, nameEntry, amtEntry, reorderEntry, dateEntry):
        entry.delete(0, END) #indicats where the new component should be added or what should be removed from where

    except KeyError as e: #Checks for duplicates, if true returns an error message box
      messagebox.showerror("Duplicate Entry", str(e))
    except ValueError as e: #Check for incorrect value input
      messagebox.showerror("Invalid Input", str(e))
    except Exception as e: #general Error
      messagebox.showerror("Error", f"An unexpected error occurred: {e}")

  Button(container, text="Submit", width=12, command=submit).grid(row=6, column=0, pady=20)
  Button(container, text="Back", width=12, command=mainMenu).grid(row=6, column=2, pady=20)


def updateS():
  clear_container()

  Label(
      container,
      text="Update Existing Stock",
      font=("Sans", 16, "bold"),
      relief=RIDGE,
      bd=1,
      width=30,
  ).grid(row=0, column=0, columnspan=3, pady=10)

  Label(container, text="Product ID:").grid(row=1, column=0, sticky=W, pady=5)
  proEntry = Entry(container, width=25)
  proEntry.grid(row=1, column=1, pady=5)

  def check():
    item_id = proEntry.get().strip()
    if not item_id:
      messagebox.showwarning("Input Required", "Please enter a Product ID.")
      return
    if Op.StockCheck(item_id):
      info = Op.stock_data[item_id]
      messagebox.showinfo(
          "Product Found",
          f"Name: {info['name']}\nCurrent Qty: {info['quantity']}\n"
          f"Expiry: {info['expiry_date'].strftime('%d %m %Y')}",
      )
    else:
      messagebox.showerror(
          "Not Found", f"Product ID '{item_id}' does not exist."
      )

  Button(container, text="Check ID", width=15, command=check).grid(
      row=1, column=2, padx=5
  )

  Label(container, text="New Quantity:").grid(row=2, column=0, sticky=W, pady=5)
  amtEntry = Entry(container, width=25)
  amtEntry.grid(row=2, column=1, pady=5)

  Label(container, text="New Expiry Date (DD MM YYYY):").grid(
      row=3, column=0, sticky=W, pady=5
  )
  dateEntry = Entry(container, width=25)
  dateEntry.grid(row=3, column=1, pady=5)

  def submit():
    try:
      item_id = proEntry.get().strip() #remove spaces
      raw_qty = amtEntry.get().strip()
      raw_date = dateEntry.get().strip()

      if not all([item_id, raw_qty, raw_date]):
        raise ValueError("All fields are required.")

      new_qty = int(raw_qty)
      new_date = parse_date(raw_date)

      Op.UpdateStock(item_id, new_qty, new_date)
      Lg.UpdateLog(item_id, new_qty, new_date)

      messagebox.showinfo(
          "Updated", f"Stock for ID '{item_id}' updated successfully!"
      )
      for entry in (proEntry, amtEntry, dateEntry):
        entry.delete(0, END)

    except KeyError as e:
      messagebox.showerror("Not Found", str(e))
    except ValueError as e:
      messagebox.showerror("Invalid Input", str(e))
    except Exception as e:
      messagebox.showerror("Error", f"An unexpected error occurred: {e}")

  Button(container, text="Submit", width=12, command=submit).grid(row=4, column=0, pady=20)
  Button(container, text="Back", width=12, command=mainMenu).grid(row=4, column=2, pady=20)


def checkS():
  clear_container()

  Label(container, text="Current Stock Levels", font=("Sans", 16, "bold"), relief=RIDGE, bd=1, width=30).pack(pady=8)

  list_frame = Frame(container)
  list_frame.pack(fill=BOTH, expand=True, pady=5)

  scrollbar = Scrollbar(list_frame, orient=VERTICAL)
  listbox = Listbox(list_frame, font=("Courier", 10), yscrollcommand=scrollbar.set, height=12 )
  scrollbar.config(command=listbox.yview)
  scrollbar.pack(side=RIGHT, fill=Y)
  listbox.pack(side=LEFT, fill=BOTH, expand=True)

  try:
    stock_tuples = Op.ViewStock()
    if not stock_tuples:
      listbox.insert(END, "No stock records found.")
    else:
      header = f"{'ID':<8} | {'Name':<16} | {'Qty':<6} | {'Expiry':<12} | {'Status'}"
      listbox.insert(END, header)
      listbox.insert(END, "-" * 75)
      for item_id, name, qty, exp_str, status in stock_tuples:
        row = f"{item_id:<8} | {name:<16} | {qty:<6} | {exp_str:<12} | {status}" #formatted string with the information
        listbox.insert(END, row)
  except Exception as e: #Goes to this excpetion if an unexpected error prevents the code from retrieving the view stock method
    messagebox.showerror("Error", f"Failed to load stock levels: {e}")

  Button(container, text="Back to Menu", width=15, command=mainMenu).pack(
      pady=10
  )


def stockR(): #Stock Records option
  clear_container()

  Label(container, text="Inventory & Audit Report", font=("Sans", 16, "bold"), relief=RIDGE, bd=1, width=30 ).pack(pady=8)

  list_frame = Frame(container)
  list_frame.pack(fill=BOTH, expand=True, pady=5)

  scrollbar = Scrollbar(list_frame, orient=VERTICAL)
  listbox = Listbox(list_frame, font=("Courier", 9), yscrollcommand=scrollbar.set, height=14) 
  scrollbar.config(command=listbox.yview)
  scrollbar.pack(side=RIGHT, fill=Y)
  listbox.pack(side=LEFT, fill=BOTH, expand=True)

  try:
    data = Lg.ShowLog()

    listbox.insert(END, "=== INITIAL STOCK ===")
    if not data["initial"]: #if there is no initial stock available
      listbox.insert(END, "No initial stock recorded.")
    else:
      for item_id, name, qty, exp_str in data["initial"]:
        listbox.insert(
            END,
            f"ID: {item_id:<8} | Name: {name:<15} | Qty: {qty:<5} | Expiry: {exp_str}",
        )

    listbox.insert(END, "")
    listbox.insert(END, "=== UPDATED STOCK REPORT ===")
    if not data["report"]: #if there is no report available 
      listbox.insert(END, "No updated stock records.")
    else:
      for item_id, name, qty, exp_str, status in data["report"]:
        listbox.insert(
            END, #indicats where the new component should be added
            f"ID: {item_id:<8} | Name: {name:<15} | Qty: {qty:<5} | Exp: {exp_str} | {status}",
        )

    listbox.insert(END, "")
    listbox.insert(END, "=== AUDIT LOGS ===")
    if not data["logs"]:
      listbox.insert(END, "No changes logged yet.")
    else:
      for entry in data["logs"]:
        listbox.insert(END, entry)

  except Exception as e:
    messagebox.showerror("Error", f"Failed to generate report: {e}")

  Button(container, text="Back to Menu", width=15, command=mainMenu).pack(pady=10)


def contact():
  clear_container()

  Label(
      container,
      text="Contact Supplier / Business",
      font=("Sans", 16, "bold"),
      relief=RIDGE,
      bd=1,
      width=30,
  ).grid(row=0, column=0, columnspan=2, pady=10)

  Label(container, text="Your Email:").grid(row=1, column=0, sticky=W, pady=5)
  senderEntry = Entry(container, width=35)
  senderEntry.grid(row=1, column=1, pady=5)

  Label(container, text="Company Email:").grid(row=2, column=0, sticky=W, pady=5)
  recipientEntry = Entry(container, width=35)
  recipientEntry.grid(row=2, column=1, pady=5)

  Label(container, text="Subject:").grid(row=3, column=0, sticky=W, pady=5)
  subjectEntry = Entry(container, width=35)
  subjectEntry.grid(row=3, column=1, pady=5)

  Label(container, text="Message:").grid(row=4, column=0, sticky=NW, pady=5)
  msgText = Text(container, width=35, height=6)
  msgText.grid(row=4, column=1, pady=5)

  def send_email():
    sender = senderEntry.get().strip()#removes spaces and stoer
    recipient = recipientEntry.get().strip()
    subject = subjectEntry.get().strip()
    body = msgText.get("1.0", END).strip()#text size

    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$" #validates email and stores it in email_pattern
    try:
      if not re.match(email_pattern, sender) or not re.match(
          email_pattern, recipient
      ):
        raise ValueError("Please enter valid email addresses.")
      if not subject or not body:
        raise ValueError("Subject and message body cannot be empty.")

      #Configure SMTP credentials below to send live emails
      #Allows for users to enter information to send and email.
      
      SMTP_SERVER = "smtp.gmail.com"
      SMTP_PORT = 465
      APP_PASSWORD = "rwnv llqp avgi sxzg" #Changes based on the specific company email being used to send the password #this works with Nathanael's personal email

      msg = EmailMessage()
      msg["Subject"] = f"[Inventory Inquiry from {sender}] {subject}"
      msg["From"] = sender
      msg["To"] = recipient
      msg["Reply-To"] = sender
      msg.set_content(f"Sender Contact: {sender}\n\n{body}")

      with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp: #Connects to email provider
        smtp.login(sender, APP_PASSWORD) #allows for user to log in
        smtp.send_message(msg) #sends email

      messagebox.showinfo("Sent", f"Email sent to {recipient}!")
      mainMenu()

    except ValueError as e:
      messagebox.showwarning("Validation Error", str(e))
    except smtplib.SMTPAuthenticationError:
      messagebox.showerror(
          "Authentication Failed",
          "Could not log in to the mail server. Check your email and App Password.",
      )
    except Exception as e:
      messagebox.showerror("Email Error", f"Failed to send email: {e}")

  Button(container, text="Send Email", width=15, command=send_email).grid(row=5, column=0, pady=15)
  Button(container, text="Back", width=15, command=mainMenu).grid(row=5, column=1, pady=15)


mainMenu()
window.mainloop()


