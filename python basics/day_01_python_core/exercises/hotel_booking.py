"""
Hotel booking calculator - positional, keyword n default
A hotel calculates the final bill based on:
●​ Number of rooms
●​ Number of nights
●​ Room price
●​ Breakfast charges
●​ Extra-bed charges
●​ Discount
Some charges are optional, and most bookings use standard values.
The program should allow a booking to be created using different combinations of
supplied information.
Example:
Booking 1:
3 rooms, 2 nights
Booking 2:
3 rooms, 2 nights, breakfast charges changed
Booking 3:
3 rooms, 2 nights, discount changed
"""

def hotel_calculator(num_rooms, num_nights, room_price, breakfast_charges, extra_bed_charges, discount):
    total_room_cost = num_rooms *room_price * num_nights
    total_breakfast_cost = num_rooms * breakfast_charges * num_nights
    total_extra_bed_cost = num_rooms * extra_bed_charges * num_nights
    total_cost = total_room_cost + total_breakfast_cost + total_extra_bed_cost
    total_cost_after_discount = total_cost - discount
    return total_cost_after_discount


rooms = int(input("Enter number of rooms: "))
nights = int(input("Enter number of nights: "))
room_price = int(input("Enter room price: "))
breakfast_charges = int(input("Enter breakfast charges: "))
extra_bed_charges = int(input("Enter extra bed charges: "))
discount = int(input("Enter discount: "))

cost = hotel_calculator(rooms, nights, room_price, breakfast_charges, extra_bed_charges, discount)
print("Total cost after discount: ", cost)
