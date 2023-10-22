# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 14:43:29 2020

@author: jk
"""


from PyQt5.QtCore import *

from PyQt5.QtWidgets import *

class Dlg(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.layout = QGridLayout(self)
        self.label1 = QLabel('Visualizzare tutti i beni per:')
        self.label2 = QLabel('Macro-epoca originaria:')

        comunes = ['Ameglia', 'Arcola', 'Bagnone', 'Bolano', 'Carrara', 'Casola', 'Castelnuovo Magra',
                   'Comano, località Crespiano', 'Fivizzano', 'Fivizzano località Pieve S. Paolo', 
                   'Fivizzano località Pieve di Viano', 'Fivizzano località Soliera', 'Fosdinovo'
                   'Genova', 'La Spezia', 'Levanto', 'Licciana Nardi', 'Lucca', 'Lusuolo', 'Massa',
                   'Minucciano', 'Montignoso', 'Ortonovo', 'Piazza al sercho', 'Pietrasanta', 'Pignine',
                   'Pisa', 'Podenzana', 'Pontremoli', 'Portovenere', 'Santo Stefano di Magra', 'Sarzana',
                   'Serravezza', 'Sesta Godano', 'Varese Ligure', 'Vezzano Ligure', 'Zignago' ]

        nb_row = len(comunes)
        nb_col = 1

        data = [ [] for i in range(nb_row) ]

        for i, comune in enumerate(comunes):
            for j in range(nb_col):
                data[i].append(comune)

        self.table1 = QTableWidget()
        self.table1.horizontalHeader().setStretchLastSection(True)

        self.table1.setRowCount(nb_row)
        self.table1.setColumnCount(nb_col)
        self.table1.setHorizontalHeaderLabels(['Comune'])

        for row in range (nb_row):
            for col in range(nb_col):
                item = QTableWidgetItem(str(data[row][col]))
                self.table1.setItem(row, col, item)

        self.layout.addWidget(self.label1, 0, 0)
        self.layout.addWidget(self.table1, 1, 0)
        self.layout.addWidget(self.label2, 2, 0)

w = Dlg()
w.resize(350,300)
w.setWindowTitle('Ricerca beni')
w.setWindowFlags(Qt.WindowStaysOnTopHint)
w.show()