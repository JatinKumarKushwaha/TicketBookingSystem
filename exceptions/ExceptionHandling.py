class EventNotFoundException(Exception):
	def __init__(self, message="The event you are trying for it's avaliable. Please select form the listed events."):
		self.message = message
		super().__init__(self.message)

class InvalidBookingIDException(Exception):
	def __init__(self, message="Invalid booking ID. Please enter a valid booking ID."):
		self.message = message
		super().__init__(self.message)

class NullPointerException(Exception):
	def __init__(self, message):
		self.message = str("A catastrophic error has occured: ") + str(message)
		super().__init__(self.message)