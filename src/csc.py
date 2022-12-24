from .csp import CSP
from .slice import Slice


class CSC:

    def __init__(self, id):
        self.slice = None
        self.id = id
        self.child_provider = None 
        self.level = None
        self.parent_csp = None 
        print(f"CSC created: {self.id}")


    def make_slice(self, num_child):
        for i in range(num_child):
            slice_i = Slice(f"{self.slice.name}_{i}", self.slice.bandwidth/(num_child+1), self.slice.bandwidth_guaranteed/(num_child+1), self.slice.bandwidth_max/(num_child+1))    # +1 because needs to themselves as well
            self.slice.children.append(slice_i)


    def init_provider(self, num_child=10):
        # assuming that we are making slices inside the main function 
        self.make_slice(num_child)
        self.child_provider = CSP(self.id+ "_provd", self.slice.children, self.slice.bandwidth, self.level, self)
        
    
    # make str fucntion to print all the attributes of the class new line separated
    def __str__(self):
        return f"CSC ||\nid: {self.id}\nlevel: {self.level}\nchild_provider: {self.child_provider.id if self.child_provider else None }\nslice: {self.slice.name}"