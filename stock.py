class Stock:
    def __init__(self, stock_id, name):
        self.stock_id = stock_id
        self.name = name
        self.entries = []

    def add_entry(self, entry):
        if entry not in self.entries:
            self.entries.append(entry)

    def remove_entry(self, entry):
        if entry in self.entries:
            self.entries.remove(entry)

    def get_total_quantity(self):
        return sum(entry.quantity for entry in self.entries)
