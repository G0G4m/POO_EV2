import tkinter as tk
from tkinter import ttk

texto_bienvenida = "Bienvenido admin al gestionador de la base de datos\nen las siguientes pestañas podras agregar,editar o eliminar datos de la base de datos\ndependiendo del area que quieras"

class tab_home(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.label = tk.Label( self, text = texto_bienvenida)
        self.label.pack(pady = 40, padx = 40)