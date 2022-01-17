# Clicker v5 (Autoclicker)
from cProfile import label
from msilib.schema import CheckBox
import tkinter as tk
from tkinter import IntVar

LastPressed = True
e = 0
number = 0
def Pressed():
    if LastPressed == True:
        Label.bind("<space>", UpTwo)
        Label.bind("<Double-Button-1>", UpTwo)
    elif LastPressed == False:
        Label.bind("<space>", DownTwo)
        Label.bind("<Double-Button-1>", DownTwo)

def Background():
    if number > 0:
        window["bg"] = "green"
    elif number < 0:
        window["bg"] = "red"
    else:
        window["bg"] = "grey"

def Hover(e):
    window["bg"] = "yellow"

def HoverLeave(e):
    Background()

def Up():
    global number, LastPressed
    LastPressed = True
    number +=1 
    Label['text'] = number
    Background()
    Pressed()
    CheckBox.configure(state = "normal")

def UpTwo(e):
    global number, LastPressed
    number = number * 3
    Label["text"] = number
    Background()
    LastPressed = False

def DownTwo(e):
    global number, LastPressed
    number = round((number/3),2)
    Label['text'] = number
    Background()
    LastPressed = True

def Down():
    global number, LastPressed
    LastPressed = False
    number -= 1
    Label['text'] = number
    Background()
    Pressed()
    CheckBox.configure(state = "normal")

def upButton(event):
    Up()

def downButton(event):
    Down()

def autoClick():
    global countCheck
    checkBox = Check.get()
    if checkBox == 1:
        if LastPressed == True:
            Up()
        elif LastPressed == False:
            Down()
        window.after(5000,autoClick)

window = tk.Tk()
window.title("Clicker v5 (AutoClicker)")
window.geometry("250x200")
window["bg"] = "grey"
window.eval('tk::PlaceWindow . center') # optioneel (puur om het scherm in het midden te krijgen)

buttonUp = tk.Button(bg="white", width=20, text="Up", bd=0, command=Up)
buttonUp.place(y=45,x=50)

Label = tk.Label(bg="white",width=20, text=number)
Label.place(y=100,x=50)

buttonDown = tk.Button(bg="white",width=20, text="Down", bd=0, command=Down)
buttonDown.place(y=150,x=50)

Check = tk.IntVar()
CheckBox = tk.Checkbutton(window, text = "Autoclick",command = autoClick,variable = Check,state = "disabled",onvalue = 1, offvalue = 0)
CheckBox.pack()

Label.bind("<Enter>", Hover)
Label.bind("<Leave>", HoverLeave)
window.bind("<Up>", Up)
window.bind("<Down>", Down)
window.bind("<Up>", upButton) and window.bind("<+>", upButton)
window.bind("<Down>", downButton) and window.bind("-", downButton)

window.mainloop()