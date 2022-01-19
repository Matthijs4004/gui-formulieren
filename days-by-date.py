import tkinter as tk
import datetime
from time import strftime
from datetime import date
from tkinter import ttk
from tkinter import messagebox
from calendar import monthrange
from calendar import month_name

window = tk.Tk()
window.geometry("220x100")
window.title("Days By Date Calculator")
window.eval('tk::PlaceWindow . center') # optioneel (puur om het scherm in het midden te krijgen)

total_days = tk.IntVar()
selectedDay = tk.IntVar()
selectedMonth = tk.StringVar()
selectedYear = tk.IntVar()

def createWidgets():
    DayBox = ttk.Combobox(window, width=5,textvariable=selectedDay)
    DayBox['values'] = [[day] for day in range(1, total_days.get())]
    #DayBox.place(x=35, y=25)
    DayBox.grid(row=0, column=1, padx=10, pady=15)

    MonthBox = ttk.Combobox(window, width=5, textvariable=selectedMonth)
    MonthBox['values'] = [month_name[month][0:3] for month in range(1, 13)]
    #MonthBox.place(x=100, y=25)
    MonthBox.grid(row=0, column=2, padx=10, pady=15)

    YearEntry = ttk.Entry(window, width=8, textvariable=selectedYear)
    #YearEntry.place(x=165, y=25)
    YearEntry.grid(row=0, column=3, padx=10, pady=15)

def calculateButton():
    btn = tk.Button(window, width=5, text="Go", bd=0.5, activebackground="grey", command=calculateTime)
    #btn.place(x=100, y=50)
    btn.grid(row = 1, column=2)

def calculateTime():
    x = selectedMonth.get()
    future_day = selectedDay.get()
    future_month = datetime.datetime.strptime(x, '%b').month
    future_year = selectedYear.get()

    current_date = date.today()
    future_date = date(future_year, future_month, future_day)
    difference = future_date - current_date
    day_difference = difference.days
    
    if day_difference == 0:
        message = "Deze datum is vandaag"
    elif day_difference < 0:
        message = f"Deze datum was {day_difference} dagen geleden"
    else:
        message = f"Deze datum is {day_difference} dagen in de toekomst"

    messagebox.showinfo(None, message)

def localTime():
    current_local_time = datetime.datetime.now()

    current_day = current_local_time.day
    current_month = current_local_time.strftime('%b')
    current_month_num = current_local_time.month
    current_year = current_local_time.year
    current_days = monthrange(current_year, current_month_num)[1] + 1

    selectedDay.set(current_day)
    selectedMonth.set(current_month)
    selectedYear.set(current_year)
    total_days.set(current_days)

localTime()
createWidgets()
calculateButton()

d0 = date(2021, 12, 31)
d1 = date(2022, 12, 31)
delta = d1 - d0
window.mainloop()