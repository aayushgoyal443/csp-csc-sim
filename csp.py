from slice import Slice

class CSP:

    def __init__(self, id, slices, bandwidth, level, parent_csc= None):
        self.slices = slices
        self.bandwidth = bandwidth
        self.level = level
        self.id = id
        self.parent_csc = parent_csc
        self.connected_users = []
        self.total_users =0
        print("CSP created")


    def check_user(self, user):
        if self.bandwidth >= user.bandwidth:
            return True
        else:
            return False


    def add_User(self, user):
        self.connected_users.append(user)
        self.total_users += 1
        for slice in self.slices:
            if slice.is_available():
                user.slice = slice
                slice.connected_users.append(user)
                print("User added to CSP, allocated slice is:" + user.slice.name)
                return True
        print("User not allocated any slice")
        return False

    def __str__(self):
        return f"CSP ||\nid: {self.id}\nlevel: {self.level}\nbandwidth: {self.bandwidth}\nconnected_users: {self.connected_users}\nparent_csc: {self.parent_csc.id if self.parent_csc else None}\nslices: {self.slices }"