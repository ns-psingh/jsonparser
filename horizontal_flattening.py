"""
Module for handling horizontal flatenning
"""

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
                    del document[field][0]
                for result in list(flatenned_results.keys()):
                    document[result] = flatenned_results[result] 
        return document

    def restructure_flatten_object(self, field_name, document):
        """
        This function will take the embedded document and return a dict to flatten arrays
        """
        result = {}
        for key in list(document.keys()):
            if isinstance(document[key], dict):
                document = self.horizontal_flat(document)
                key = list(document.keys())[0]            
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

    def display_in_sql_table(self):
        """
        This function will make create a SQL
        based table using a relational SQL server
        and insert all records
        """