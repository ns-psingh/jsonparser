"""
Module for handling horizontal flatenning
"""

class HorizonalFlattening():
    
    def _init_(self):
        self.flatten_objects = False
        pass

    def horizontal_flat(self, document):
        """
        This method will perform horizontal flatenning for a document
        """
        for field in list(document.keys()):
            if isinstance(document[field], dict):
                flatenned_results = self.restructure(field, document[field])
                del document[field]
                for result in list(flatenned_results.keys()):
                    document[result] = flatenned_results[result]

    def restructure(self, field_name, document):
        """
        This function will take the embedded document and return a dict
        """
        result = {}
        for key in list(document.keys()):
            result[field_name+"."+key] = document[key]
        return result

    def display_in_sql_table(self):
        """
        This function will make create a SQL
        based table using a relational SQL server
        and insert all records
        """