
# to run
# python read_script_parameters.py some_data.pkl

import sys
import pickle

# Displays arguments you typed in from the command line
print('arguments', len(sys.argv), str(sys.argv))
filename = sys.argv[1]

# creating a pickle file
data = {
    'test': 1,
    'a': True,
    'name': 'world'
}

with open(filename, 'wb') as writefile:
    pickle.dump(data, writefile)


# reading that same pickle file
with open(filename, 'rb') as readfile:
    data_loaded = pickle.load(readfile)

def hello(name):
    print('hello', name)

hello(data_loaded['name'])
