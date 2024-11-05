from base_method import base_meth
import sqlite3 as sql

conn = sql.connect(database = r"db\db_pr.db")
c = conn.cursor()

class proyecto(base_meth):

    def __init__(self,nombre_proyecto,descripcion_proyecto,fecha_inicio,id_proyecto = None):
        self.id = id_proyecto
        self.nombre_proyecto = nombre_proyecto
        self.descripcion_proyecto = descripcion_proyecto
        self.fecha_inicio = fecha_inicio

    def create():
        pass
    
    def read_all():
        pass
    
    def update():
        pass
    
    def delete():
        pass