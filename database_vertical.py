import sqlite3

class VerticalFlattenDataBase():
	
	def __init__(self, database_name):
		self.database_name = database_name

	def create_vertical_tables(self, db, command_to_create):
		try:
			conn = db.create_connection()
			cursor = conn.cursor()
			cursor.execute(command_to_create)
			conn.commit()
			conn.close()
			print("Creation Successful")
			return True
		except Exception as e:
			print("Error", e)
			return False

	def insert_vertical_data(self, db, command_to_insert, tuple_of_values):
		try:
			conn = db.create_connection()
			cursor = conn.cursor()
			cursor.execute(command_to_insert, tuple_of_values)
			conn.commit()
			conn.close()
			print("Insertion Successful")
			return True
		except Exception as e:
			print("Error", e)
			return False

	def query_vertical_data(self, db, command_to_query):
		try:
			conn = db.create_connection()
			cursor = conn.cursor()
			cursor.execute(command_to_query)
			rows = cursor.fetchall()
			for row in rows:
				print(row)
			conn.commit()
			conn.close()
			print("Query Successful")
			return True
		except Exception as e:
			print("Error", e)
			return False

	def create_connection(self):
		'''
			Creates a DB Connection
		'''
		conn = None
		try:
			conn = sqlite3.connect(self.database_name)
			return conn
		except sqlite3.Error as e:
			print("Error: ", e)
