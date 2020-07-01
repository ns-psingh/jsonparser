import copy
import unittest
import vertical_flatten as vf

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

class TestVerticalFlatten(unittest.TestCase):

    def setUp(self):
        self.vf = vf.VerticalFlatten()

    def test_vertical_flatten_schema_as_dict(self):
        document = copy.deepcopy(sample_document)
        return_as_dict = 1
        assert self.vf.vertical_flatten_call(document, return_as_dict) == {
                                                                            1: ['k', 'e', 'f'],
                                                                            2: ['a', 'b', 'c'],
                                                                            3: ['date', 'grade'],
                                                                            4: ['_id',
                                                                                'address.building',
                                                                                'address.coord.csv',
                                                                                'address.street',
                                                                                'address.zipcode',
                                                                                'borough',
                                                                                'cuisine',
                                                                                'name',
                                                                                'restaurant_id']
                                                                        }
    def test_vertical_flatten_schema_as_list(self):
        document = copy.deepcopy(sample_document)
        return_as_dict = 0
        assert self.vf.vertical_flatten_call(document, return_as_dict) == [
                                                                            ['k', 'e', 'f'],
                                                                            ['a', 'b', 'c'],
                                                                            ['date', 'grade'],
                                                                            ['_id',
                                                                            'address.building',
                                                                            'address.coord.csv',
                                                                            'address.street',
                                                                            'address.zipcode',
                                                                            'borough',
                                                                            'cuisine',
                                                                            'name',
                                                                            'restaurant_id']
                                                                        ]
                                                                        