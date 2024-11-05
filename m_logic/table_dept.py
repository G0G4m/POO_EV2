from base_method import base_meth
import sqlite3 as sql

conn = sql.connect(database = r"db\db_pr.db")
c = conn.cursor()

class departamento(base_meth):

    def __init__(self,nombre_departamento = None,gerente_asociado = None,id_departamento = None,empleado_asociado = None):
        self.id = id_departamento
        self.nombre_departamento = nombre_departamento
        if len(nombre_departamento) <= 100:
            print("valor ingresado al nombre de departamento valido")
        else:
            raise ValueError("valor ingresado a nombre de departamento supera el maximo de 100 caracteres")
        self.gerente_asociado = gerente_asociado
        c.execute("SELECT nombre_empleado FROM empleado")
        v_gerente = [row[0] for row in c.fetchall()]
        if gerente_asociado in v_gerente:
            print("el valor ingresado en gerente asignado es valido")
        else:
            raise ValueError("valor ingresado en gerente asignado no se encuentra registrado")
        self.empleado_asociado = empleado_asociado
        c.execute("SELECT nombre_empleado FROM empleado")
        v_emp = [row[0] for row in c.fetchall()]
        if empleado_asociado in v_emp:
            print("el valor ingresado en empleado asignado es valido")
        else:
            raise ValueError("valor ingresado en empleado asignado no se encuentra registrado")
        
    def create(self):
        c.execute('INSERT INTO departamento(nombre_departamento,gerente_asociado,empleado_asociado) VALUES (?,?,?)',(
            self.nombre_departamento,
            self.gerente_asociado,
            self.empleado_asociado
            ))
        conn.commit()
        self.id_departamento = c.lastrowid
    
    def read_all():
        c.execute('SELECT * FROM departamento')
        departamento = c.fetchall()
        conn.commit()
        return departamento
    
    def update(self):
        c.execute('UPDATE departamento SET nombre_departamento = ?, gerente_asociado = ?, empleado_asociado = ? WHERE id_departamento = ?',(
            self.nombre_departamento,
            self.gerente_asociado,
            self.empleado_asociado,
            self.id_departamento
        ))
        conn.commit()
    
    def delete(self):
        c.execute('DELETE FROM departamento WHERE id_departamento = ?',(
            self.id_departamento,
        ))
        conn.commit()