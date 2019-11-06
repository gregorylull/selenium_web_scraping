
import sys
import pickle

print('arguments', len(sys.argv), str(sys.argv))

def hello(name):
    print('hello', name)

filename = sys.argv[1]

with open(filename, 'rb') as readfile:
    files = pickle.load(readfile)

hello(files)

something = {
    'test': 1,
    'a': True,
    'name': 'greg'
}

# creating a pickle file
# with open('some_data.pkl', 'wb') as writefile:
#     pickle.dump(something, writefile)

