import horizontal_flattening as hf
from vertical_flatten import VerticalFlatten
import sys
import json

if __name__ == "__main__":
	flattening = str(sys.argv[1])
	file_name = str(sys.argv[2])
	with open(file_name) as f:
		document = json.load(f)
	if flattening == 'hf':
		hf = hf.HorizonalFlattening()
		hf.flatten_arrays_set_value(int(sys.argv[3]))
		if str(sys.argv[4]) == 'True':
			hf.flatten_objects_set_value(True)
		elif str(sys.argv[4] == 'False'):
			hf.flatten_objects_set_value(False)
		else:
			print('Invalid argument for flatten_objects')
		result = hf.horizontal_flat(document)
		hf.display_in_sql_table(result)
	elif flattening == 'vf':
		db_creation_name = str(sys.argv[3])
		if db_creation_name is None:
			print("Enter Data Base Name Please.")
		else:
			vf = VerticalFlatten()
			temp = vf.vertical_flatten_call(document, return_as_dict=1)
			vf.vertical_database_queries(temp, db_creation_name)
	else:
		print('Invalid argument for flattening type')
