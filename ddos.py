from src.slice import Slice
from src.csp import CSP 
from src.csc import CSC 

import os 
import sys
import yaml
import simpy 

# Read YAML file
CONF_FILENAME = os.path.join(os.path.dirname(__file__), sys.argv[1])
try:
    with open(CONF_FILENAME, 'r') as stream:
        data = yaml.load(stream, Loader=yaml.FullLoader)
except FileNotFoundError:
    print('File Not Found:', CONF_FILENAME)
    exit(0)


SLICES_INFO = data['slices']
BASE_STATION = data['base_stations'][0]


# Create slices
slices = []
for name, info in SLICES_INFO.items():
    slices.append(Slice(name, info['bandwidth'], info['bandwidth_guaranteed'], info['bandwidth_max']))


BASE_LEVEL =1
csp_a = CSP(BASE_STATION['name'] ,slices, BASE_STATION['bandwidth'], BASE_LEVEL)


# Create CSCs
csc_a = CSC("IIT Delhi")
csp_a.add_User(csc_a)
csc_a.init_provider()


csp_b = csc_a.child_provider

names  = ["RANDOM DPT", "RANDOM DPT", "RANDOM DPT", "CSE DPT", "EE DPT", "MATHS DPT"]
NUM_CHILD = len(names)
csc_bs = []
for i in range(NUM_CHILD):
    csc_b = CSC(names[i])  
    csp_b.add_User(csc_b)
    print(csc_b)
    csc_bs.append(csc_b)

# for csc_b in csc_bs:
# 	csc_b.start_consume()


print()
# check prints
print(slices)
print(csp_a)
print(csc_a)
print(csp_b)    