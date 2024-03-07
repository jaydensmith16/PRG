# Simple Python program to calculate the square of a number

def square_number():
    try:
        number = input("Enter a number to square: ")
        squared_number = int(number) ** 2
        print(f"The square of {number} is {squared_number}.")
    # for when it is a type error
    except TypeError:
        print("An error occured. Please enter an integer.")
    # for when it is a value error
    except ValueError:
        print("An error occured. Please enter an integer.")


square_number()
