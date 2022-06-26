from models.printer import Printer


def validate_fields(mac, model, date_purchased = None, sector = None, date_maintenance = None, reason_maintenance = None):
    printer = Printer(mac, model, date_purchased, sector)
    if date_maintenance != None and reason_maintenance != None:
        printer.add_maintenance(date_maintenance, reason_maintenance)
    return printer