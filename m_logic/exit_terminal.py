import tkinter as tk
import sys

class redirect_text():
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self,string):
        self.text_widget.insert(tk.END,string)
        self.text_widget.see(tk.END)
    
    def flush(self):
        pass