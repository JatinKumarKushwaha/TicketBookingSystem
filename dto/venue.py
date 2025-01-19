class Venue:
	def __init__(self, venue_id, venue_name: str, venue_address: str):
		self.venue_id = venue_id
		self.venue_name = venue_name
		self.venue_address = venue_address

	#Getters
	def get_venue_id(self) -> str:
		return self.venue_id
	def get_venue_name(self) -> str:
		return self.venue_name
	def get_venue_address(self) -> str:
		return self.venue_address

	#Setters
	def set_venue_name(self, venue_id: str) -> None:
		self.venue_id = venue_id
	def set_venue_name(self, venue_name: str) -> None:
		self.venue_name = venue_name
	def set_venue_address(self, venue_address: str) -> None:
		self.venue_address = venue_address

	def display_venue_details(self) -> None:
		print("Venue name: " + self.venue_name)
		print("Venue address: " + self.venue_address)