## Restaurant Management System

### Overview
This program is a restaurant management system for Charming Thyme Trattoria. It allows users to make, cancel, update, and view reservations. It also provides a random meal recommendation feature.


### Files

`main.py`: main script for the restaurant management system. 

`menuItems_21097837.txt`: contains a list of menu items available at the restaurant. Each item is listed on a new line.

`reservation_21097837.txt`: stores the reservation data. Each reservation is stored in the following format:

    `YYYY-MM-DD|Slot X|NAME|EMAIL|PHONE|NUM_GUESTS`

### Features
**Add Reservation**: Allows users to add a new reservation.  
**Cancel Reservation**: Allows users to cancel an existing reservation.  
**Update Reservation**: Allows users to update the details of an existing reservation.  
**View All Reservations**: Displays all current reservations.  
**Generate Random Meal Recommendation**: Provides a random meal recommendation from the menu.  

### Data Persistence
- Reservations are loaded from reservation_21097837.txt at the start of the program.
- Any changes to reservations (add, cancel, update) are saved back to reservation_21097837.txt.

### Menu Items
- The menu items are read from menuItems_21097837.txt for the random meal recommendation feature.