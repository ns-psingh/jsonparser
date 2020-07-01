"""
    Module to handle Vertical Flattening
"""

class VerticalFlatten():

    def __init__(self):
        list_of_all_schemas = []

    def dict_as_value(self, name, dict_as_value):
        list_to_return = []
        for key, value in dict_as_value.items():
            if isinstance(value, dict):
                pass
            elif isinstance(value, list):
                bool_val = self.validate_for_another_schema(value)
                if bool_val:
                    self.get_vertical_flatten_schema(value[0])
                else:
                    list_to_return.append(name+"."+key+".csv")
            else:
                list_to_return.append(name+"."+key)
        return list_to_return

    def get_vertical_flatten_schema(self, json_as_dict, initial_key):
        '''
            This function will take json as dict and flatten it vertically
            If the value is of type string, int, float, or anything other then list, treat it as
            column of schema.
            Returns a dict with key specifying table/schema number and corresponding value is list
            of columns/attributes for that schema.
        '''
        schema_list = []
        dict_of_schemas = {}
        for key, value in json_as_dict.items():
            if isinstance(value, dict):
                temp_val = self.dict_as_value(key, value)
                for x in temp_val:
                    schema_list.append(x)
            elif isinstance(value, list):
                bool_val = self.validate_for_another_schema(value)
                if bool_val:
                    new_schema_dict = self.get_vertical_flatten_schema(value[0], initial_key+1)
                    dict_of_schemas.update(new_schema_dict)
                else:
                    '''
                        Raise exception
                    '''
                    pass
            else:
                schema_list.append(key)
            dict_of_schemas[initial_key] = schema_list

        return dict_of_schemas

    def validate_for_another_schema(self, list_to_verify):
        '''
            This function will check if the list validate for new table, if all are of type dict
        '''
        for i in list_to_verify:
            if isinstance(i, dict) == False:
                return False
        return True
        

        

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
 "score" : 5
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

# vf = VerticalFalten()
#print(vf.get_vertical_flatten_schema(sample_document, 1))

# [{"Quality_Food": 4, "Safety": 4, "Quantity_Food": 5}, {"Quality_Food": 4, "Safety": 4, "Quantity_Food": 5}]
# [{"a": 3, "b": 2, "c": 1, "d":[{"k": 2, "e": 2, "f": 1}, {"k": 2, "e": 2, "f": 1}]}, {"a": 2, "b": 2, "c": 1, "d":[]}, {"a": 5, "b": 2, "c": 1, "d":[]}, {"a": 8, "b": 2, "c": 1, "d":[]}]
