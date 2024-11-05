import m_logic.table_emp as mp
import sqlite3 as sql
from m_fn.sf.condiciones_table import condition_table as con_table

conn = sql.connect(database = r"db\db_pr.db")
c = conn.cursor()

class reg_tiempo(mp.empleado):
    def __init__(self,empleado_reg = None, proyecto_reg = None, fecha_reg = None, cantidad_horas = None, trabajo_realizado = None,id_registro = None):
        super().__init__(id_empleado=empleado_reg)
        self._empleado_reg = empleado_reg
        list_id_emp = c.execute("SELECT id_empleado FROM empleado")
        v_emp = [row[0] for row in list_id_emp.fetchall()]
        if int(empleado_reg) in v_emp:
            print("el valor ingresado en id empleado es valido")
        else:
            raise ValueError("valor ingresado en id empleado no es valido")
        self.proyecto_reg = proyecto_reg
        if isinstance(empleado_reg,int):
            print("valor de poryecto valido")
        else:
            raise ValueError("valor ingresado en proyecto no valido")
        self.fecha_reg = fecha_reg
        if isinstance(fecha_reg,str):
            año = fecha_reg[:4]
            mes = fecha_reg[4:6]
            dia = fecha_reg[6:8]
            fecha_format = f"{año}-{mes}-{dia}"
            self.fecha_reg = fecha_format
            print("valor de fecha valido")
        else:
            raise ValueError("valor ingresado no valido en fecha, ingresar como YYYYMMDD")
        self.cantidad_horas = cantidad_horas
        if isinstance(cantidad_horas,int):
            print("valor de cantidad de horas valido")
        else:
            raise ValueError("Valor ingresado en cantidad de horas no valido")
        self.trabajo_realizado = trabajo_realizado
        if len(trabajo_realizado) <= 500:
            print("valor valido")
        else:
            raise ValueError("valor ingresado en trabajo realizado no valido")

    def create(self):
        c.execute('INSERT INTO reg_tiempo (empleado_reg, proyecto_reg, fecha_reg, cantidad_horas, trabajo_realizado) VALUES (?,?,?,?,?)',(
            self.id_empleado,
            self.proyecto_reg,
            self.fecha_reg,
            self.cantidad_horas,
            self.trabajo_realizado,
        ))
        conn.commit()
        self.id_registro = c.lastrowid

    def read_all():
        c.execute('SELECT * FROM reg_tiempo')
        reg_tiempo = c.fetchall()
        conn.commit()
        return reg_tiempo