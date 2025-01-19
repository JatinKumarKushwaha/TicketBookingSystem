from typing import List
from abc import ABC, abstractmethod
from datetime import date

from dto.customer import Customer
from dto.event import Event

class Booking(ABC):
	def __init__(self, booking_id: int, customer: Customer, event: Event, num_tickets: int, total_cost: int, booking_date: date):
		self.booking_id = booking_id
		self.customer =  customer
		self.event = event
		self.num_tickets = num_tickets
		self.total_cost = total_cost
		self.booking_date = booking_date

	#Getters
	def booking_id(self) -> int:
		return self.booking_id
	def get_customer(self) -> Customer:
		return self.customer
	def get_event(self) -> Event:
		return self.event
	def get_num_tickets(self) -> int:
		return self.num_tickets
	def get_total_cost(self) -> int:
		return self.total_cost
	def get_booking_date(self) -> date:
		return self.booking_date


	#Setters
	def booking_id(self, booking_id: int) -> None:
		self.booking_id = booking_id
	def get_customer(self, customer: Customer) -> None:
		self.booking_id = customer
	def get_event(self, event: Event) -> None:
		self.booking_id = event
	def get_num_tickets(self, num_tickets: int) -> None:
		self.booking_id = num_tickets
	def get_total_cost(self, total_cost: int) -> None:
		self.booking_id = total_cost
	def get_booking_date(self, booking_dates: int) -> None:
		self.booking_id = booking_dates