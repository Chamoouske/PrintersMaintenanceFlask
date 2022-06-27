from flask import render_template


def homepage(table_ok, printers=[]):
    return render_template('home.html', table_ok=table_ok, selected='home', printers=printers)

def create_printer(error=False, saved=False, table_ok=False):
    return render_template('create.html', table_ok=table_ok, selected='new_printer', error=error, saved=saved)

def page_about(table_ok=False):
    return render_template('about.html', table_ok=table_ok, selected='about')

def show_printer_info(printer, maintenances, table_ok=False):
    return render_template('printer.html', table_ok=table_ok, printer=printer, maintenances=maintenances)

def edit_maintenance(maintenance, table_ok=False):
    return render_template('edit_maint.html', maintenance=maintenance, table_ok=table_ok)

def page_not_exist(table_ok=False):
    return render_template('not_exist.html', table_ok=table_ok)