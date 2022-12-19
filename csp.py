from slice import Slice

class CSP:

    def __init__(self, slices, bandwidth, level, parent_csc= None):
        self.slices = slices
        self.bandwidth = bandwidth
        self.level = level
        self.parent_csc = parent_csc
        self.connected_users = []
        self.total_users =0
        self.unused_slices = slices.copy()
        print("CSP created")

    def add_User(self, user):
        self.connected_users.append(user)
        self.total_users += 1
        user.slice = self.unused_slices.pop(0)
        user.slice.connected_users.append(user)
        print("User added to CSP, allocated slice is:" + user.slice.name)  
        # how much part of the slice needs to be given
        return True 


    def __str__(self):
        return f"CSP|| level: {self.level} bandwidth: {self.bandwidth} connected_users: {self.connected_users} unused_slices: {self.unused_slices} total_users: {self.total_users} slices: {self.slices}"