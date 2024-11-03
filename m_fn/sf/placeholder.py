import tkinter as tk

def placeholder(entry,placeholder_text):
    
    def on_entry_click(event):
        if entry.get() == placeholder_text:
            entry.delete(0,tk.END)
            entry.config(fg="black")
    
    def on_focusout(event):
        if entry.get() == "":
            entry.insert(0,placeholder_text)
            entry.config(fg="grey")
    
    entry.insert(0,placeholder_text)
    entry.bind("<FocusIn>",on_entry_click)
    entry.bind("<FocusOut>",on_focusout)
    entry.config(fg="grey") 