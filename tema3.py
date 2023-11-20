import os 
os.system('cls')

seats = [0, 0, 1, 2, 0, 0, 0, 0]

free_seats = len(seats)

option = -1

while option != 0:
    
    print()
    for pi in range(len(seats)):
        print("", pi + 1, "", end="  ")
    print()

    for pi in range(len(seats)):
        if seats[pi] == 1:
            print("|-|", end="  ")
        elif seats[pi] == 2:
            print("|+|", end="  ")
        else:
            print("| |", end="  ")

    print("\nfree seats:", free_seats)
    print("\n")

    print("menu")
    print("1. book")
    print("2. buy")
    print("3. cancel")
    print("0. exit")
    print("--------------------")

    option = int(input(">>> "))

    if option == 1:
        place = int(input("which place: "))
        #hw 1 let's say free_seats =len( seats)
        if 1 <= place <= len(seats) and seats[place - 1] == 0:
            # Check if place is within boundaries and is free
            seats[place - 1] = 1
            free_seats -= 1  # Decrease free seats count when booking
        else:
            print("Invalid selection. Please choose a valid and free seat.")
          #hw2add cheack condition
          # -boundaries
          # -check if the place is  free
    elif option == 2:
        place = int(input("which place to buy: "))

        if 1 <= place <= len(seats) and seats[place - 1] == 1:
            # Check if place is within boundaries and is booked
            seats[place - 1] = 2
            print("Seat  bought successfully.")
        else:
            print("Invalid selection. Please choose a valid booked seat to buy.")

    elif option == 3:
        place = int(input("which place to cancel: "))
         #hw2- add buy , cancel + check only if booked!!!!
        if 1 <= place <= len(seats) and seats[place - 1] == 1:
            # Check if place is within boundaries and is booked
            seats[place - 1] = 0
            free_seats += 1  # Increase free seats count when canceling
            print("Booking for seat  canceled.")
        else:
            print("Invalid selection. Please choose a valid booked seat to cancel.")
