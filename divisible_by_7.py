# Have the person enter an integer
integer_1 = 4
print("Enter an integer: " + str(integer_1) + "")
# Have the person enter another integer
integer_2 = 29
print("Enter another integer: " + str(integer_2) + "")
# see if both numbers are greater than zero
print("Both numbers greater than 0:")
if integer_1 > 0 or integer_2 > 0:
    print("True")
# integer 2 is the larger number
print("" + str(integer_2) + " is the larger number:")
if integer_1 < integer_2 and integer_2 > integer_1:
    print("True")
else:
    print("false")
# both numbers are greater than 20
print("both numbers are greater than 20:")
if integer_1 > 20 or integer_2 > 20:
    print("True")
else: 
    print("false")
# if the numbers are not negative, they are positive
print("The numbers are not negative.")
if not integer_1 < 0 and integer_2 < 0:
    print("false")
else:
    print("true")
# integer 1 is not 13
print("" + str(integer_1) +" is not 13")
if not integer_1 == 13:
    print("true")
else:
    print("false")
# the numbers are less than 100
print("Either number is less than 100.")
if integer_1 < 100 and integer_2 < 100:
    print("true")
else:
    print("false")