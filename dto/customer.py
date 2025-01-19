class Customer:
	def __init__(self,customer_id: str, name: str, email: str, phone_number: str):
		self.customer_id = customer_id
		self.name = name
		self.email = email
		self.phone_number = phone_number

	#Getters
	def get_customer_id(self) -> str:
		return self.customer_id
	def get_name(self) -> str:
		return self.name
	def get_email(self) -> str:
		return self.email
	def get_phone_number(self) -> str:
		return self.phone_number

	#Setters
	def set_customer_id(self,customer_id: str) -> None:
		self.customer_id = customer_id
	def set_name(self,name: str) -> None:
		self.name = name
	def set_email(self,email: str) -> None:
		self.email = email
	def set_phone_number(self,phone_number: str) -> None:
		self.phone_number = phone_number
