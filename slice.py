class Slice:

    def __init__(self, name, bandwidth):
        self.name = name
        self.bandwidth = bandwidth
        self.connected_users = []
        print("Slice created")

    def __str__(self):
        return f"slice || name: {self.name} bandwidth: {self.bandwidth} connected_users: {self.connected_users}"
    