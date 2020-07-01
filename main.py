import pprint
from test_horizontal_flattening import TestCovid

if __name__ == "__main__":
	test_case = TestCovid()
	test_case.setUp()
	
	result = test_case.test_horizontal_flat()
	pprint.pprint(result, indent=4)

