import sqlite3

def create_table():
    conn = sqlite3.connect(r"db\db_pr.db")
    c = conn.cursor()
    
    #Se crea la tabla departamento si no existe
    c.execute("""CREATE TABLE IF NOT EXISTS departamento(
              id_departamento INTEGER PRIMARY KEY AUTOINCREMENT,
              nombre_departamento TEXT,
              gerente_asociado INTEGER,
              FOREIGN KEY (gerente_asociado) REFERENCES empleado (id_empleado)
              )""")
    
    #Se crea la tabla empleado si no existe
    c.execute("""CREATE TABLE IF NOT EXISTS empleado(
              id_empleado INTEGER PRIMARY KEY AUTOINCREMENT,
              nombre_empleado TEXT,
              direccion_empleado TEXT,
              numero_tel TEXT,
              direccion_correo TEXT,
              emp_departamento INTEGER,
              inicio_contrato TEXT,
              salario INTEGER,
              FOREIGN KEY (emp_departamento) REFERENCES departamento (id_departamento)
              )""")
    
    #Se crea la tabla proyecto si no existe a su vez descrip = descripcion
    c.execute("""CREATE TABLE IF NOT EXISTS proyecto(
              id_empleado INTEGER PRIMARY KEY AUTOINCREMENT,
              nombre_proyecto TEXT,
              descrip_proyecto TEXT,
              fecha_inicio TEXT
              )""")
    
    #Se crea la tabla reg_tiempo si no existe
    c.execute("""CREATE TABLE IF NOT EXISTS reg_tiempo(
              id_registro INTEGER PRIMARY KEY AUTOINCREMENT,
              empleado_reg INTEGER,
              proyecto_reg INTEGER,
              fecha_reg TEXT,
              cantidad_horas INTEGER,
              trabajo_realizado TEXT,
              FOREIGN KEY (empleado_reg) REFERENCES empleado (id_empleado),
              FOREIGN KEY (proyecto_reg) REFERENCES proyecto (id_proyecto)
              )""")
    
    #Se crea si no existe emp_prj, emp = empleado y prj = proyecto
    c.execute("""CREATE TABLE IF NOT EXISTS emp_prj(
              empleado_id INTEGER,
              proyecto_id INTEGER,
              PRIMARY KEY (empleado_id, proyecto_id),
              FOREIGN KEY (empleado_id) REFERENCES empleado (id_empleado),
              FOREIGN KEY (proyecto_id) REFERENCES proyecto (id_proyecto)
              )""")
    
    #Se crea si no existe la tabla user
    c.execute("""CREATE TABLE IF NOT EXISTS user(
              id_user INTEGER PRIMARY KEY AUTOINCREMENT,
              name_user TEXT,
              key_user TEXT
              )""")
    
    conn.commit()