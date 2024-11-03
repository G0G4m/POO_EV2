from m_logic import table_emp as te
import m_logic.exit_terminal as xt
import tkinter as tk
from tkinter import ttk
import sys
from m_fn.sf.terminal import terminal_text as tt
from m_fn.sf.treeview import treeview as tv
from m_fn.sf.placeholder import placeholder

class tab_empleado(tk.Frame):
    def __init__(self,master):
        super().__init__(master)

        subtab = ttk.Notebook(self)
        subtab.pack(expand = True, fill = "both")

        tab1 = tk.Frame(subtab)
        tab2 = tk.Frame(subtab)

        subtab.add(tab1, text= "Agregar")
        subtab.add(tab2, text= "Editar")