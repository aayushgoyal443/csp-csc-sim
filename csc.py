class CSC:

    def __init__(self):
        self.slice = None
        print("CSC created")


    def __str__(self):
        return f"CSC || slice: {self.slice.name if self.slice else None}"