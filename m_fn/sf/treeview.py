import tkinter as tk

def treeview(tree,func):
        for row in tree.get_children():
            tree.delete(row)
        for row in func:
            view_date = tree.insert("", "end", values=row)
            tree.see(view_date)