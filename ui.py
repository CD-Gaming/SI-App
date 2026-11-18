from tkinter import *
import tkinter.font as tkFont
#label: an area widget that holds text and/or an image within a window
#entry widget: textbox thats accepts a single line of user input

window = Tk()
window.geometry("540x400")# window size
window.title("Inventory Management App")
window.config(background="#276CF5")

#icon = PhotoImage(file='filename.filetype) to import the image the window's icon
#window.iconphoto(True,icon)
count = 0
def test():
    global count  #makes it accessiible to the whole program? or a function version of it
    count+= 1
    #print(count) doesnt appear in the window
    counter.config(text=count) #to show the changed number in the window  Can be used to change sets of buttons?
    if count == 5:
        choice_1.destroy()
        text1.config(text="This is crazy")

def submit():
    inputT= uinput_1.get() #gets whatever was typed in the text area
    print("This is what you type: " + inputT)

def delete():
    uinput_1.delete(0,END) #removes the line of text

bfont = tkFont.Font(family="Arial", size=15 , weight=tkFont.NORMAL) #reusable object
inputfont = tkFont.Font(family="Arial", size=11 , weight=tkFont.NORMAL)

#USER PROMPTS
heading = Label(window, #contains widgets
              text  ="Inventory Management Menu", 
              font  =('Sans',30,'bold'),
              fg    ="#0F0D05",   #forground(text color) color I believe using hexcode or name
            #  bg    = '#276CF5'
                relief=RAISED, #border type
                bd= 5, #border size
               # padx= , pady= padding for text
               #image = photo allows for images to be placed inside the label
               #compound='top' #affects the position of the image
              )
text1 = Label(window, #contains widgets
              text  ="Please choose an option below", 
              font  =('Sans',23),
              fg    ="#363535"  #forground(text color) color I believe using hexcode or name
     
              )

#USER OPTIONS
choice_1 = Button(window,
                  text='Record Stock'
                  )
choice_1.config(command=test, #can be used to refer to methods and functions? without the brackets. Performs call back of function
                font  = bfont, 
                fg='#595959'
                #activebackground='' Active background color
                #activeforeground=''
                #state=ACTIVE/DISABLED
                ) #config works for label objects too
counter = Label(window, text=count, font= bfont)

confirm = Button(window, 
                 text="Confirm", 
                 font=bfont,
                  fg='#595959', 
                 command=submit
                 )

delete = Button(window, 
                 text="delete", 
                 font=bfont,
                  fg='#595959', 
                 command=delete
                 )


uinput_1 = Entry() #doesnt require window
uinput_1.config(font= inputfont,
                width= 52 #size of the text area
                #,state=ACTIVE/DISABLED can also be disabled
                #show = '*' hides whatever is typed (password thing)
                )
#uinput_1.insert(0,'Eg: 1328') #default text

#The order in which they are packed or placed in sequential or from top to bottom
heading.pack()
text1.pack() #'place' allows you to pick the specifc location
choice_1.pack()
counter.pack()
uinput_1.pack()
confirm.pack(side = BOTTOM) #changes where the button is placed
delete.pack()

window.mainloop() #constantly keeps the frame open  
#ALL operations should be placed before here?
#pack function universally allows for the components to be placed on the window
#Automatically sets itself up
#Options are paned window or just an extra window
#PANED WINDOW SETUP AFTER SETTING THE WHOLE THING UP VIA GRID
#USE CLASSES/FUNCTION/METHODS TO UPDATE THE WINDOW AS THE PROGRAM IS OPENED
#HAVE IT SO THAT THE PANED WINDOW IS ALWAYS BEING REPLACED AFTER THE OPERATION IS DONE? USING CONFIG?
#CAN USE OVERRIDING TO CHANGE THE COMPONENTS
#OR SIMPLY OVERWRITE THEM OR TOPLEVEL WIndow
#Just use destroy object and keep recreating them for each option...
