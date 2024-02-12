#Enter the numeric grade you recieved
numeric_grade = (79)
print("Enter the numeric grade:")
print("" + str(numeric_grade) + "")
if numeric_grade > 89:
    print("The letter grade is A.")
elif numeric_grade > 79:
    print("The letter grade is B.")
elif numeric_grade > 69:
    print("The letter grade is C.")
elif numeric_grade > 59:
    print("The letter grade is D.")
elif numeric_grade < 51:
    print("The letter grade is F.")