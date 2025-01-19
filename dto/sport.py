from dto.event import Event

class Sport(Event):
	def __init__(self,sports_name: str,team_name: str):
		self.sports_name = sports_name
		self.team_name = team_name

	#Getters
	def get_sports_name(self) -> str:
		return self.sports_name
	def get_team_name(self) -> str:
		return self.team_name

	#Setters
	def set_sports_name(self, sports_name: str) -> None:
		self.sports_name = sports_name
	def set_team_name(self, team_name: str) -> None:
		self.team_name = team_name
		
	def display_sports_details(self) -> None:
		print("Sports name: " + self.sports_name)
		print("Team name: " + self.team_name)