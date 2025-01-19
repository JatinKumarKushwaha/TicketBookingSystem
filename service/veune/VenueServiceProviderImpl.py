from dto.venue import Venue
from service.veune.IVenueServiceProvider import IVenueServiceProvider
from util.dbutil import DBConnection
from exceptions.ExceptionHandling import NullPointerException

class VenueServiceProviderImpl(IVenueServiceProvider):
	def __init__(self):
		self.coonection = None
		self.cursor = None

	def getVenue(self, id: int) -> Venue:
		try:
			self.coonection = DBConnection.getDBConnection()
			self.cursor = self.coonection.cursor()
			self.cursor.execute("""SELECT * FROM Venue WHERE venue_id = ?""", (id))
			row = self.cursor.fetchone()
			venue = Venue(row[0], row[1], row[2])

			return venue
		except NullPointerException as e:
			raise NullPointerException(e)

	def getAllVenue(self) -> None:
		self.coonection = DBConnection.getDBConnection()
		self.cursor = self.coonection.cursor()
		self.cursor.execute("SELECT * from Venue")
		
		for e in self.cursor.fetchall():
			print(e)