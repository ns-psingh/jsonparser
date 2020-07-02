import sqlite3
from sqlite3 import Error

class DB():
    
    def __init__(self, db_name):
        #super().__init__()
        self.db_name = db_name

    def create_table_horizontal(self, conn, document):
        """
            Creates a table as per the specified columns after horizontal flattening.
        """
        columns = []
        for key in document.keys():
            columns.append(key)
        try:
            cursor = conn.cursor()
            cursor.execute("""
                    CREATE TABLE HORIZONTAL_FLAT {}
            """.format(tuple(columns)))
        except Error as e:
            print("Error encountered while creating tables for Horizontal-Flattening -> {}".format(e))
    
    def insert_data_horizontal(self, conn, document):
        """
            Inserts data into specified columns after horizontal flattening
        """ 
        data = []
        key_count = 0
        for value in document.values():
            data.append(str(value))
            key_count = key_count + 1
        
        # This segment is used to compute VALUES(?,?,?) where no. of ? = no. of columns
        l = []
        for i in range(0, key_count):
            l.append('?')
        s = ",".join(l)
        s = '(' + s + ')'

        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO HORIZONTAL_FLAT VALUES {}".format(tuple(data)))
        except Error as e:
            print("Error encountered while inserting values into table for Horizontal-Flattening -> {}".format(e))
        

    def create_connection(self):
        """
            Creates db connection to SQLite database specified by self.db  
        """
        conn = None
        try:
            conn = sqlite3.connect(self.db_name)
            return conn
        except Error as e:
            print("Error encountered while connecting to db : {}".format(e))
        return conn


