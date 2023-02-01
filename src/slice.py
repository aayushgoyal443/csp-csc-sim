class Slice:

    def __init__(self, name, bandwidth, bandwidth_guaranteed, bandwidth_max):
        self.name = name
        self.bandwidth = bandwidth
        self.bandwidth_guaranteed = bandwidth_guaranteed
        self.bandwidth_max = bandwidth_max
        self.children = []
        self.connected_users = []
        self.connected_active_users = []
        print(f"Slice created: {self.name}")

    def is_available(self):
        if(self.connected_active_users == []):
            bandwidth_next = self.bandwidth_max
        else:
            bandwidth_next = self.bandwidth_max/ (len(self.connected_active_users)+1)
        if bandwidth_next < self.bandwidth_guaranteed:
            return False
        return True

    def get_consumable_share(self):
        if(len(self.connected_active_users)) == 0:
            return self.bandwidth
        else:
            return self.bandwidth//len(self.connected_active_users)

    # make str fucntion to print all the attributes of the class new line separated
    def __str__(self):
        return f"Slice ||\nname: {self.name}\nbandwidth: {self.bandwidth}\nbandwidth_guaranteed: {self.bandwidth_guaranteed}\nbandwidth_max: {self.bandwidth_max}\nchildren: {self.children}\nconnected_users: {self.connected_users} \nconnected_active_users: {self.connected_active_users}\n\n"