"""Writing guests to a text file"""

guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")
    
guests.close()

"""Printing file contents"""
with open("guests.txt") as guests:
    for line in guests:
        print(line)

"""Appending new guests and print"""
new_guests = ["Sam", "Danielle", "Jacob"]

with open("guests.txt", "a") as guests:
    for i in new_guests:
        guests.write(i + "\n")

guests.close()

with open("guests.txt") as guests:
    for line in guests:
        print(line)

"""Removing checkout guests"""
checked_out = ["Andrea", "Manuel", "Khalid"]
temp_list = []

with open("guests.txt", "r") as guests:
    for guest in guests:
        temp_list.append(guest.strip())

with open("guests.txt", "w") as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.write(name + "\n")

with open("guests.txt") as guests:
    for line in guests:
        print(line)

"""To check if guests are still checked in"""

guests_to_check = ["Bob", "Andrea"]
checked_in = []

with open("guests.txt", "r") as guests:
    for guest in guests:
        checked_in.append(guest.strip())
    for guest_to_check in guests_to_check:
        if guest_to_check in checked_in:
            print("{} is checked in".format(guest_to_check))
        else:
            print("{} is not checked in".format(guest_to_check))