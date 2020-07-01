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

class TestVerticalFlatten(unittest.TestCase):

    def setUp(self):
        self.vf = vf.VerticalFlatten()

    def test_vertical_flatten_schema(self):
        document = copy.deepcopy(sample_document)
        initial_key = 1
        assert self.vf.get_vertical_flatten_schema(document, initial_key) == {
                                                                        1: ['_id',
                                                                            'address.building',
                                                                            'address.coord.csv',
                                                                            'address.street',
                                                                            'address.zipcode',
                                                                            'borough',
                                                                            'cuisine',
                                                                            'name',
                                                                            'restaurant_id'],
                                                                        2: ['date', 'grade', 'score']
                                                                        }
