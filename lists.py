seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print("Available Seating:", seats)

while True:
    print("Available Seats:", seats)
    seat_numbers = input("Please type the seat number you would like to purchase: ")
    if seat_numbers.lower() == "done":
        break
    try:
        seat_number = int(seat_numbers)

        if seat_number < 1 or seat_number > 20:
            print("Invalid number")
        elif seat_number in seats:
            seats.remove(seat_number)
            print(f"Seat {seat_number} successfully purchased.")
        else:
            print(f"Seat {seat_number} is not available. Please select another.")
    except ValueError:
        print("Invalid input. Please enter a valid seat number or 'done' to finish.")

print("Updated Available Seating:", seats)