from dto.movie import Movie
from dto.sport import Sport
from dto.concert import Concert
from dto.event import Event, EventType
from dto.venue import Venue
from util.dbutil import DBConnection
from exceptions.ExceptionHandling import *
from service.event.IEventServiceProvider import IEventServiceProvider

class EventServiceProviderImpl(IEventServiceProvider):
	def __init__(self):
		self.coonection = None
		self.cursor = None

	def create_event(self, event_name: str, date: str, time: str, total_seats: int, ticket_price: float, event_type: EventType, venue: Venue) -> Event:
		
		# Create an event based on the type
		if not (event_type.value.lower() == 'movie' or event_type.value.lower() == "movies" or event_type.value.lower() == 'concert' or event_type.value.lower() == "concerts" or event_type.value.lower() == 'sport' or event_type.value.lower() == "sports"):
			raise ValueError("Invalid event type. Must be 'Movie', 'Concert', or 'Sport'.")

		try:
			self.coonection = DBConnection.getDBConnection()

			self.cursor = self.coonection.cursor()
			self.cursor.execute("""INSERT INTO Event (event_name, event_date, event_time, venue_id, total_seats, available_seats, ticket_price, event_type) Values(?, ?, ?, ?, ?, ?, ?, ?)""", (event_name, date, time, venue.get_venue_id(), total_seats, total_seats, ticket_price, event_type.value))
			self.coonection.commit()
			
		except NullPointerException as e:
			raise NullPointerException(e)

	def getEventDetails(self) -> list:
		"""Return an array of event details."""
		try:
			self.coonection = DBConnection.getDBConnection()
			self.cursor = self.coonection.cursor()
			self.cursor.execute("SELECT * FROM Event")

			for e in self.cursor.fetchall():
				print(e)

		except NullPointerException as e:
			raise NullPointerException(e)
		

	def getAvailableNoOfTickets(self) -> int:
		"""Return the total available tickets for all events."""
		# TODO: return no of seats
		total_available_tickets = 0
		try:
			self.coonection = DBConnection.getDBConnection()
			self.cursor = self.coonection.cursor()
			self.cursor.execute("SELECT event_name, available_seats FROM Event")
			for e in self.cursor.fetchall():
				print(e)
				total_available_tickets += e[1]

		except NullPointerException as e:
			raise NullPointerException(e)

		return total_available_tickets
	
	def get_booked_num_of_tickets():
		# return (total_seats - available_seats)
		print("wow you did something")
	
	def calculate_total_revenue():
		# return ticket * pirce for the event
		print("something")

	def getEvent(self, id: int) -> Event:
		try:
			self.coonection = DBConnection.getDBConnection()
			self.cursor = self.coonection.cursor()
			self.cursor.execute("""SELECT * FROM Event WHERE event_id = ?""", (id))
			row = self.cursor.fetchone()
			event = Event(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])

			return event
		except NullPointerException as e:
			raise NullPointerException(e)