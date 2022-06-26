import sqlalchemy
import pandas

engine = None
def create_engine() -> None:
    global engine
    engine = sqlalchemy.create_engine('sqlite:///src\\static\\db\\database.db')
    pass

def create_tables_db() -> bool:
    global engine
    if engine == None:
        create_engine()
    try:
        engine.execute("""
                   CREATE TABLE IF NOT EXISTS printers (
                       identify TEXT PRIMARY KEY NOT NULL,
                       model TEXT NOT NULL,
                       sector TEXT,
                       date_purchased TEXT
                   )
                   """)
        engine.execute("""
                   CREATE TABLE IF NOT EXISTS maintenances (
                       printer TEXT,
                       date_maintenance TEXT NOT NULL,
                       reason TEXT NOT NULL
                   )
                   """)
        return True
    except Exception:
        return False


def verify_tables() -> bool:
    global engine
    if engine == None:
        create_engine()
    try:
        engine.execute("""
                       SELECT * FROM printers
                       """)
        return True
    except:
        return False
