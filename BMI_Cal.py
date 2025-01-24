# BMI Calculation function

def BMI_Cal(weight: int, height: float):
    x = weight / (height * height)

    if x < 18.5:
        return "Underweight"
    elif x<25:
        return "Normal"
    elif x < 30:
        return "Overweight"
    else:
        return "Obesity"
