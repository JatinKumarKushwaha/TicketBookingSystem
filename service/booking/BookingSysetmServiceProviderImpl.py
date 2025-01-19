from dto.booking import Booking
from dto.event import Event
from dto.customer import Customer
from exceptions.ExceptionHandling import  NullPointerException, InvalidBookingIDException
from service.booking.IBookingSystemServiceProvider import IBookingSystemServiceProvider
from util.dbutil import DBConnection
from datetime import date

class BookingSystemServiceProviderImpl(IBookingSystemServiceProvider):
	def __init__(self):
		self.connction = DBConnection.getDBConnection()
		self.cursor = None
			
	def book_tickets(self, event: Event, customer: Customer, num_tickets: int, total_cost: int, booking_date: date) -> int:
		try:
			self.connction = DBConnection.getDBConnection()
			self.cursor = self.connction.cursor()

			self.cursor.execute("""INSERT INTO Booking (customer_id, event_id, num_tickets, total_cost, booking_date) VALUES(?, ?, ?, ?, ?)""", (customer.get_customer_id(), event.get_event_id(), num_tickets, total_cost, booking_date))
			self.cursor.execute("SELECT LAST_INSERT_ID()") # May not be needed for databases other than MySQL
			id = self.cursor.fetchone()[0]
			self.connction.commit()

			return id

		except NullPointerException as e:
			raise NullPointerException(e)

	def cancel_booking(self, booking_id):
		try:
			self.connction = DBConnection.getDBConnection()
			self.cursor = self.connction.cursor()

			self.cursor.execute("""DELETE FROM Booking where booking_id = (?)""", (booking_id))
			self.connction.commit()

		except InvalidBookingIDException as e:
			raise InvalidBookingIDException(e)