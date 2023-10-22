# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:27:03 2020

@author: jk
"""

from ttkwidgets import AutoHideScrollbar

import tkinter as tk

window=tk.Tk()
listbox=tk.Listbox(window,height=5)
scrollbar=AutoHideScrollbar(window,command=listbox.yview)
listbox.configure(yscrollcommand=scrollbar.set)

for i in range(10):
    listbox.insert('end','item %i'%i)

tk.Label(window,text="Increase the window's height\ntomake the scrollbar vanish.").pack(side='top',padx=4,pady=4)
scrollbar.pack(side='right',fill='y')
listbox.pack(side='left',fill='both',expand=True)
window.mainloop()