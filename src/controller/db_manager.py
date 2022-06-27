import sqlalchemy
from sqlalchemy import MetaData, Table, Column, String, Integer

from controller.data_manager import *


engine = None
def create_engine() -> None:
    global engine
    engine = sqlalchemy.create_engine('sqlite:///src\\static\\db\\database.db', echo=True)
    pass

meta = MetaData()
printers = Table(
            'printers', meta,
            Column('identify', String, primary_key=True),
            Column('model', String),
            Column('sector', String),
            Column('date_purchased', String),
            Column('count_maintenances', Integer)
        )
maintenances = Table(
            'maintenances', meta,
            Column('printer', String),
            Column('date_maintenance', String),
            Column('reason', String)
        )

def create_tables_db() -> bool:
    global engine
    if engine == None:
        create_engine()
    try:
        meta.create_all(engine)
        return True
    except:
        return False


def save_printer(printer) -> bool:
    global engine
    if engine == None:
        create_engine()
    try:
        global printers
        stmt = printers.insert().values(identify=printer.identify,
                                        model=printer.model,
                                        sector=printer.sector,
                                        date_purchased=printer.date_purchased,
                                        count_maintenances=0)
        with engine.connect() as conn:
            conn.execute(stmt)
        if printer.count_maintenances > 0:
            return save_maintenances(printer.maintenances, printer.identify)
        return True
    except:
        return False


def save_maintenances(printer_maintenances, identify) -> bool:
    global engine
    if engine == None:
        create_engine()
    try:
        global maintenances
        for maintenance in printer_maintenances:
            stmt = maintenances.insert().values(
                                            printer=identify,
                                            date_maintenance=maintenance[0],
                                            reason=maintenance[1]
                                            )
            with engine.connect() as conn:
                conn.execute(stmt)
        return update_count_maint(identify=identify, operation='add')
    except:
        return False
    
    
def delete_maintenance(maintenance):
    global engine
    if engine == None:
        create_engine()
    try:
        global maintenances
        s = maintenances.delete().where(maintenances.c.printer==maintenance[0],
                                        maintenances.c.date_maintenance==maintenance[1],
                                        maintenances.c.reason==maintenance[2])
        with engine.connect() as conn:
            conn.execute(s)
        return update_count_maint(maintenance[0], 'sub')
    except:
        return False
    
    
def update_maintenances(maintenance, identify):
    global engine
    if engine == None:
        create_engine()
    try:
        global maintenances
        s = maintenances.update().where(
                maintenances.c.printer==identify[0]).where(
                    maintenances.c.date_maintenance==identify[1]).where(
                        maintenances.c.reason==identify[2]).values(
                                                printer=maintenance[0],
                                                date_maintenance=maintenance[1],
                                                reason=maintenance[2])
        with engine.connect() as conn:
            conn.execute(s)
        return True
    except:
        return False
    

def update_count_maint(identify, operation='add'):
    global engine
    if engine == None:
        create_engine()
    try:
        printer = get_printers(identify)
        for row in printer:
            if operation == 'add':
                new_value = row[4] + 1
            else:
                new_value = row[4] - 1
        s = printers.update().where(printers.c.identify == identify).values(count_maintenances = new_value)
        with engine.connect() as conn:
            conn.execute(s)
        return True
    except:
        return False


def verify_db():
    global engine
    if engine == None:
        create_engine()
    try:
        with engine.connect as conn:
            conn.execute('SELECT * FROM printers')
        return True
    except:
        return False


def get_printers(printer=''):
    if printer != '':
        s = printers.select().where(printers.c.identify == printer)
    else:
        s = printers.select()
    with engine.connect() as conn:
        result = conn.execute(s)
        for row in result:
            yield row


def get_maintenances(printer):
    s = maintenances.select().where(maintenances.c.printer == printer)
    global engine
    with engine.connect() as conn:
        result = conn.execute(s)
        for row in result:
            yield row


def verify_printer(printer):
    result = get_printers(printer)
    for row in result:
        if row[0] == printer:
            return row
    return False
