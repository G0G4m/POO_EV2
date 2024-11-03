import m_logic.base_method as bm
import sqlite3 as sql


conn = sql.connect(database = "db\db_pr.db")
c = conn.cursor()

class empleado(bm.base_meth):

    def __init__(self,nombre_empleado=None,direccion_empleado=None,numero_tel=None,direccion_correo=None,departamento=None,inicio_contrato=None,salario=None,id_empleado=None):
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
        self.departamento = departamento
        c.execute("SELECT nombre_departamento FROM departamento")
        v_dept = [row[0] for row in c.fetchall()]
        if departamento in v_dept:
            print("el valor ingresado en departamento es valido")
        else:
            raise ValueError("valor ingresado en departamento no se encuentra registrado")
        self.inicio_contrato = inicio_contrato
        if isinstance(inicio_contrato,str):
            año = inicio_contrato[:4]
            mes = inicio_contrato[4:6]
            dia = inicio_contrato[6:8]
            fecha_format = f"{año}-{mes}-{dia}"
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
        c.execute('INSERT INTO empleado (nombre_empleado,direccion_empleado,numero_telefonico,direccion_correo,departamento,inicio_contrato,salario) VALUES (?,?,?,?,?,?)', (
            self.nombre_empleado,
            self.direccion_empleado,
            self.numero_tel,
            self.direccion_correo,
            self.departamento,
            self.inicio_contrato,
            self.salario,
        ))
        conn.commit()
        self.id_registro = c.lastrowid
    
    def read_all():
        c.execute('SELECT * FROM empleado',)
        return c.fetchall()
    
#var1 = empleado("Ezequiel","pasaje lenga 6119","990989668","xxx@gmail.com","Recursos humanos","20002020","600000",)
#var1.create