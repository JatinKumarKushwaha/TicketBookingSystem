from abc import ABC, abstractmethod
from dto.venue import Venue

class IVenueServiceProvider(ABC):
	@abstractmethod
	def getVenue(id: int) -> Venue:
		pass

	@abstractmethod
	def getAllVenue(self) -> None:
		pass
