class Bill:
    def __init__(self):
        self.room = 0
        self.food = 0
        self.laundry = 0

    def total(self):
        return self.room + self.food + self.laundry
