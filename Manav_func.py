'''
This file is a compilation of all function definitions used in the making of project files
tried by Manav.
'''

import tkinter as tk
from SQL_queries import *
import sqlite3 as sql3

def create_room_table(container):
    # Insert sql logic here

    row_data=[('1','2','3'),('a','b','c'),('x','y','z')]
    for x in range(len(row_data)):
        for y in range(len(row_data[x])):
            lbl=tk.Label(container,text=row_data[x][y])
            lbl.grid(row=x,column=y)