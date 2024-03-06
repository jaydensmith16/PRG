# weight conversion calculator
weight_conversion = .453592
height_conversion = .0254
# Have user enter their weight and height in lbs and inches
weight = float(input("Enter you weight(lbs):"))
height = float(input("Enter you height(in):"))
# This part converts the lbs to kg
weight_kg = weight * weight_conversion
# This part converts m into in
height_m = height * height_conversion
# this part takes those calculations and puts them into the formula
bmi = weight_kg / (height_m * height_m)
# tells the answer to the calculation
print(f"Your bmi is {bmi:,.2f}")
# will print where ever you are on the bmi spectrum
if bmi < 18.5:
    print("You are underweight.")
if bmi > 18.5 and bmi < 25:
    print("You have a normal weight.")
if bmi > 30:
    print("You are obese.")