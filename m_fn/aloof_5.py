from m_logic import table_reg_tiempo as rt
import m_logic.exit_terminal as xt
import tkinter as tk
from tkinter import ttk
import sys
from m_fn.sf.treeview import treeview as tv
from m_fn.sf.placeholder import placeholder

class tab_registro_tiempo(tk.Frame):
    def __init__(self,master):
        super().__init__(master)

        subtab = ttk.Notebook(self)
        subtab.pack(expand = True, fill = "both")

        tab = tk.Frame(subtab)

        subtab.add(tab, text= "Agregar")

        label = tk.Label(tab, text="AGREGAR REGISTRO DE TIEMPO", font= 16).place(x=100,y=10)
        label2 = tk.Label(tab, text="VISTA REGISTRO DE TIEMPO", font= 16).place(x=120,y=200)

        tittle_empleado = tk.Label(tab,text="Empleado").place(x=50,y=60)
        text_empleado = tk.Entry(tab,width=55,)
        text_empleado.place(x=150,y=60)
        placeholder(text_empleado,"ID empleado")
        
        tittle_proyecto = tk.Label(tab,text="Proyecto").place(x=50,y=80)
        text_proyecto = tk.Entry(tab,width=55)
        text_proyecto.place(x=150,y=80)
        placeholder(text_proyecto,"ID proyecto")

        tittle_registro = tk.Label(tab,text="Fecha registro").place(x=50,y=100)
        text_registro = tk.Entry(tab,width=55)
        text_registro.place(x=150,y=100)
        placeholder(text_registro,"Fecha formato YYYYMMDD")

        tittle_horas = tk.Label(tab,text="Cantidad horas").place(x=50,y=120)
        text_horas = tk.Entry(tab,width=55)
        text_horas.place(x=150,y=120)
        placeholder(text_horas,"Horas trabajadas")

        tittle_tb_realizado = tk.Label(tab,text="Trabajo realizado").place(x=50,y=140)
        text_tb_realizado = tk.Entry(tab,width=55)
        text_tb_realizado.place(x=150,y=140)
        placeholder(text_tb_realizado,"Breve resumen de lo que hizo en el turno")

        def agregar_datos_reg_tiempo():

            v1 = text_empleado.get()
            v2 = text_proyecto.get()
            v3 = text_registro.get()
            v4 = text_horas.get()
            v5 = text_tb_realizado.get()

            if not v1.isdigit():
                print("valor no valido en id empleado")
                text_empleado.delete(0,tk.END)
                return
            
            if not v2.isdigit():
                print("valor no valido en id proyecto")
                text_proyecto.delete(0,tk.END)
                return

            if not len(v3) ==8:
                print("el formato de fecha es YYYYMMDD")
                text_registro.delete(0,tk.END)
                return
            
            if not v4.isdigit():
                print("el valor no es valido en cantidad de horas")
                text_horas.delete(0,tk.END)
                return
            
            if not len(v5) <= 500:
                print("el valor exede los caracteres maximos")
                text_tb_realizado.delete(0,tk.END)
                return
            
            if not len(v5) > 0:
                print("el valor no contiene nada")
                text_tb_realizado.delete(0,tk.END)
                return
            
            v1 = int(v1)
            v2 = int(v2)
            v4 = int(v4)

            datos = rt.reg_tiempo(v1,v2,v3,v4,v5)
            datos.create()
            print("Creacion de registro exitoso")

            text_empleado.delete(0,tk.END)
            text_proyecto.delete(0,tk.END)
            text_registro.delete(0,tk.END)
            text_horas.delete(0,tk.END)
            text_tb_realizado.delete(0,tk.END)

            tv(tree,rt.reg_tiempo.read_all())

        boton_save = tk.Button(tab, text="Guardar", command=agregar_datos_reg_tiempo)
        boton_save.place(x=10,y=10)

        tree = ttk.Treeview(tab, columns=("ID", "Empleado asignado", "Proyecto", "Fecha registro","Horas trabajadas","Trabajo realizado"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Empleado asignado", text="Empleado asignado")
        tree.heading("Proyecto", text="Proyecto")
        tree.heading("Fecha registro", text="Fecha registro")
        tree.heading("Horas trabajadas", text="Horas trabajadas")
        tree.heading("Trabajo realizado", text="Trabajo realizado")

        tree.place(x=12,y=260)

        tree.column("ID",width=25,anchor=tk.CENTER)
        tree.column("Empleado asignado",width=120,anchor=tk.CENTER)
        tree.column("Proyecto",width=60,anchor=tk.CENTER)
        tree.column("Fecha registro",width=100,anchor=tk.CENTER)
        tree.column("Horas trabajadas",width=100,anchor=tk.CENTER)
        tree.column("Trabajo realizado",width=110,anchor=tk.CENTER)

        tv(tree,rt.reg_tiempo.read_all())