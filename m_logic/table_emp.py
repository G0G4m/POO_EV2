import sqlite3 as sql
from m_fn.sf.condiciones_table import condition_table as con_table

conn = sql.connect(database = r"db\db_pr.db")
c = conn.cursor()

class empleado():

    def __init__(self,nombre_empleado=None,direccion_empleado=None,numero_tel=None,direccion_correo=None,emp_departamento=None,inicio_contrato=None,salario=None,id_empleado=None):
        self.id = id_empleado
        self.nombre_empleado = nombre_empleado
        if len(nombre_empleado) <= 150:
            print("valor de nombre de empleado valido")
        else:
            raise ValueError("valor de nombre empleado supera el limite de 150 carcateres")
        self.direccion_empleado = direccion_empleado
        self.numero_tel = numero_tel
        if len(numero_tel) == 9:
            print("valor de numero telefonico valido")
        else:
            raise ValueError("valor ingresado en numero telefonico es menor o maximo al limite de 9 caracteres")
        self.direccion_correo = direccion_correo
        if len(direccion_correo) <= 320:
            print("valor de direccion de correo valido")
        else:
            raise ValueError("valor ingresado en direccion de correo supera el limite de 320 caracteres")
        self.emp_departamento = emp_departamento
        con_table("v_emp","v_t_emp",emp_departamento,"id_departamento","departamento")
        self.inicio_contrato = inicio_contrato
        if isinstance(inicio_contrato,str):
            año = inicio_contrato[:4]
            mes = inicio_contrato[4:6]
            dia = inicio_contrato[6:8]
            if int(mes) <=12:
                mes = str(mes)
                fecha_format = f"{año}-{mes}-{dia}"
            else:
                raise ValueError(f"no existe un mes numero {mes}")
            self.fecha_reg = fecha_format
            print("valor valido")
        else:
            raise ValueError("valor ingresado no valido en fecha, ingresar como YYYYMMDD")
        self.salario = salario
        if len(salario) <= 8:
            print("valor de salario ingresado valido")
        else:
            raise ValueError("valor ingresado en salario no es valido o supera el limite de 8 caracteres")
    
    def create(self):
        
        c.execute('INSERT INTO empleado (nombre_empleado,direccion_empleado,numero_tel,direccion_correo,emp_departamento,inicio_contrato,salario) VALUES (?,?,?,?,?,?,?)', (
            self.nombre_empleado,
            self.direccion_empleado,
            self.numero_tel,
            self.direccion_correo,
            self.emp_departamento,
            self.inicio_contrato,
            self.salario,
        ))
        conn.commit()
        self.id_empleado = c.lastrowid
    
    def read_all():
        c.execute('SELECT * FROM empleado')
        empleado = c.fetchall()
        conn.commit()
        return empleado
    
    def update(self):
        c.execute("UPDATE empleado SET nombre_empleado = ?,direccion_empleado = ?,numero_telefonico = ?,direccion_correo = ?,departamento = ?,inicio_contrato = ?,salario = ? WHERE id_empleado = ?",(
            self.nombre_empleado,
            self.direccion_empleado,
            self.numero_tel,
            self.direccion_correo,
            self.departamento,
            self.inicio_contrato,
            self.salario,
            self.id_empleado
        ))
        conn.commit()