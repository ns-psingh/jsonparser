from General_Exceptions import VerticalFlattenException

class VerticalFlatten():

    def __init__(self):
        pass

    def dict_as_value(self, name, dict_as_value):
        list_to_return = []
        for key, value in dict_as_value.items():
            if isinstance(value, dict):
                # We can do a recursive call, not implementing for now.
                pass
            elif isinstance(value, list):
                bool_val = self.validate_for_another_schema(value)
                if bool_val:
                    list_of_schema = self.vertical_flatten_call(value[0])
                    for j in list_of_schema:
                        if(isinstance(j, list)):
                            list_to_return.append(j)
                elif self.validate_for_comma_seprated_value(value):
                    csv_value = ""
                    for i in value:
                        csv_value = csv_value+str(i)
                        csv_value = csv_value+","
                    temp_dict = {}
                    temp_dict[name+"."+key+".csv"] = csv_value
                    list_to_return.append(temp_dict)
                else:
                    raise VerticalFlattenException("All Elements are Not of Type Str Int, May include List and Dict.") 
            else:
                temp_dict = {}
                temp_dict[name+"."+key] = value
                list_to_return.append(temp_dict)
        return list_to_return

    def vertical_flatten_call(self, json_as_dict, return_as_dict=None):
        '''
            This function will take json as dict and flatten it vertically
            If the value is of type string, int, float, or anything other then list, treat it as
            column of schema.
        '''
        overall_list = []
        schema_list = []
        for key, value in json_as_dict.items():
            if isinstance(value, dict):
                temp_val = self.dict_as_value(key, value)
                for x in temp_val:
                    if isinstance(x, list):
                            overall_list.append(x)
                            continue
                    schema_list.append(x)
            elif isinstance(value, list):
                bool_val = self.validate_for_another_schema(value)
                if bool_val:
                    list_of_nested_lists = self.vertical_flatten_call(value[0])
                    for i in list_of_nested_lists:
                        overall_list.append(i)
                else:
                    '''
                        Raise exception
                    '''
                    raise VerticalFlattenException("All Elements are Not of Type Dict.")
            else:
                temp_dict = {}
                temp_dict[key] = value
                schema_list.append(temp_dict)
        overall_list.append(schema_list)
        if return_as_dict == 1:
            count_var = 1
            final_dict = {}
            for i in overall_list:
                final_dict[count_var] = i
                count_var = count_var+1
            return final_dict
        return overall_list

    def validate_for_another_schema(self, list_to_verify):
        '''
            This function will check if the list validate for new table, if all are of type dict
        '''
        for i in list_to_verify:
            if isinstance(i, dict) == False:
                return False
        return True

    def validate_for_comma_seprated_value(self, list_to_verify):
        for i in list_to_verify:
            if isinstance(i, dict):
                return False
            if isinstance(i, list):
                return False
        return True

        

sample_document = {
 "_id" : "5780046cd5a397806c3dab38",
 "address" : {
 "building" : "1007",
 "coord" : [-73.856077, 40.848447],
 "Parth" : [{"a1": 2, "c1": 34, "b1": [{"e1": 22, "f1":[{"g1": 23}]}, {"ee1": 32}]}, 
            {"a1": 21, "b1": 31}],
 "Abcde" : [{"a1": 2, "c1": 34, "b1": {'la': 'li', 'ga': 'gi', 'ra': [{'pii': 'pa', 'po':'pu', 'test': {"ggs": "okay", "last_level": [{"parth": 10}]}}]}}, 
            {"a1": 21, "b1": 31}],
 "street" : "Morris Park Ave",
 "zipcode" : "10462"
 },
 "borough" : "Bronx",
 "cuisine" : "Bakery",
 "grades" : [
 {
 "date" : "2014-03-03T00:00:00Z",
 "grade" : "A",
 "score" : [{"a": 3, "b": 2, "c": 1, "d":[{"k": 2, "e": 2, "f": 1}, {"k": 2, "e": 2, "f": 1}]}, {"a": 2, "b": 2, "c": 1, "d":[]}, {"a": 5, "b": 2, "c": 1, "d":[]}, {"a": 8, "b": 2, "c": 1, "d":[]}]
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


# vf = VerticalFlatten()
# temp = vf.vertical_flatten_call(sample_document, return_as_dict=1)
# for i, j in temp.items():
#     print(i, j)

# [{"Quality_Food": 4, "Safety": 4, "Quantity_Food": 5}, {"Quality_Food": 4, "Safety": 4, "Quantity_Food": 5}]
# [{"a": 3, "b": 2, "c": 1, "d":[{"k": 2, "e": 2, "f": 1}, {"k": 2, "e": 2, "f": 1}]}, {"a": 2, "b": 2, "c": 1, "d":[]}, {"a": 5, "b": 2, "c": 1, "d":[]}, {"a": 8, "b": 2, "c": 1, "d":[]}]
