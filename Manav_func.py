'''
This file is a compilation of all function definitions used in the making of project files
tried by Manav.
'''

import tkinter as tk
import SQL_queries as queries
import sqlite3 as sql3

def create_room_table(container,selected_option):
    try:
        # CLEARING THE FRAME
        for w in container.winfo_children():
            w.destroy()

        # Insert sql logic here
        #print("called")
        query=""
        if (selected_option.get()=="All"):
            query=queries.room_all
        elif (selected_option.get()=="Occupied"):
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
        lbl_header1 = tk.Label(container, text="Room No",bg="#0d3c59",fg="yellow",font=(15))
        lbl_header1.grid(row=0,column=0)
        lbl_header2 = tk.Label(container, text="Availability",bg="#0d3c59",fg="yellow",font=(15))
        lbl_header2.grid(row=0,column=1)
        lbl_header3 = tk.Label(container, text="Room Type",bg="#0d3c59",fg="yellow",font=(15))
        lbl_header3.grid(row=0,column=2)
        lbl_header4 = tk.Label(container, text="Customer ID",bg="#0d3c59",fg="yellow",font=(15))
        lbl_header4.grid(row=0,column=3)
        # ADDING THE ROWS
        row_count=1
        for row in result:
            # print(row)
            lbl1 = tk.Label(container,text=row[0],bg="#0d3c59",fg="#ffffff",font=(12))
            lbl1.grid(row=row_count,column=0)
            lbl2 = tk.Label(container,text="Free",bg="#0d3c59",fg="#00ff00",font=(12))
            if(row[2]!=None):
                lbl2['text']="Occupied"
                lbl2['fg']='#ffffff'
            lbl2.grid(row=row_count,column=1)
            lbl3 = tk.Label(container,text=row[1],bg="#0d3c59",fg="#ffffff",font=(12))
            lbl3.grid(row=row_count,column=2)
            lbl4 = tk.Label(container, text=row[2],bg="#0d3c59",fg="#ffffff",font=(12))
            lbl4.grid(row=row_count,column=3)
            row_count+=1
        # column expansion set to true
        for i in range(4):
            container.columnconfigure(i,weight=1)
    except:
        print("Some Error has occured")


def list_customers():
    try:
        query=queries.list_customers
        conn=sql3.connect("hotel_management.db")
        cur=conn.cursor()
        cur.execute(query)
        result=cur.fetchall()
        print(result)

        cur.close()
        conn.close()
        l=[]
        for r in result:
            l.append(r[0])
        return l
    except:
        print("Error has occured in listing")

def fetch_customer_details(option,l1,l2,l3,l4,l5):
    try:
        # query=queries.customer_details+option.get()+";"
        query=queries.customer_details
        conn=sql3.connect("hotel_management.db")
        cur=conn.cursor()
        cur.execute(query,option.get())
        result=cur.fetchall()
        print(result)
        l1["text"]=result[0][0]
        l2["text"]=result[0][1]
        l3["text"]=result[0][2]
        l5["text"]=result[0][3]
        l5["text"]=result[0][4]

        cur.close()
        conn.close()
        
    except:
        print("Error has occuredin fetching")