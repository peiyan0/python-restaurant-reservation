# Purpose of the program: This program is a restaurant management system for Charming Thyme Trattoria.
# It allows users to make, cancel, update, and view reservations. 
# It also provides a random meal recommendation feature.

import csv
from datetime import datetime, timedelta
import random

# Class for storing reservation data
class Reservation:
    def __init__(self, date, session, name, email, phone, num_guests):
        # Constructor for Reservation class to initialize attributes
        self.date = date
        self.session = session
        self.name = name
        self.email = email
        self.phone = phone
        self.num_guests = num_guests

# Class for restaurant management system
class RestaurantManagementSystem:
    def __init__(self):
        self.reservations = [] # List to store reservation objects
    
    # Decorator function to add separators before and after a function call
    def decorator(func): 
        def wrapper(*args, **kwargs):
            print("="*100)
            func(*args, **kwargs)
            print("="*100)
        return wrapper
    
    # Add reservation function 
    @decorator
    def add_reservation(self):
        while len(self.reservations) < 32:
            date = self.get_valid_date()
            session = self.get_valid_session()

            # Check if the selected session on the specified date is fully booked
            session_count = sum(1 for reservation in self.reservations if reservation.date == date and reservation.session == session)
            if session_count >= 8:
                print("The selected session is fully booked. Please choose a different session.")
                continue

            # Allow user to input information for add reservation
            name = input("Enter the guest's name: ").strip()
            while name == "" or name.isnumeric():
                print("Invalid name format! Please enter a valid name (alphabetic characters only).")
                name = input("Enter the guest's name: ")
            name = name.upper()
            email = input("Enter the guest's email: ").strip()
            while email == "" or "@" not in email:
                print("Invalid email format! Please enter a valid email address.")
                email = input("Enter the guest's email: ")
            phone = input("Enter the guest's phone number: ").strip()
            while phone == "" or phone.isalpha() or len(phone) not in [10, 11]:
                print("Invalid phone format! Please enter a valid phone number (10-11 digits).")
                phone = input("Enter the guest's phone number: ")

            num_guests = self.get_valid_num_guests()

            # Append information into reservation list
            reservation = Reservation(date, session, name, email, phone, num_guests)
            self.reservations.append(reservation)
            print("Reservation added successfully!")

            # Ask user if they want to add another reservation
            add_another = input("Do you want to add another reservation? (Y/N): ").lower()
            if add_another != 'y':
                break
    
    # Function to get a valid date for reservation
    def get_valid_date(self):
        while True:
            date_str = input("Enter the reservation date (YYYY-MM-DD): ").strip()
            try:
                date = datetime.strptime(date_str, "%Y-%m-%d")
                # Check if the reservation date entered is valid
                if date < datetime.now() + timedelta(days=5):
                    print("Reservations must be made at least 5 days in advance.")
                else:
                    return date.strftime("%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")

    # Function to get a valid session number
    def get_valid_session(self):
        while True:
            print("Our restaurant has 4 sessions:")
            print("1: 12pm-2pm")
            print("2: 2pm-4pm")
            print("3: 6pm-8pm")
            print("4: 8pm-10pm")
            session = input("Enter the session (1-4): ")
            # Check if the session entered is valid
            if session not in ["1", "2", "3", "4"]:
                print("Invalid session. Please enter a session number between 1 and 4.")
            else:
                return "Slot " + session

    # Function to get a valid number of guests
    def get_valid_num_guests(self):
        while True:
            num_guests = input("Enter the number of guests: ")
            # Check if the number of guest is valid
            if not num_guests.isdigit():
                print("Invalid number. Please enter a valid number.")
            elif int(num_guests) not in range(1, 5):
                print("The restaurant seating accommodates a maximum of 4 guests in a single reservation.")
            else:
                return int(num_guests)
            
    # Cancel reservation function
    @decorator
    def cancel_reservation(self):
        while True:
            name = input("Enter the guest's name to cancel the reservation: ")
            canceled = False
            # Remove the reservation name which user input
            for reservation in self.reservations:
                if reservation.name.lower() == name.lower():
                    self.reservations.remove(reservation)
                    canceled = True

            if canceled:
                print("Reservation canceled successfully!")
            else:
                print("Reservation not found.")
            # Ask if user wants to cancel another reservation
            cancel_another = input("Do you want to cancel another reservation? (Y/N): ").lower()
            if cancel_another != 'y':
                break
    
    # Update reservation information
    @decorator
    def update_reservation(self): 
        while True:
            name = input("Enter the guest's name to update the reservation: ")
            found = False

            for reservation in self.reservations:
                if reservation.name.lower() == name.lower():
                    found = True
                    print("Reservation found! Please provide the updated information.\n")
                    reservation.date = self.get_valid_date()
                    reservation.session = self.get_valid_session()
                    reservation.num_guests = self.get_valid_num_guests()

                    print("Reservation updated successfully!")
                    break

            if not found:
                print("Reservation not found.")
            # Ask if user wants to update another reservation
            update_another = input("Do you want to update another reservation? (Y/N): ").lower()
            if update_another != 'y':
                break
  
    # Display all reservations function
    @decorator
    def display_reservations(self):
        if not self.reservations:
            print("No reservations found.")
            return
        # Print formatted reservation list
        print("Reservations:")
        print("{:<12} {:<10} {:<20} {:<30} {:<15} {:<12}".format(
            "Date", "Session", "Name", "Email", "Phone", "Guests"))
        for reservation in self.reservations:
            print("{:<12} {:<10} {:<20} {:<30} {:<15} {:<12d}".format(
                reservation.date, reservation.session, reservation.name,
                reservation.email, reservation.phone, reservation.num_guests))
   
    # Generate random meal recommendation function
    @decorator
    def generate_meal_recommendation(self): 
        try:
            with open('menuItems_21097837.txt', 'r') as file:
                menu_items = file.readlines()
                if not menu_items:
                    raise FileNotFoundError
        except FileNotFoundError:
            print("Menu items file not found.")
            return
        # Print one random meal by using import random
        random_recommendation = random.choice(menu_items).strip()
        print("Random Meal Recommendation:", random_recommendation)
  
    # Save reservation data into text file function
    def save_data_to_file(self): 
        try:
            with open('reservation_21097837.txt', 'w') as file:
                # Save formatted reservations into text file
                for reservation in self.reservations:
                    line = f"{reservation.date}|{reservation.session}|{reservation.name}|{reservation.email}|{reservation.phone}|{reservation.num_guests}\n"
                    file.write(line)
            print("Data saved to file successfully!")
        except Exception as e:
            print("Error saving data to file:", str(e))

