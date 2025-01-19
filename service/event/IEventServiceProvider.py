from abc import ABC, abstractmethod
from dto.venue import Venue
from dto.event import Event, EventType

class IEventServiceProvider(ABC):
	@abstractmethod
	def calculate_total_revenue():
		# return (total_seats - avaliable_seats) * ticket_price
		pass

	@abstractmethod
	def create_event(self, event_name: str, date: str, time: str, total_seats: int, ticket_price: float, event_type: EventType, venue: Venue) -> Event:
		pass

	@abstractmethod
	def getEventDetails(self) -> list:
		pass

	@abstractmethod
	def getAvailableNoOfTickets(self) -> int:
		# return avaliable number of seats
		pass

	@abstractmethod
	def get_booked_num_of_tickets():
		# return (total_seats - avaliable_seats)
		pass
	
	@abstractmethod
	def getEvent(self, id: int) -> Event:
		pass