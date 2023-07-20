import csv
from datetime import datetime, timedelta
import random

class Reservation:
    def __init__(self, date, session, name, email, phone, num_guests):
        self.date = date
        self.session = session
        self.name = name
        self.email = email
        self.phone = phone
        self.num_guests = num_guests

class RestaurantManagementSystem:
    def __init__(self):
        self.reservations = []

    def decorator(func): #decorates the functions
        def wrapper(*args, **kwargs):
            print("="*100)
            func(*args, **kwargs)
            print("="*100)
        return wrapper
    
    @decorator

    def add_reservation(self):
        while len(self.reservations) < 32:
            # Check if the all session is fully booked
            if len(self.reservations) >= 32:
                print("All sessions are fully booked. No more reservations can be made.")
                return
            date = self.get_valid_date()
            session = self.get_valid_session()
            # Check if the selected session is fully booked
            session_count = sum(1 for reservation in self.reservations if reservation.session == session)
            if session_count >= 8:
                print("The selected session is fully booked. Please choose a different session.")
                return
            # Format the session value as "Slot {session}"
            session = f"Slot {session}"

            # Allow user to input information for add reservation
            name = input("Enter the guest's name: ")
            while name == "" or name.isnumeric():
                print("Invalid name format!")
                name = input("Enter the guest's name: ")
            name = name.upper()
            email = input("Enter the guest's email: ")
            while email == "" or "@" not in email:
                print("Invalid email format!")
                email = input("Enter the guest's email: ")
            phone = input("Enter the guest's phone number: ")
            while phone == "" or phone.isalpha():
                print("Invalid phone format!")
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

    def get_valid_date(self):
        while True:
            date_str = input("Enter the reservation date (YYYY-MM-DD): ")
            try:
                date = datetime.strptime(date_str, "%Y-%m-%d")
                # Check if the reservation date entered is valid
                if date < datetime.now() + timedelta(days=5):
                    print("Reservations must be made at least 5 days in advance.")
                else:
                    return date.strftime("%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")

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
                return session

    def get_valid_num_guests(self):
        while True:
            num_guests = input("Enter the number of guests: ")
            # Check if the number of guest is valid
            if not num_guests.isdigit():
                print("Invalid number. Please enter a valid number.")
            elif int(num_guests) > 4:
                print("The restaurant seating accommodates a maximum of 4 guests in a group.")
            else:
                return int(num_guests)
    
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
    
    @decorator

    def update_reservation(self): # Update reservation information
        while True:
            name = input("Enter the guest's name to update the reservation: ")
            found = False

            for reservation in self.reservations:
                if reservation.name.lower() == name.lower():
                    found = True
                    print("Reservation found! Please provide the updated information.")
                    reservation.date = self.get_valid_date()
                    reservation.session = self.get_valid_session()
                    # Format the session value as "Slot {session}"
                    reservation.session = f"Slot {reservation.session}"
                    reservation.num_guests = self.get_valid_num_guests()

                    print("Reservation updated successfully!")
                    break

            if not found:
                print("Reservation not found.")
            # Ask if user wants to update another reservation
            update_another = input("Do you want to update another reservation? (Y/N): ").lower()
            if update_another != 'y':
                break
  
    @decorator

    def display_reservations(self): # Display entire reservation list
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
   
    @decorator

    def generate_meal_recommendation(self): # Generate random meal recommendation
        try:
            with open('menuItems_21097837.txt', 'r') as file:
                menu_items = file.readlines()
        except FileNotFoundError:
            print("Menu items file not found.")
            return
        # Print one random meal by using import random
        random_recommendation = random.choice(menu_items).strip()
        print("Random Meal Recommendation:", random_recommendation)
  
    @decorator

    def save_data_to_file(self): # Save reservation into text file
        try:
            with open('reservation_21097837.txt', 'w') as file:
                # Save formatted reservations into text file
                for reservation in self.reservations:
                    line = f"{reservation.date}|{reservation.session}|{reservation.name}|{reservation.email}|{reservation.phone}|{reservation.num_guests}\n"
                    file.write(line)
            print("Data saved to file successfully!")
        except Exception as e:
            print("Error saving data to file:", str(e))


def main(): # Procedure the whole program
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

    while True:
        # Prints the main menu of the management system
        print("-"*30)
        print("Main Menu")
        print("-"*30)
        print("a) Add Reservation(s)")
        print("b) Cancel Reservation(s)")
        print("c) Update/Edit Reservation(s)")
        print("d) Display Reservations")
        print("e) Generate Meal Recommendation")
        print("f) Exit")
        print("-"*30)

        choice = input("Enter your choice (a-f): ").lower()

        # Check which selection user input
        if choice == 'a':
            restaurant.add_reservation()
        elif choice == 'b':
            restaurant.cancel_reservation()
        elif choice == 'c':
            restaurant.update_reservation()
        elif choice == 'd':
            restaurant.display_reservations()
        elif choice == 'e':
            restaurant.generate_meal_recommendation()
        elif choice == 'f':
            restaurant.save_data_to_file()
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() # Starts the main function
