import sqlite3 as sql

conn = sql.connect(database = r"db\db_pr.db")
c = conn.cursor()

def condition_table(name_func,name_tupla,var_table,con_1,table):
    name_func = c.execute(f"SELECT {con_1} FROM {table}")
    name_tupla = [row[0] for row in name_func.fetchall()]
    if int(var_table) in name_tupla:
        print(f"el valor ingresado en {con_1} es valido")
    else:
        raise ValueError(f"valor ingresado en {con_1} no es valido")