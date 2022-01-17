from cgitb import text
from select import select
import tkinter as tk
from datetime import date
from tkinter import LEFT, ttk
from turtle import bgcolor, width

window = tk.Tk()
window.geometry("250x100")
window.title("Days By Date Calculator")
window.eval('tk::PlaceWindow . center') # optioneel (puur om het scherm in het midden te krijgen)


selectedDay = tk.StringVar()
DayBox = ttk.Combobox(window, width=5,textvariable=selectedDay)
DayBox.place(x=35, y=25)

selectedMonth = tk.StringVar()
MonthBox = ttk.Combobox(window, width=5, textvariable=selectedMonth)
MonthBox.place(x=100, y=25)

selectedYear = tk.StringVar()
YearEntry = ttk.Entry(window, width=8, textvariable=selectedYear)
YearEntry.place(x=165, y=25)

d0 = date(2021, 12, 31)
d1 = date(2022, 12, 31)
delta = d1 - d0
window.mainloop()