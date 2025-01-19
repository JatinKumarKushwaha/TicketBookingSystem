from dto.customer import Customer
from service.customer.ICustomerServiceProvider import ICustomerServiceProvider
from util.dbutil import DBConnection
from exceptions.ExceptionHandling import NullPointerException

class CustomerServiceProviderImpl(ICustomerServiceProvider):
	def __init__(self) -> None:
		self.connection = None
		self.cursor = None

	def display_customer_details():
		pass

	def createCustomer(self, name: str, email: str, phone_number: int) -> int:
		try:
			self.connection = DBConnection.getDBConnection()
			self.cursor = self.connection.cursor()
			self.cursor.execute("""INSERT INTO Customer (customer_name, email, phone) VALUES(?, ?, ?)""", (name, email, phone_number))
			self.cursor.execute("SELECT LAST_INSERT_ID()") # May not be needed for databases other than MySQL
			id = self.cursor.fetchone()[0]
			self.connection.commit()
			
			return id
		except NullPointerException as e:
			raise NullPointerException(e)
	
	def getCustomer(self, id: int) -> Customer:
		try:
			self.coonection = DBConnection.getDBConnection()
			self.cursor = self.coonection.cursor()
			self.cursor.execute("""SELECT * FROM Customer WHERE customer_id = ?""", (id))
			row = self.cursor.fetchone()
			customer = Customer(row[0], row[1], row[2], row[3])

			return customer
		except NullPointerException as e:
			raise NullPointerException(e)