from slice import Slice
from csp import CSP 
from csc import CSC 

import os 
import sys
import yaml

# Read YAML file
CONF_FILENAME = os.path.join(os.path.dirname(__file__), sys.argv[1])
try:
    with open(CONF_FILENAME, 'r') as stream:
        data = yaml.load(stream, Loader=yaml.FullLoader)
except FileNotFoundError:
    print('File Not Found:', CONF_FILENAME)
    exit(0)


SLICES_INFO = data['slices']
BASE_STATIONS = data['base_stations'][0]


# Create slices
slices = []
for name, info in SLICES_INFO.items():
    slices.append(Slice(name, info['bandwidth']))


provider = CSP(slices, BASE_STATIONS['bandwidth'], 0)


# Create CSCs
csc = CSC()

provider.add_User(csc)


# check prints
print(slices)
print(provider)
print(csc)