import json
from datetime import datetime

class BookingManager:
    def __init__(self, db_connector):
        self.db_connector = db_connector

    def get_expected_price(self, venue_id, date, start_time, end_time):
        schedules = self.db_connector.fetch_schedules()

        for schedule in schedules:
            if (
                schedule.venue_id == venue_id
                and schedule.date == date
                and schedule.start_time == start_time
                and schedule.end_time == end_time
            ):
                return schedule.price
        
        raise ValueError("Schedule not found")



    def check_duplicate_bookings(self):
        bookings = self.db_connector.fetch_bookings()
        
        # Create a set to store unique bookings
        unique_bookings = set()
        duplicate_found = False
        
        for booking in bookings:
            key = (booking.date, booking.start_time, booking.end_time)
            if key in unique_bookings:
                duplicate_found = True
                print(f"Duplicate booking found: {booking}")
            else:
                unique_bookings.add(key)
        
        if not duplicate_found:
            print("No duplicate bookings found")
    
    # Other booking management methods

    def insert_booking(self, booking_data):
        # Extract booking data
        booking_id = booking_data["Booking_id"]
        venue_id = booking_data["venue_id"]
        user_id = booking_data["User_id"]
        date = booking_data["date"]
        start_time = booking_data["Start_time"]
        end_time = booking_data["end_time"]
        price = booking_data["price"]

        # Construct SQL query
        query = """
        INSERT INTO bookings (booking_id, venue_id, user_id, date, start_time, end_time, price)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        # Execute the query with the provided data
        try:
            connection = self.db_connector.get_connection()
            with connection.cursor() as cursor:
                cursor.execute(query, (booking_id, venue_id, user_id, date, start_time, end_time, price))
                connection.commit()
                return cursor.lastrowid  # Return the ID of the inserted row
        except Exception as e:
            print("Error inserting booking:", str(e))
            connection.rollback()
            return None
        finally:
            connection.close()

    def fetch_bookings(self):
        return self.db_connector.fetch_bookings()

    def get_schedule(self):
        return self.schedule_data
