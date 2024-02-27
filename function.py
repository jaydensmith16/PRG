# function definition
def square(side):
    area = side * side
    print("The area of the square is "+ str(area) +" square units")

#function definition
def circle(radius):
    print("The area of a circle is radius times radius times pi")
    pi = 3.14
    area_circle = radius * radius * pi
    print("The area of the circle is "+ str(area_circle) + " square units.")

square(4)
circle (5)