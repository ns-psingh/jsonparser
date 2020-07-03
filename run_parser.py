import horizontal_flattening as hf
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
            print('Implementation pending')
            #will be done in seperate PR
        else:
            print('Invalid argument for flattening type')          