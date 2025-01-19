from abc import ABC, abstractmethod
from dto.customer import Customer

class IBookingSystemServiceProvider(ABC):
	@abstractmethod
	def book_tickets(self, event_name: str, num_tickets: int, customers: list[Customer]) -> int:
		pass

	@abstractmethod
	def cancel_booking(self, booking_id: int):
		pass
