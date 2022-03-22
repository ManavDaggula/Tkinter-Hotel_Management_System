'''
This file is a compilation of all function definitions used in the making of project files
tried by Manav.
'''

import tkinter as tk
import SQL_queries as queries
import sqlite3 as sql3

def create_room_table(container,selected_option):
    # Insert sql logic here
    query=""
    if (selected_option=="All"):
        query=queries.room_all
    elif (selected_option=="Occupied"):
        query=queries.room_occupied
    else:
        query=queries.room_empty
    conn=sql3.connect("hotel_management.db")
    cur=conn.cursor()
    cur.execute(query)
    result=cur.fetchall()
    cur.close()
    conn.close()
    # ADDING HEADERS FOR COLUMNS
    lbl_header1 = tk.Label(container, text="Room No")
    lbl_header1.grid(row=0,column=0)
    lbl_header2 = tk.Label(container, text="Availability")
    lbl_header2.grid(row=0,column=1)
    lbl_header3 = tk.Label(container, text="Room Type")
    lbl_header3.grid(row=0,column=2)
    lbl_header4 = tk.Label(container, text="Customer ID")
    lbl_header4.grid(row=0,column=3)
    # ADDING THE ROWS
    row_count=1
    for row in result:
        lbl1 = tk.Label(container,text=row[0])
        lbl1.grid(row=row_count,column=0)
        lbl2 = tk.Label(container,text="Free")
        if(row[2]==None):
            lbl2['text']="Occupied"
        lbl2.grid(row=row_count,column=1)
        lbl3 = tk.Label(container,text=row[1])
        lbl3.grid(row=row_count,column=2)
        lbl4 = tk.Label(container, text=row[2])
        lbl4.grid(row=row_count,column=3)
        row_count+=1


def list_customers():
    query=queries.list_customers
    conn=sql3.connect("hotel_management.db")
    cur=conn.cursor()
    cur.execute(query)
    result=cur.fetchall()

    cur.close()
    conn.close()
    return list(result)