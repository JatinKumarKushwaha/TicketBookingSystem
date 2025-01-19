from dto.event import Event

class Movie(Event):
	def __init__(self, genre: str, actor_name: str, actress_name: str):
		self.genre = genre
		self.actor_name = actor_name
		self.actress_name = actress_name

	#Getters
	def get_genre(self) -> str:
		return self.genre
	def get_actor_name(self) -> str:
		return self.actor_name
	def get_actress_name(self) -> str:
		return self.actress_name

	#Setters
	def set_genre(self, genre: str) -> None:
		self.genre = genre
	def set_actor_name(self, actor_name: str) -> None:
		self.actor_name = actor_name
	def set_actress_name(self, actress_name: str) -> None:
		self.actress_name = actress_name

	def display_sports_details(self) -> None:
		print("Genre: " + self.genre)
		print("Actor name: " + self.actor_name)
		print("Actress name: " + self.actress_name)