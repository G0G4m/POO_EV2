import tkinter as tk
import sys
import m_logic.exit_terminal as xt

def terminal_text(subtab):
    terminal_text = tk.Text(subtab,wrap="word",highlightthickness=2,font=("arial",10))
    terminal_text.place(x=12,y=570,height=40,width=518)
    terminal_text.config(tk.END,)

    redir = xt.redirect_text(terminal_text)
    sys.stdout = redir