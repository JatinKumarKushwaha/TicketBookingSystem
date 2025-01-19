import pyodbc

class DBConnection:

	@staticmethod
	def getDBConnection():
		try:
			server = ''
			port = ''
			database = ''
			user = ''
			password = ''

			connection_string = (
			"DRIVER={MySQL ODBC 8.0 Unicode Driver};"
			f"SERVER={server};"
			f"PORT={port};"
			f"DATABASE={database};"
			f"UID={user};"
			f"PWD={password};"
			"OPTION=3;"
			)

			conn = pyodbc.connect(connection_string)
			return conn

		except Exception as e:
			print(f"Connection failed: {e}")