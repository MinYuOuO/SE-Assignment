# BMI Calculation function
from tkinter import ttk

def BMI_Cal(weight: int, height: float):
    try:
        x = weight / (height * height)
        if x < 18.5:
            return "Underweight"
        elif x < 25:
            return "Normal"
        elif x < 30:
            return "Overweight"
        else:
            return "Obesity"
    except ZeroDivisionError:
        return "Height must be greater than zero"

def calculatorFunction(frameMain, weightEntry, heightEntry):
    try:
        weightAmount = float(weightEntry.get())
        heightAmount = float(heightEntry.get())
        result = BMI_Cal(weightAmount, heightAmount)

        # Make result text larger
        ttk.Label(frameMain, text=f"Result: {result}", font=("Arial", 14, "bold")).grid(column=0, row=4, columnspan=2)
    except ValueError:
        ttk.Label(frameMain, text="Invalid input. Enter numbers only.", font=("Arial", 12, "bold")).grid(column=0, row=4, columnspan=2)
