import sqlalchemy
import pandas


def create_engine() -> sqlalchemy.engine_from_config:
    engine = sqlalchemy.create_engine('sqlite:///src\\static\\db\\database.db')
    return engine

def create_tables_db() -> bool:
    engine = create_engine()
    try:
        engine.execute("""
                   CREATE TABLE IF NOT EXISTS printers (
                       identify TEXT PRIMARY KEY NOT NULL,
                       model TEXT NOT NULL,
                       sector TEXT,
                       date_purchased TEXT
                   )
                   
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
    engine = create_engine()
    try:
        engine.execute("""
                       SELECT * FROM printers
                       """)
        return True
    except:
        return False
