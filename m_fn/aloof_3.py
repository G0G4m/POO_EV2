import tkinter as tk
from tkinter import ttk

class tab_departamento(tk.Frame):
    def __init__(self,master):
        super().__init__(master)

        subtab = ttk.Notebook(self)
        subtab.pack(expand = True, fill = "both")

        tab1 = tk.Frame(subtab)
        tab2 = tk.Frame(subtab)
        tab3 = tk.Frame(subtab)

        subtab.add(tab1, text= "Agregar")
        subtab.add(tab2, text= "Editar")
        subtab.add(tab3, text = "Eliminar")