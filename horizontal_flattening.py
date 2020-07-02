"""
Module for handling horizontal flatenning
"""
import pprint
from database import DB
class HorizonalFlattening():
    
    def __init__(self):
        self.flatten_objects = False
        self.flatten_arrays = 0

    def flatten_objects_set_value(self, value):
        self.flatten_objects = value
    
    def flatten_objects_get_value(self):
        return self.flatten_objects

    def flatten_arrays_set_value(self, value):
        self.flatten_arrays = value

    def flatten_arrays_get_value(self):
        return self.flatten_arrays

    def horizontal_flat(self, document):
        """
        This method will perform horizontal flatenning for a document
        """
        for field in list(document.keys()):
            if isinstance(document[field], dict) and self.flatten_objects_get_value():
                flatenned_results = self.restructure_flatten_object(field, document[field])
                del document[field]
                for result in list(flatenned_results.keys()):
                    document[result] = flatenned_results[result]
            elif isinstance(document[field], list) and self.flatten_arrays_get_value() > 0: #bug_7
                flatenned_results = self.restructure_flatten_array(field, document[field], self.flatten_arrays_get_value())
                for _ in range(0, self.flatten_arrays_get_value()):
                    del document[field][_]
                for result in list(flatenned_results.keys()):
                    document[result] = flatenned_results[result] 
        return document

    def restructure_flatten_object(self, field_name, document):
        """
        This function will take the embedded document and return a dict to flatten arrays
        """
        result = {}
        for key in list(document.keys()):
            result[field_name+"."+key] = document[key]
        return result
    
    def restructure_flatten_array(self, field_name, document, num):
        """
        This function will take the embedded document and return a dict to flatten objects
        """
        result = {}
        for _ in range(0,num):
            result[field_name+"."+str(_)] = document[_]
        return result

    def display_in_sql_table(self, document):
        """
        This function will make create a SQL
        based table using a relational SQL server
        and insert all records
        """
        db = DB("horizontal_database.db")
        conn = db.create_connection()
        if conn is not None:
            db.create_table_horizontal(conn, document)
            db.insert_data_horizontal(conn, document)
        else:
            print("Error while creating database connection")

sample_document = {
 "_id" : "5780046cd5a397806c3dab38",
 "address" : {
 "building" : "1007",
 "coord" : [-73.856077, 40.848447],
 "street" : "Morris Park Ave",
 "zipcode" : "10462"
 },
 "borough" : "Bronx",
 "cuisine" : "Bakery",
 "grades" : [
 {
 "date" : "2014-03-03T00:00:00Z",
 "grade" : "A",
 "score" : 2
 }, {
 "date" : "2013-09-11T00:00:00Z",
 "grade" : "A",
 "score" : 6
 }, {
 "date" : "2013-01-24T00:00:00Z",
 "grade" : "A",
 "score" : 10
 }, {
 "date" : "2011-11-23T00:00:00Z",
 "grade" : "A",
 "score" : 9
 }, {
 "date" : "2011-03-10T00:00:00Z",
 "grade" : "B",
 "score" : 14
 }
 ],
 "name" : "Morris Park Bake Shop",
 "restaurant_id" : "30075445"
}

hf = HorizonalFlattening()
hf.flatten_arrays_set_value(2)
hf.flatten_objects_set_value(False)

result = hf.horizontal_flat(sample_document)
pprint.pprint(result)
hf.display_in_sql_table(result)