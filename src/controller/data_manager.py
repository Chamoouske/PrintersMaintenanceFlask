import pandas as pd


def get_values_printer_class(printer_class):
    printer = printer_class.__dict__
    identify = printer['identify']
    model = printer['model']
    sector = printer['sector']
    date_purchased = printer['date_purchased']
    return identify, model, sector, date_purchased


def convert_tables_in_df(engine):
    printers = pd.read_sql_table('printers', engine)
    maintenances = pd.read_sql_table('maintenances', engine)
    printers['maintenances'] = maintenances['printer'].count()
    
    return printers
