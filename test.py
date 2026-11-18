from tkinter import *

window = Tk()
window.geometry("600x400")
heading = Label(window, #contains widgets
                 text  ="Inventory Management Menu", 
                 font  =('Sans',30,'bold'),
                 fg    ="#0F0D05",   
                 relief=RAISED, 
                 bd= 2 ,
                 width= 25
                 ).grid(row=0,column=0, columnspan=3)
def mainMenu():
    h1 = Label(window, #contains widgets
              text  ="Please enter product info below", 
              font  =('Sans',20),
              fg    ="#0F0D05",  
              relief= RIDGE,
              bd = 1,
              width= 25
              )
    rec = Button(window,text='Record Stock',width=40)
    rec.config(command=recordS)

    upd = Button(window,text='Update Stock',width=40)
    upd.config(command=updateS)

    csl = Button(window,text='Check Stock Levels',width=40)
    csl.config(command=recordS)

    ir = Button(window,text='Inventory Report',width=40)
    ir.config(command=recordS)
    
    cb = Button(window,text='Contact Business',width=40)
    cb.config(command=recordS)

    ex = Button(window,text='Exit',width=40)
    ex.config(command=recordS)
    #Component placement
    h1.grid(row=3,column=0,columnspan=3)
    rec.grid(row=5,column=0,columnspan=3)
    upd.grid(row=6,column=0,columnspan=3)
    csl.grid(row=7,column=0,columnspan=3)
    ir.grid(row=8,column=0,columnspan=3)
    cb.grid(row=9,column=0,columnspan=3)
    ex.grid(row=10,column=0,columnspan=3)
    
    #Placeholders if need (none this time)
      
def recordS():
    def submit():
        id= proEntry.get() #CHECK IF THE PRODUCT ALREADY EXISTS
        Pname = nameEntry.get()
        quantity = amtEntry.get()
        reorder = reorderEntry.get()
        date = dateEntry.get()
        delete()
        print(id + Pname + quantity + reorder + date)

    def delete(): #Clear out the text areas after entering the data.
        proEntry.delete(0,END)
        nameEntry.delete(0,END)
        amtEntry.delete(0,END)
        reorderEntry.delete(0,END)
        dateEntry.delete(0,END)
    
    def back():
        heading.destroy()
        proID.destroy()
        proEntry.destroy()
        checkButton.destroy()
        name.destroy()
        nameEntry.destroy()
        amt.destroy()
        amtEntry.destroy()
        reorderEntry.destroy()
        reorderLv.destroy()
  
    def check():
        pass

    rec.destroy() #CHANGE THISsss
    sdadsa

    heading = Label(window, #contains widgets
              text  ="Please enter product info below", 
              font  =('Sans',20),
              fg    ="#0F0D05",  
              relief= RIDGE,
              bd = 1,
              width= 25
              )

    proID = Label(window, text='Product id: ')
    proEntry = Entry(window)
    
    checkButton = Button(window,text='Check for Id', width=15)
    checkButton.config(command=check)

    name = Label(window, text='Product name: ')
    nameEntry = Entry(window)

    amt = Label(window, text='Product amount: ') 
    amtEntry = Entry(window)    

    reorderLv = Label(window, text='Reorder Level: ')
    
    reorderEntry = Entry(window)

    expDate = Label(window, text='Expiry Date (DAY MONTH YEAR) format with spaces: ')
    dateEntry = Entry(window)
    
    submitButton = Button(window,text='Submit',width=7)
    submitButton.config(command=submit)
    backButton = Button(window,text='Back',width=7)
    backButton.config(command=back)


    #Component Placement
    heading.grid(row=1,column=0,columnspan=3)#stretches to go into 3 columns
    proID.grid(row=2,column=0)
    proEntry.grid(row=2,column = 1)
    checkButton.grid(row=2,column=2) 
    name.grid(row=4,column=0)
    nameEntry.grid(row=4,column = 1)
    amt.grid(row=6,column=0)
    amtEntry.grid(row=6,column = 1)
    reorderLv.grid(row=8,column=0) 
    reorderEntry.grid(row=8,column = 1)
    expDate.grid(row=10,column=0)
    dateEntry.grid(row=10,column = 1) 
    submitButton.grid(row=13,column=0,columnspan=1) #stretches to go into 1 columns
    backButton.grid(row=13,column=2,columnspan=1) #stretches to go into 1 columns

    #Placeholders
    Label(window).grid(row=3,column=0)
    Label(window).grid(row=5,column=0)
    Label(window).grid(row=7,column=0) 
    Label(window).grid(row=9,column=0) 
    Label(window).grid(row=11,column=0) 
    Label(window).grid(row=12,column=0) 
    
def updateS():
    pass
def checkStock():
    pass
def stockReport():
    pass
def contact():
    pass
def exit():
    pass
mainMenu()
#LAY THEM OUT LIKE THIS, SO THAT THEY BUTTONS OR ATTRIBUTES CAN EXIST FIRST BEFORE BEING ALLOWED TO DELTE THEM



window.mainloop()