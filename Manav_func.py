'''
This file is a compilation of all function definitions used in the making of project files
tried by Manav.
'''

import tkinter as tk
import tkinter.messagebox
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
        l4["text"]=result[0][3]
        l5["text"]=result[0][4]

        cur.close()
        conn.close()
        
    except:
        print("Error has occured in fetching")

def perform_checkout(frm,cust_id):
    for x in frm.winfo_children():
        x.destroy()
    lbl1=tk.Label(frm,text="Customer ID",bg="#0d3c59",fg="#79c0ec",font=("Helvetica",15,"bold"))
    lbl2=tk.Label(frm,text="Entry Date-Time",bg="#0d3c59",fg="#79c0ec",font=("Helvetica",15,"bold"))
    lbl3=tk.Label(frm,text="Exit Date-Time",bg="#0d3c59",fg="#79c0ec",font=("Helvetica",15,"bold"))
    lbl4=tk.Label(frm,text="Total Fare",bg="#0d3c59",fg="#79c0ec",font=("Helvetica",15,"bold"))
    lbl1.grid(row=0,column=0)
    lbl2.grid(row=1,column=0)
    lbl3.grid(row=2,column=0)
    lbl4.grid(row=3,column=0)

    lbl5 = tk.Label(frm,text=cust_id,bg="#0d3c59",fg="yellow",font=(12))
    lbl6 = tk.Label(frm,bg="#0d3c59",fg="yellow",font=(12))
    lbl7 = tk.Label(frm,bg="#0d3c59",fg="yellow",font=(12))
    lbl8 = tk.Label(frm,bg="#0d3c59",fg="#f66628",font=(12))
    lbl5.grid(row=0,column=1)
    lbl6.grid(row=1,column=1)
    lbl7.grid(row=2,column=1)
    lbl8.grid(row=3,column=1)

    btn_back = tk.Button(frm,text="Back",command=lambda: cancel_checkout(frm))
    btn_back.grid(row=4,column=0)
    btn_ok = tk.Button(frm,text="OK",command=lambda: delete_customer(cust_id))
    btn_ok.grid(row=4,column=1)

    try:
        query=queries.calc_fare
        conn=sql3.connect("hotel_management.db")
        cur=conn.cursor()
        cur.execute(query,cust_id)
        result=cur.fetchone()
        print(result)

        lbl5.config(text=cust_id)
        lbl6.config(text=result[0])
        lbl7.config(text=result[1])
        lbl8.config(text=result[2])

        cur.close()
        conn.close()

    except Exception as e:
        print("Error has occured while checking out.")
        # print(e)


def delete_customer(cust_id):
    print("Ok button pressed.")
    try:
        conn=sql3.connect("hotel_management.db")
        cur=conn.cursor()
        
        query=queries.empty_room
        cur.execute(query,cust_id)
        query=queries.delete_customer
        cur.execute(query,cust_id)
        
        conn.commit()
        cur.close()
        conn.close()

        tkinter.messagebox.showinfo(title=None,message="Check-Out Completed")
        exit()

    except Exception as e:
        # print("Error occurred in deleting customer record.")
        print(e)

def cancel_checkout(frm):
    for x in frm.winfo_children():
        x.destroy()
    lbl_1 = tk.Label(frm,text="Customer ID", bg="#0d3c59",fg="#79c0ec",font=("Helvetica",15,"bold"))
    lbl_1.grid(row=0,column=0)
    lbl_2 = tk.Label(frm,text="Name", bg="#0d3c59",fg="#79c0ec",font=("Helvetica",15,"bold"))
    lbl_2.grid(row=1,column=0)
    lbl_3 = tk.Label(frm,text="Phone", bg="#0d3c59",fg="#79c0ec",font=("Helvetica",15,"bold"))
    lbl_3.grid(row=2,column=0)
    lbl_4 = tk.Label(frm,text="Aadhar", bg="#0d3c59",fg="#79c0ec",font=("Helvetica",15,"bold"))
    lbl_4.grid(row=3,column=0)
    lbl_5 = tk.Label(frm,text="Gender", bg="#0d3c59",fg="#79c0ec",font=("Helvetica",15,"bold"))
    lbl_5.grid(row=4,column=0)
    lbl_6 = tk.Label(frm,text="Check-In Date & Time", bg="#0d3c59",fg="#79c0ec",font=("Helvetica",15,"bold"))
    lbl_6.grid(row=5,column=0)
    selected_customer=tk.StringVar()
    selected_customer.set("Select a customer ID")
    lbl_7 = tk.Label(frm,text="-", bg="#0d3c59",fg="yellow",font=(15))
    lbl_7.grid(row=1,column=1)
    lbl_8 = tk.Label(frm,text="-", bg="#0d3c59",fg="yellow",font=(15))
    lbl_8.grid(row=2,column=1)
    lbl_9 = tk.Label(frm,text="-", bg="#0d3c59",fg="yellow",font=(15))
    lbl_9.grid(row=3,column=1)
    lbl_10 = tk.Label(frm,text="-", bg="#0d3c59",fg="yellow",font=(15))
    lbl_10.grid(row=4,column=1)
    lbl_11 = tk.Label(frm,text="-", bg="#0d3c59",fg="yellow",font=(15))
    lbl_11.grid(row=5,column=1)
    optn_1 = tk.OptionMenu(frm,selected_customer,*list_customers(), command=lambda x: fetch_customer_details(selected_customer,lbl_7,lbl_8,lbl_9,lbl_10,lbl_11))
    optn_1.grid(row=0,column=1)
    # img_btn = tk.PhotoImage(file="checkButton.png")
    # btn_chk = tk.Button(frm_checkout,text="",image=img_btn,command=lambda : func.fetch_customer_details(selected_customer,lbl_7,lbl_8,lbl_9,lbl_10,lbl_11))
    # btn_chk.grid(row=0,column=2)

    # Adding the next button
    # img_btn = tk.PhotoImage(file="nextButton.png")
    btn_next = tk.Button(frm,text="Next",bg="#0d3c59", fg="#79c0ec", command=lambda: perform_checkout(frm,selected_customer.get()))
    btn_next.grid(row=6,column=1)

    for i in range(6):
        frm.rowconfigure(i,weight=1)
    frm.columnconfigure(0,weight=1)
    frm.columnconfigure(1,weight=1)