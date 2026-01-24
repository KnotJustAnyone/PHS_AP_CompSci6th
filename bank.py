class Bank:
    def __init__(self, *elevators):
        self.elevators = elevators
print(Bank(1,2,3,4,9).elevators)