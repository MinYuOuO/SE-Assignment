import Function
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Small Tools")

frameMain = ttk.Frame(root, padding=10)
frameMain.grid()

# Labels and Input Fields
ttk.Label(frameMain, text="Welcome, user", font=("Arial", 16)).grid(column=0, row=0, columnspan=2)

ttk.Label(frameMain, text="Weight (kg):", font=("Arial", 16)).grid(column=0, row=1)
weightEntry = ttk.Entry(frameMain)
weightEntry.grid(column=1, row=1)

ttk.Label(frameMain, text="Height (m):", font=("Arial", 16)).grid(column=0, row=2)
heightEntry = ttk.Entry(frameMain)
heightEntry.grid(column=1, row=2)

# Button to Calculate BMI (calling function from Function.py)
ttk.Button(frameMain, text="Calculate BMI", command=lambda: Function.calculatorFunction(frameMain, weightEntry, heightEntry)).grid(column=0, row=3, columnspan=2)

# Exit Button
ttk.Button(frameMain, text="Exit", command=root.destroy).grid(column=0, row=5, columnspan=2)

root.mainloop()
