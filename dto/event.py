from abc import ABC, abstractmethod
from datetime import date
from datetime import time
from enum import Enum
from dto.venue import Venue

class EventType(Enum):
	Movie = "Movie"
	Concert = "Concert"
	Sport = "Sport"

class Event(ABC):
	def __init__(self, event_id: int, event_name: str, event_date: date, event_time: time, venue: Venue, total_seats: int, avaliable_seats: int, ticket_price: float, event_type: EventType):
		self.event_id = event_id
		self.event_name = event_name
		self.event_date = event_date
		self.event_time = event_time
		self.venue = venue
		self.total_seats = total_seats
		self.avaliable_seats = avaliable_seats
		self.ticket_price = ticket_price
		self.event_type = event_type

	#Getters
	def get_event_id(self) -> int:
		return self.event_id
	def get_event_name(self) -> str:
		return self.event_name
	def get_event_date(self) -> date:
		return self.event_date
	def get_event_time(self) -> time:
		return self.event_time
	def get_venue(self) -> Venue:
		return self.venue
	def get_total_seats(self) -> int:
		return self.total_seats
	def get_avaliable_seats(self) -> int:
		return self.avaliable_seats
	def get_ticket_price(self) -> float:
		return self.ticket_price
	def get_event_type(self) -> EventType:
		return self.event_type

	#Setters
	def set_event_name(self, event_id: int):
		self.event_id = event_id
	def set_event_name(self, event_name: str):
		self.event_name = event_name
	def set_event_date(self, event_date: date):
		self.event_date = event_date
	def set_event_time(self, event_time: time):
		self.event_time = event_time
	def set_venue(self, venue: Venue):
		self.venue = venue
	def set_total_seats(self, total_seats: int):
		self.total_seats = total_seats
	def set_avaliable_seats(self, avaliable_seats: int):
		self.avaliable_seats = avaliable_seats
	def set_ticket_price(self, ticket_price: float):
		self.ticket_price = ticket_price
	def set_event_type(self, event_type: EventType):
		self.event_type = event_type