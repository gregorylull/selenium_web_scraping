
import sys
import pickle

# to run
# python read_script_parameters.py some_data.pkl

print('arguments', len(sys.argv), str(sys.argv))

def hello(name):
    print('hello', name)

filename = sys.argv[1]

with open(filename, 'rb') as readfile:
    something = pickle.load(readfile)

hello(something['name'])

# creating a pickle file
# something = {
#     'test': 1,
#     'a': True,
#     'name': 'greg'
# }

# with open('some_data.pkl', 'wb') as writefile:
#     pickle.dump(something, writefile)