# Procedure for the whole program
def main(): 
    restaurant = RestaurantManagementSystem()

    # Load reservations from file
    try:
        with open('reservation_21097837.txt', 'r') as file:
            reader = csv.reader(file, delimiter='|')
            for row in reader:
                # Check if the line has at least 6 fields
                if len(row) >= 6:
                    reservation = Reservation(row[0], row[1], row[2], row[3], row[4], int(row[5]))
                    restaurant.reservations.append(reservation)
    except FileNotFoundError:
        print("Reservation file not found.")

    print("\nWelcome to Charming Thyme Trattoria!")
    print("Home of Exquisite Fine Dining\n")

    while True:
        # Prints the main menu of the management system
        print("-"*55)
        print("Main Menu")
        print("-"*55)
        print("a) Add Reservation(s)")
        print("b) Cancel Reservation(s)")
        print("c) Edit Reservation(s)")
        print("d) View All Reservations")
        print("e) Surprise Me! - Generate Meal Recommendation")
        print("f) Exit")
        print("-"*55)

        choice = input("Enter your choice (a-f): ").lower()

        # Check which selection user input
        if choice == 'a':
            restaurant.add_reservation()
            restaurant.save_data_to_file()
        elif choice == 'b':
            restaurant.cancel_reservation()
            restaurant.save_data_to_file()
        elif choice == 'c':
            restaurant.update_reservation()
            restaurant.save_data_to_file()
        elif choice == 'd':
            restaurant.display_reservations()
        elif choice == 'e':
            restaurant.generate_meal_recommendation()
        elif choice == 'f':
            restaurant.save_data_to_file()
            print("\nThank you for dining at Charming Thyme Trattoria!")
            print("Have a wonderful day. Goodbye!\n")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() # Starts the main function
