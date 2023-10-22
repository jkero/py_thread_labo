# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:32:57 2020

@author: jk
"""

# -*- coding: utf-8 -*-
# Copyright (c) Juliette Monsel 2018
# For license see LICENSE
from ttkwidgets import Calendar
import tkinter as tk
from datetime import datetime

def validate():
    sel = calendar.selection
    if sel is not None:
        label.configure(text='Selected date: %s' % sel.isoformat('%x'))
        
window = tk.Tk()
calendar = Calendar(window, year=2020, month=3, selectforeground='white',
selectbackground='red')
calendar.pack()
tk.Button(window, text='Select', command=validate).pack()
label = tk.Label(window, text='Selected date:')
label.pack()
window.mainloop()