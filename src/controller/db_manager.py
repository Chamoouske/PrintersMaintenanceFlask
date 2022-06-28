import sqlalchemy
from sqlalchemy import MetaData, Sequence, Table, Column, String, Integer, desc


engine = None
def create_engine() -> None:
    global engine
    engine = sqlalchemy.create_engine('sqlite:///src\\static\\db\\database.db', echo=True)
    pass

meta = MetaData()
printers = Table(
            'printers', meta,
            Column('id', Integer, Sequence('user_id_seq'), primary_key=True),
            Column('model', String),
            Column('sector', String),
            Column('date_purchased', String),
            Column('count_maintenances', Integer)
        )
maintenances = Table(
            'maintenances', meta,
            Column('id', Integer, Sequence('user_id_seq'), primary_key=True),
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
        stmt = printers.insert().values(model=printer.model,
                                        sector=printer.sector,
                                        date_purchased=printer.date_purchased,
                                        count_maintenances=0)
        with engine.connect() as conn:
            conn.execute(stmt)
        if printer.count_maintenances > 0:
            id_printer = get_id_last_printer_add()
            return save_maintenances(printer.maintenances, id_printer)
        return True
    except:
        return False
    
    
def get_id_last_printer_add():
    global engine
    if engine == None:
        create_engine()
    try:
        global printers
        s = printers.select().order_by(desc(printers.c.id))
        with engine.connect() as conn:
            result = conn.execute(s)
            for row in result:
                return row[0]
    except:
        return False
    

def update_printer(printer):
    global engine
    if engine == None:
        create_engine()
    try:
        global printers
        u = printers.update().where(printers.c.id==printer[0]).values(model=printer[1],sector=printer[2],date_purchased=printer[3])
        with engine.connect() as conn:
            conn.execute(u)
        return True
    except:
        return False
    
    
def delete_printer_db(id):
    global engine
    if engine == None:
        create_engine()
    try:
        global printers
        d = printers.delete().where(printers.c.id==id)
        with engine.connect() as conn:
            conn.execute(d)
        return delete_all_maintenance(id)
    except:
        return False
    

def delete_all_maintenance(id):
    global engine
    if engine == None:
        create_engine()
    try:
        global maintenances
        s = maintenances.delete().where(maintenances.c.printer==id)
        with engine.connect() as conn:
            conn.execute(s)
        return True
    except:
        return False


def save_maintenances(printer_maintenances, id) -> bool:
    global engine
    if engine == None:
        create_engine()
    try:
        global maintenances
        for maintenance in printer_maintenances:
            stmt = maintenances.insert().values(
                                            printer=id,
                                            date_maintenance=maintenance[0],
                                            reason=maintenance[1]
                                            )
            with engine.connect() as conn:
                conn.execute(stmt)
            update_count_maint(id=id, operation='add')
        return True
    except:
        return False
    
    
def delete_maintenance(id_maint, id_printer):
    global engine
    if engine == None:
        create_engine()
    try:
        global maintenances
        s = maintenances.delete().where(maintenances.c.id==id_maint)
        with engine.connect() as conn:
            conn.execute(s)
        return update_count_maint(id_printer, 'sub')
    except:
        return False
    
    
def update_maintenances(maintenance):
    global engine
    if engine == None:
        create_engine()
    try:
        global maintenances
        s = maintenances.update().where(
                maintenances.c.id==maintenance[0]).values(
                                                date_maintenance=maintenance[1],
                                                reason=maintenance[2])
        with engine.connect() as conn:
            conn.execute(s)
        return True
    except:
        return False
    

def update_count_maint(id, operation='add'):
    global engine
    if engine == None:
        create_engine()
    try:
        printer = get_printers(id)
        for row in printer:
            if operation == 'add':
                new_value = row[4] + 1
            else:
                new_value = row[4] - 1
        s = printers.update().where(printers.c.id == id).values(count_maintenances = new_value)
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
        s = printers.select().where(printers.c.id == printer)
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
