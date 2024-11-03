from base_method import base_meth
import sqlite3 as sql

conn = sql.connect(database = "db\db_pr.db")
c = conn.cursor()

class departamento(base_meth):

    def __init__(self,nombre_departamento,gerente_asociado,id_departamento = None):
        self.id = id_departamento
        self.nombre_departamento = nombre_departamento
        self.gerente_asociado = gerente_asociado

    def create():
        pass
    
    def read_all():
        pass
    
    def update():
        pass
    
    def delete():
        pass