# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 12:33:44 2020

@author: jk
"""


import sys
from PyQt5.QtWidgets import QLineEdit, QApplication, QWidget, QLabel, QPushButton, QMessageBox

def dialog():
    mbox = QMessageBox()

    mbox.setText("Your allegiance has been noted")
    mbox.setDetailedText("You are now a disciple and subject of the all-knowing Guru")
    mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            
    mbox.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(300,300)
    w.setWindowTitle('Guru99')
    
    label = QLabel(w)
    label.setText("Behold the Guru, Guru99")
    label.move(100,130)
    label.show()

    btn = QPushButton(w)
    btn.setText('Beheld')
    btn.move(110,150)
    btn.show()
    btn.clicked.connect(dialog)
    
    # line = QLineEdit()
    # line.move(120, 130)
    # line.show()

    
    w.show()
    sys.exit(app.exec_())