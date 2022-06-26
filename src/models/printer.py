class Printer:
    def __init__(self, mac, model, purchased, sector) -> None:
        self.mac = mac
        self.model = model
        self.sector = sector
        self.maintenance = []
        self.purchased = purchased
        pass

    def add_maintenance(self, date_maintenance, reason):
        self.maintenance.append({"data": date_maintenance, 'motivo': reason})
        return self.maintenance[-1]
    
    def edit_attr(self, attr, new_value):
        self[attr] = new_value
        return self[attr]
