# Add the parent directory to sys.path
import sys
import os
from datetime import datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dto.event import EventType
from exceptions.ExceptionHandling import EventNotFoundException, NullPointerException, InvalidBookingIDException
from service.event.EventServiceProviderImpl import EventServiceProviderImpl
from service.booking.BookingSysetmServiceProviderImpl import BookingSystemServiceProviderImpl
from service.veune.VenueServiceProviderImpl import VenueServiceProviderImpl
from service.customer.CustomerServiceProviderImpl import CustomerServiceProviderImpl

class TicketBookingSystem:
	def __init__(self):
		self.event_service = EventServiceProviderImpl()
		self.customer_service = CustomerServiceProviderImpl()
		self.booking_service = BookingSystemServiceProviderImpl()
		self.venue_service = VenueServiceProviderImpl()

	def create_event(self):
		event_name = str(input("Enter event name: "))
		event_date = str(input("Enter event date (YYYY-MM-DD): "))
		event_time = str(input("Enter event time (HH:MM:SS): "))
		total_seats = int(input("Enter total seats: "))
		ticket_price = float(input("Enter ticket price: "))
		event_type = str(input("Enter event type (Movie/Sports/Concert): "))
		self.venue_service.getAllVenue()
		venue_id = int(input("Enter venue id from the listed venues: "))

		#TODO: perform a venue id check

		if event_type.lower() == "movie" or event_type.lower() == "movies":
			event_type = EventType.Movie
		elif event_type.lower() == "concert" or event_type.lower() == "concerts":
			event_type = EventType.Concert
		elif event_type.lower() == "sport" or event_type.lower() == "sports":
			event_type = EventType.Sport
		else:
			print("Entered event is invalid. Please enter a valid event type.")
			return

		# TODO get the venue info with the venue id
		venue = self.venue_service.getVenue(venue_id)

		self.event_service.create_event(event_name, event_date, event_time, total_seats, ticket_price, event_type, venue)

	def book_tickets(self):
		while True:
			print("Select type of seat (Silver/Gold/Diamond):")
			ticket_type = str(input())
			price_multiplier = 1
			if (ticket_type.lower() == "silver"):
				price_multiplier = 1
			elif ticket_type.lower() == "gold":
				price_multiplier = 2
			elif ticket_type.lower() == "diamond":
				price_multiplier = 3
			else:
				print("Entered ticket type is invalid. Please enter a valid ticket type.")
				continue
			break
		
		self.event_service.getEventDetails()
		# Perform event id check
		try:
			event_id = int(input("Enter event id: "))
		except EventNotFoundException as e:
			raise EventNotFoundException(e)

		event = self.event_service.getEvent(event_id)
		num_tickets = int(input("Enter number of tickets: "))

		try:
			customer_name = input("Enter your name: ")
			email = input("Enter your email: ")
			phone = int(input("Enter your phone: "))

			customer = self.customer_service.getCustomer(self.customer_service.createCustomer(customer_name, email, phone))
			
			booking_id = self.booking_service.book_tickets(event, customer, num_tickets, num_tickets * event.get_ticket_price() * price_multiplier, datetime.today())
			print("Ticket(s) booked")
			print(f"Your booking id is: {booking_id}")
		except NullPointerException as e:
			raise NullPointerException(e)

	def cancel_booking(self):
		booking_id = int(input("Enter booking ID: "))

		try:
			self.booking_service.cancel_booking(booking_id)
		except InvalidBookingIDException as e:
			raise InvalidBookingIDException(e)

	def run(self):
		while True:
			print("1. Create Event")
			print("2. Book Tickets")
			print("3. Cancel Tickets") # --> Booking
			print("4. Get Event Details")
			print("5. Get Available Seats")
			print("6. Exit")

			choice = int(input("Enter your choice: "))

			if choice == 1:
				self.create_event()
			elif choice == 2:
				self.book_tickets()
			elif choice == 3:
				self.cancel_booking()
			elif choice == 4:
				self.event_service.getEventDetails()
			elif choice == 5:
				available_seats = self.event_service.getAvailableNoOfTickets()
				print(f"Available seats: {available_seats}")
			elif choice == 6:
				break
			else:
				print("Invalid choice! Please try again.")