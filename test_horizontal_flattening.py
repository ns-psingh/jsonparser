import horizontal_flattening as hf
import unittest

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
class TestCovid(unittest.TestCase):
    """ Class to test HorizontalFlatenning class """

    def setUp(self):
        self.hf = hf.HorizonalFlattening()

    def test_horizontal_flat_simple(self):
        assert self.hf.horizontal_flat(sample_document) == sample_document
    
    def test_horizontal_flatten_object(self):
        self.hf.flatten_arrays_set_value(2)
        self.hf.flatten_objects_set_value(False)
        assert self.hf.horizontal_flat(sample_document) == {'_id': '5780046cd5a397806c3dab38',
                                                            'address': {'building': '1007', 
                                                                        'coord': [-73.856077, 40.848447], 
                                                                        'street': 'Morris Park Ave', 
                                                                        'zipcode': '10462'}, 
                                                            'borough': 'Bronx', 
                                                            'cuisine': 'Bakery', 
                                                            'grades': [{'date': '2013-09-11T00:00:00Z', 'grade': 'A', 'score': 6}, 
                                                                       {'date': '2011-11-23T00:00:00Z', 'grade': 'A', 'score': 9}, 
                                                                       {'date': '2011-03-10T00:00:00Z', 'grade': 'B', 'score': 14}], 
                                                            'name': 'Morris Park Bake Shop', 
                                                            'restaurant_id': '30075445', 
                                                            'grades.0': {'date': '2014-03-03T00:00:00Z', 'grade': 'A', 'score': 2}, 
                                                            'grades.1': {'date': '2013-09-11T00:00:00Z', 'grade': 'A', 'score': 6}}


    