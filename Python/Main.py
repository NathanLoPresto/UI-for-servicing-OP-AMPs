# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 13:17:08 2021

@author: Nathan LoPresto
"""
import sys
from PyQt5 import QtWidgets

#local imports 
from pyqtgraphing import MainWindow


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())

