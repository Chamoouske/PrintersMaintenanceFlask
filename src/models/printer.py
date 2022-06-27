class Printer:
    def __init__(self, identify, model, purchased='', sector='', count_maintenances=0) -> None:
        self.identify = identify
        self.model = model
        self.sector = sector
        self.maintenances = []
        self.count_maintenances = count_maintenances
        self.date_purchased = purchased
        pass

    def add_maintenance(self, date_maintenance, reason):
        self.maintenances.append([date_maintenance, reason])
    
    def edit_attr(self, attr, new_value):
        self[attr] = new_value
