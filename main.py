from m_db.table import create_table
from m_fn.sf.terminal import terminal_text as tertex
import tkinter as tk
from tkinter import ttk
from m_fn.aloof_1 import tab_home
from m_fn.aloof_2 import tab_proyecto
from m_fn.aloof_3 import tab_departamento
from m_fn.aloof_4 import tab_empleado
from m_fn.aloof_5 import tab_registro_tiempo

def interfaz():

    root = tk.Tk()
    root.geometry("550x650")
    root.title("Framwork DB")
    root.resizable(False, False)
    
    notebook = ttk.Notebook(root)
    notebook.pack(expand= True, fill= "both")
    
    home_tab = tab_home(notebook)
    empleado_tab = tab_empleado(notebook)
    departamento_tab = tab_departamento(notebook)
    proyecto_tab = tab_proyecto(notebook)
    registro_tab = tab_registro_tiempo(notebook)

    #notebook.add(home_tab, text= "Home")
    notebook.add(empleado_tab, text= "Empleado")
    #notebook.add(departamento_tab, text= "Departamento")
    #notebook.add(proyecto_tab, text = "Proyecto")
    notebook.add(registro_tab, text = "Registro Tiempo")

    tertex(notebook)

    root.mainloop()

create_table()

interfaz()