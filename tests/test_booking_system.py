import unittest
from datetime import datetime
from booking_system.booking_manager import BookingManager
from booking_system.database_connector import DatabaseConnector

class TestBookingSystem(unittest.TestCase):

    def setUp(self):
        self.db_connector = DatabaseConnector()
        self.booking_manager = BookingManager(self.db_connector)

    def tearDown(self):
        self.db_connector.close_connection()

    def test_insert_booking(self):
        print("--------------------------------------------------------")
        booking_data = {
            "Booking_id": "BK/000010",
            "venue_id": 15,
            "User_id": 10,
            "date": "2022-12-10",
            "Start_time": "09:00:00",
            "end_time": "11:00:00",
            "price" : 1000000.00
        }

        try:
            expected_price = self.booking_manager.get_expected_price(
                booking_data["venue_id"],
                booking_data["date"],
                booking_data["Start_time"],
                booking_data["end_time"]
            )
        except ValueError as e:
            self.assertEqual(str(e), "Schedule not found")
            print("Price not match: Schedule not found")
            expected_price = None

        

        # Check for duplicate bookings
        duplicate_found = self.booking_manager.check_duplicate_bookings()
        self.assertFalse(duplicate_found)

        # Insert the booking
        inserted_id = self.booking_manager.insert_booking(booking_data)
        self.assertIsNotNone(inserted_id)
        self.assertIsInstance(inserted_id, int)
        print("--------------------------------------------------------")

    
    def test_insert_booking_2(self):
        print("--------------------------------------------------------")
        booking_data = {
            "Booking_id": "BK/000020",
            "venue_id": 15,
            "User_id": 10,
            "date": "2022-12-10",
            "Start_time": "07:00:00",
            "end_time": "09:00:00",
            "price" : 800000.00
        }

        try:
            expected_price = self.booking_manager.get_expected_price(
                booking_data["venue_id"],
                booking_data["date"],
                booking_data["Start_time"],
                booking_data["end_time"]
            )
        except ValueError as e:
            self.assertEqual(str(e), "Schedule not found")
            print("Price not match: Schedule not found")
            expected_price = None


        # Check for duplicate bookings
        duplicate_found = self.booking_manager.check_duplicate_bookings()


        # Insert the booking
        inserted_id = self.booking_manager.insert_booking(booking_data)
        self.assertIsNotNone(inserted_id)
        self.assertIsInstance(inserted_id, int)
    print("--------------------------------------------------------")
    
    def test_insert_booking_3(self):
        print("--------------------------------------------------------")
        booking_data = {
            "Booking_id": "BK/000010",
            "venue_id": 15,
            "User_id": 10,
            "date": "2022-12-10",
            "Start_time": "09:00:00",
            "end_time": "11:00:00",
            "price" : 1000000.00
        }

        # Check expected price from schedule
        try:
            expected_price = self.booking_manager.get_expected_price(
                booking_data["venue_id"],
                booking_data["date"],
                booking_data["Start_time"],
                booking_data["end_time"]
            )
        except ValueError as e:
            self.assertEqual(str(e), "Schedule not found")
            print("Price not match: Schedule not found")
            expected_price = None


        # Check for duplicate bookings
        duplicate_found = self.booking_manager.check_duplicate_bookings()

        # Insert the booking
        inserted_id = self.booking_manager.insert_booking(booking_data)
        self.assertIsNotNone(inserted_id)
        self.assertIsInstance(inserted_id, int)

        print("--------------------------------------------------------")

    

if __name__ == '__main__':
    unittest.main()
