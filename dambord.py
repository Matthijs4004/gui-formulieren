import tkinter as tk

window = tk.Tk()
window.geometry("650x650")
window.title("Het Dambord")

i = False
for x in range(10):
    if i == True:
        i = False
    else:
        i = True
    for m in range(10):
        if i == True:
            kleur = "black"
            i = False
        else:
            kleur = "white"
            i = True
        vierkant = tk.Label(window, bg = kleur, padx = 30, pady = 20)
        vierkant.grid(row = x, column = m)

window.mainloop()



