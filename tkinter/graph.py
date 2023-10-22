# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 09:49:03 2020

@author: jk
"""

from tkinter import *

master = Tk()

w = Canvas(master, width=200, height=100)
w.pack()
""" TODO
ecrire un point position random
valider hors canevas (bump)
faire bouger le point
animer le mouvement
"""
graph = tk_tools.Graph(
    parent=root,
    x_min=-1.0,
    x_max=1.0,
    y_min=0.0,
    y_max=2.0,
    x_tick=0.2,
    y_tick=0.2,
    width=500,
    height=400)

graph.grid(row=0, column=0)# create an initial line

line_0 = [(x/10, x/10) for x in range(10)]

graph.plot_line(line_0)

mainloop()

