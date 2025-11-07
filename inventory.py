class Inventory:
    def __init__(self, initial=None):
        self.content = {}

        if initial:
            for item, quantity in initial.items():
                self.content[item] = int(quantity)

    def add(self, item, quantity):
        self.content[item] = int(quantity)

    def __repr__(self):
        return str(self.content)
