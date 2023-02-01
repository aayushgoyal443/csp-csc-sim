from .slice import Slice
import random

class CSP:

    def __init__(self, id, slices, bandwidth, level, parent_csc= None):
        self.slices = slices
        self.bandwidth = bandwidth
        self.level = level
        self.id = id
        self.parent_csc = parent_csc
        self.connected_users = []
        self.total_users =0
        print(f"CSP created: {self.id}")


    def check_user(self, user):
        if user not in self.connected_users:
            print(f"{user.id} has been validated by {self.id}")
            if self.parent_csc is None:
                print("Validation complete")
                return True
            else:
                print(f"Forwarding to {self.parent_csc.parent_csp.id}")
                return self.parent_csc.parent_csp.check_user(user)
        else:
            print(f"{user.id} already connected in the network")
            return False


    def add_User(self, user):
        if self.check_user(user):
            self.connected_users.append(user)
            self.total_users += 1
            l = len(self.slices)
            # make an array with numbers from 0 to l-1 and then shuffle the array
            num = [i for i in range(l)]
            random.shuffle(num)
            for i in num:
                slice = self.slices[i]
                if slice.is_available():
                    user.slice = slice
                    user.usage_remaining = slice.bandwidth_guaranteed
                    user.parent_csp = self
                    user.level = self.level+1
                    slice.connected_users.append(user)
                    print(f"{user.id} added to CSP ({self.id}), allocated slice is:" + user.slice.name)
                    return True
            print(f"{user.id} not allocated any slice")
            return False
        else:
            return False

    def __str__(self):
        return f"CSP ||\nid: {self.id}\nlevel: {self.level}\nbandwidth: {self.bandwidth}\nconnected_users: {self.connected_users}\nparent_csc: {self.parent_csc.id if self.parent_csc else None}\nslices: {self.slices }\n\n"