from m_logic import table_emp as te
import m_logic.exit_terminal as xt
import tkinter as tk
from tkinter import ttk
from m_fn.sf.treeview import treeview as tv
from m_fn.sf.placeholder import placeholder
import sqlite3 as sql

conn = sql.connect(database = r"db\db_pr.db")
c = conn.cursor()

class tab_empleado(tk.Frame):
    def __init__(self,master):
        super().__init__(master)

        subtab = ttk.Notebook(self)
        subtab.pack(expand = True, fill = "both")

        tab1 = tk.Frame(subtab)
        tab2 = tk.Frame(subtab)

        subtab.add(tab1, text= "Agregar")
        subtab.add(tab2, text= "Editar")

        label = tk.Label(tab1, text="AGREGAR EMPLEADO", font= 16).place(x=160,y=10)
        label2 = tk.Label(tab1, text="VISTA DE EMPLEADO", font= 16).place(x=159,y=210)

        tittle_empleado = tk.Label(tab1,text="Nombre").place(x=50,y=60)
        text_empleado = tk.Entry(tab1,width=55,)
        text_empleado.place(x=170,y=60)
        placeholder(text_empleado,"Nombre del empleado")
        
        tittle_direccion = tk.Label(tab1,text="Direccion").place(x=50,y=80)
        text_direccion = tk.Entry(tab1,width=55)
        text_direccion.place(x=170,y=80)
        placeholder(text_direccion,"Direccion del empleado")

        tittle_tel_num = tk.Label(tab1,text="Numero telefonico").place(x=50,y=100)
        text_tel_num = tk.Entry(tab1,width=55)
        text_tel_num.place(x=170,y=100)
        placeholder(text_tel_num,"los ultimos 9 numeros del numero telefonico")

        tittle_correo = tk.Label(tab1,text="Correo").place(x=50,y=120)
        text_correo = tk.Entry(tab1,width=55)
        text_correo.place(x=170,y=120)
        placeholder(text_correo,"Direccion de correo electronico")

        tittle_departamento = tk.Label(tab1,text="Departamento").place(x=50,y=140)
        text_departamento = tk.Entry(tab1,width=55)
        text_departamento.place(x=170,y=140)
        placeholder(text_departamento,"ID del departamento perteneciente")

        tittle_contrato = tk.Label(tab1,text="Inicio contrato").place(x=50,y=160)
        text_contrato = tk.Entry(tab1,width=55)
        text_contrato.place(x=170,y=160)
        placeholder(text_contrato,"formato del inicio de contrato es YYYYMMDD")

        tittle_salario = tk.Label(tab1,text="Salario").place(x=50,y=180)
        text_salario = tk.Entry(tab1,width=55)
        text_salario.place(x=170,y=180)
        placeholder(text_salario,"salario sin punto separador")

        def agregar_datos_empleado():

            v1 = text_empleado.get()
            v2 = text_direccion.get()
            v3 = text_tel_num.get()
            v4 = text_correo.get()
            v5 = text_departamento.get()
            v6 = text_contrato.get()
            v7 = text_salario.get()

            if not len(v1) <= 150:
                print("valor no valido en nombre")
                text_empleado.delete(0,tk.END)
                return
            
            if not isinstance(v2,str):
                print("valor no valido direccion")
                text_direccion.delete(0,tk.END)
                return

            if not len(v3) == 9:
                print("el numero telefonico no es valido o supera el limite de 9 caracteres")
                text_tel_num.delete(0,tk.END)
                return
            
            if not len(v4) <= 320:
                print("el correo electronico no es valido o supera los 320 caracteres limite")
                text_correo.delete(0,tk.END)
                return
            
            list_dept = c.execute("SELECT id_departamento FROM departamento")
            v_dept = [row[0] for row in list_dept.fetchall()]
            if not int(v5) in v_dept:
                print("el valor exede los caracteres maximos")
                text_departamento.delete(0,tk.END)
                return
            
            if not len(v6) == 8:
                print("el valor supera o no tiene el minimo de 8 caracteres")
                text_contrato.delete(0,tk.END)
                return
            
            if not len(v7) <= 8:
                print("el valaro del salario supera el limite maximo de caracteres")
                text_salario.delete(0,tk.END)
                return

            v5 = int(v5)

            datos = te.empleado(v1,v2,v3,v4,v5,v6,v7)
            datos.create()
            print("Creacion de registro exitoso")

            text_empleado.delete(0,tk.END)
            text_direccion.delete(0,tk.END)
            text_tel_num.delete(0,tk.END)
            text_correo.delete(0,tk.END)
            text_departamento.delete(0,tk.END)
            text_contrato.delete(0,tk.END)
            text_salario.delete(0,tk.END)

            tv(tree,te.empleado.read_all())

        boton_save = tk.Button(tab1, text="Guardar", command=agregar_datos_empleado)
        boton_save.place(x=10,y=10)

        tree = ttk.Treeview(tab1, columns=("ID", "Nombre", "Direccion", "Telefono", "Correo", "Departamento", "Inicio contrato", "Salario"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Nombre", text="Nombre")
        tree.heading("Direccion", text="Direccion")
        tree.heading("Telefono", text="Telefono")
        tree.heading("Correo", text="Correo")
        tree.heading("Departamento", text="Departamento")
        tree.heading("Inicio contrato", text="Inicio contrato")
        tree.heading("Salario", text="Salario")

        tree.place(x=12,y=260)

        tree.column("ID",width=25,anchor=tk.CENTER)
        tree.column("Nombre",width=60,anchor=tk.CENTER)
        tree.column("Direccion",width=60,anchor=tk.CENTER)
        tree.column("Telefono",width=60,anchor=tk.CENTER)
        tree.column("Correo",width=70,anchor=tk.CENTER)
        tree.column("Departamento",width=90,anchor=tk.CENTER)
        tree.column("Inicio contrato",width=90,anchor=tk.CENTER)
        tree.column("Salario",width=60,anchor=tk.CENTER)

        tv(tree,te.empleado.read_all())