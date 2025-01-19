from dto.event import Event

class Concert(Event):
	def __init__(self,artist: str,type: str):
		self.artist = artist
		self.type = type

	#Getters
	def get_artist(self) -> str:
		return self.artist
	def get_type(self) -> str:
		return self.type

	#Setters
	def set_artist(self, artist: str) -> None:
		self.artist = artist
	def set_type(self, type: str) -> None:
		self.type = type
		
	def display_cocert_details(self) -> None:
		print("Artist: " + self.artist)
		print("Type: " + self.type)