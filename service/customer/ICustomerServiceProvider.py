from abc import ABC, abstractmethod
from dto.customer import Customer

class ICustomerServiceProvider(ABC):
	@abstractmethod
	def display_customer_details():
		pass

	@abstractmethod
	def createCustomer(self, name: str, email: str, phone_number: int) -> int:
		pass

	@abstractmethod
	def getCustomer(self, id: int) -> Customer:
		pass