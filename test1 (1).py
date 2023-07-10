import csv
from datetime import datetime, timedelta

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

    def add_reservation(self):
        date = self.get_valid_date()
        session = self.get_valid_session()
        name = input("Enter the guest's name: ")
        while name == "" or name.isnumeric():
            print("Invalid name format!")
            name = input("Enter the guest's name: ")
        email = input("Enter the guest's email: ")
        while email == "" or "@" not in email:
            print("Invalid email format!")
            email = input("Enter the guest's email: ")
        phone = input("Enter the guest's phone number: ")
        while phone == "" or phone.isalpha():
            print("Invalid phone format!")
            phone = input("Enter the guest's phone number: ")

        num_guests = self.get_valid_num_guests()

        reservation = Reservation(date, session, name, email, phone, num_guests)
        self.reservations.append(reservation)
        print("Reservation added successfully!")

    def get_valid_date(self):
        while True:
            date_str = input("Enter the reservation date (YYYY-MM-DD): ")
            try:
                date = datetime.strptime(date_str, "%Y-%m-%d")
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
            if session not in ["1", "2", "3", "4"]:
                print("Invalid session. Please enter a session number between 1 and 4.")
            else:
                return session

    def get_valid_num_guests(self):
        while True:
            num_guests = input("Enter the number of guests: ")
            if not num_guests.isdigit():
                print("Invalid number. Please enter a valid number.")
            elif int(num_guests) > 4:
                print("The restaurant seating accommodates a maximum of 4 guests in a group.")
            else:
                return int(num_guests)

    def cancel_reservation(self):
        name = input("Enter the guest's name to cancel the reservation: ")
        canceled = False

        for reservation in self.reservations:
            if reservation.name.lower() == name.lower():
                self.reservations.remove(reservation)
                canceled = True

        if canceled:
            print("Reservation canceled successfully!")
        else:
            print("Reservation not found.")

    def update_reservation(self):
        name = input("Enter the guest's name to update the reservation: ")
        found = False

        for reservation in self.reservations:
            if reservation.name.lower() == name.lower():
                found = True
                print("Reservation found! Please provide the updated information.")
                reservation.date = self.get_valid_date()
                reservation.session = self.get_valid_session()
                reservation.num_guests = self.get_valid_num_guests()

                print("Reservation updated successfully!")
                break

        if not found:
            print("Reservation not found.")

    def display_reservations(self):
        if not self.reservations:
            print("No reservations found.")
            return

        print("Reservations:")
        print("{:<12} {:<10} {:<20} {:<20} {:<12} {:<12}".format(
            "Date", "Session", "Name", "Email", "Phone", "Guests"))
        for reservation in self.reservations:
            print("{:<12} {:<10} {:<20} {:<20} {:<12} {:<12}".format(
                reservation.date, reservation.session, reservation.name,
                reservation.email, reservation.phone, reservation.num_guests))

    def generate_meal_recommendation(self):
        try:
            with open('menuItems_21097837.txt', 'r') as file:
                menu_items = file.readlines()
        except FileNotFoundError:
            print("Menu items file not found.")
            return

        random_recommendation = random.choice(menu_items).strip()
        print("Random Meal Recommendation:", random_recommendation)

    def save_data_to_file(self):
        try:
            with open('reservation_21097837.txt', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Date', 'Session', 'Name', 'Email', 'Phone', 'Guests'])
                for reservation in self.reservations:
                    writer.writerow([reservation.date, reservation.session, reservation.name,
                                     reservation.email, reservation.phone, reservation.num_guests])
            print("Data saved to file successfully!")
        except IOError as e:
            print("Error saving data to file:", str(e))

def main():
    restaurant = RestaurantManagementSystem()

    # Load reservations from file
    try:
        with open('reservation_21097837.txt', 'r') as file:
            reader = csv.reader(file, delimiter='|')
            next(reader)  # Skip header row
            for row in reader:
                if len(row) >= 6:  # Check if the line has at least 6 fields
                    reservation = Reservation(row[0], row[1], row[2], row[3], row[4], int(row[5]))
                    restaurant.reservations.append(reservation)
            else:
                print("Invalid line:", row)

        print("Reservations loaded successfully!")
    except FileNotFoundError:
        print("Reservation file not found.")

    while True:
        print("Main Menu")
        print("---------")
        print("a) Add Reservation(s)")
        print("b) Cancel Reservation(s)")
        print("c) Update/Edit Reservation(s)")
        print("d) Display Reservations")
        print("e) Generate Meal Recommendation")
        print("f) Exit")

        choice = input("Enter your choice (a-f): ").lower()

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
    main()

