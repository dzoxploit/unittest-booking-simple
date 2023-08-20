import mysql.connector
class Schedule:
    def __init__(self, venue_id, date, start_time, end_time, price):
        self.venue_id = venue_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.price = price

class DatabaseConnector:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="bookingtest"
        )
        self.cursor = self.connection.cursor()

    def get_connection(self):
        # Establish a database connection using the parameters
        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="bookingtest"
        )
        return connection
    
    def fetch_bookings(self):
        query = "SELECT * FROM bookings"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def fetch_schedules(self):
        query = "SELECT * FROM schedules"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        # Convert rows into Schedule objects
        schedules = []
        for row in rows:
            schedule = Schedule(
                venue_id=row[1],  # venue_id
                date=row[2],  # date
                start_time=row[3],  # start_time
                end_time=row[4],  # end_time
                price=row[5],  # price
            )
            schedules.append(schedule)

        return schedules
    def create_bookings_table(self):
        create_table_query = """
        CREATE TABLE bookings (
            id INT AUTO_INCREMENT PRIMARY KEY,
            Booking_id VARCHAR(20),
            venue_id INT,
            User_id INT,
            date DATE,
            Start_time TIME,
            end_time TIME,
            price DECIMAL(10, 2)
        )
        """
        self.cursor.execute(create_table_query)
        self.connection.commit()
    
    def create_schedule_table(self):
        create_table_query = """
            CREATE TABLE schedules (
                id INT AUTO_INCREMENT PRIMARY KEY,
                venue_id INT,
                date DATE,
                start_time TIME,
                end_time TIME,
                price DECIMAL(10, 2)
            )
            """
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def insert_schedule(self, venue_id, date, start_time, end_time, price):
        insert_query = """
        INSERT INTO schedules (venue_id, date, start_time, end_time, price)
        VALUES (%s, %s, %s, %s, %s)
        """
        data = (venue_id, date, start_time, end_time, price)

        try:
            self.cursor.execute(insert_query, data)
            self.connection.commit()
            print("Schedule inserted successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
    
    def close_connection(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Database connection closed.")

db_connector = DatabaseConnector()
# db_connector.create_bookings_table()
# db_connector.create_schedule_table()
# db_connector.insert_schedule(15, '2022-12-10', '07:00:00', '09:00:00', 800000)
# db_connector.insert_schedule(15, '2022-12-10', '09:00:00', '11:00:00', 1000000)
# db_connector.insert_schedule(15, '2022-12-10', '11:00:00', '13:00:00', 1200000)
# db_connector.close_connection()