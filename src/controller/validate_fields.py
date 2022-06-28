from src.controller.db_manager import save_printer
from src.models.printer import Printer


def validate_fields(model, date_purchased = '', sector = '', dates_maint=[], reasons_maint=[]) -> bool:
    try:
        printer = Printer(model, date_purchased, sector, len(dates_maint))
        for i in range(len(dates_maint)):
            printer.add_maintenance(dates_maint[i],reasons_maint[i])
        return save_printer(printer)
    except:
        return False