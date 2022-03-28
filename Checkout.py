import tkinter as tk
import Manav_func as func

# Temporarily creating a window
root=tk.Tk()

# now the header
lbl_checkout=tk.Label(root, text="Checkout", font=("Segoe Script",20), bg="#0d3c59", fg="#0099ff")
lbl_checkout.pack(fill=tk.X)

# Starting with the frame
frm_checkout = tk.Frame(root, bg="#0d3c59")
frm_checkout.pack(fill="both",expand=True)

#creating the labels to be displayed and dropdown list to be selected from
lbl_1 = tk.Label(frm_checkout,text="Customer ID", bg="#0d3c59",fg="#79c0ec",font=("Helvetica",15,"bold"))
lbl_1.grid(row=0,column=0)
lbl_2 = tk.Label(frm_checkout,text="Name", bg="#0d3c59",fg="#79c0ec",font=("Helvetica",15,"bold"))
lbl_2.grid(row=1,column=0)
lbl_3 = tk.Label(frm_checkout,text="Phone", bg="#0d3c59",fg="#79c0ec",font=("Helvetica",15,"bold"))
lbl_3.grid(row=2,column=0)
lbl_4 = tk.Label(frm_checkout,text="Aadhar", bg="#0d3c59",fg="#79c0ec",font=("Helvetica",15,"bold"))
lbl_4.grid(row=3,column=0)
lbl_5 = tk.Label(frm_checkout,text="Gender", bg="#0d3c59",fg="#79c0ec",font=("Helvetica",15,"bold"))
lbl_5.grid(row=4,column=0)
lbl_6 = tk.Label(frm_checkout,text="Check-In Date & Time", bg="#0d3c59",fg="#79c0ec",font=("Helvetica",15,"bold"))
lbl_6.grid(row=5,column=0)
selected_customer=tk.StringVar()
selected_customer.set("Select a customer ID")
lbl_7 = tk.Label(frm_checkout,text="-", bg="#0d3c59",fg="yellow",font=(15))
lbl_7.grid(row=1,column=1)
lbl_8 = tk.Label(frm_checkout,text="-", bg="#0d3c59",fg="yellow",font=(15))
lbl_8.grid(row=2,column=1)
lbl_9 = tk.Label(frm_checkout,text="-", bg="#0d3c59",fg="yellow",font=(15))
lbl_9.grid(row=3,column=1)
lbl_10 = tk.Label(frm_checkout,text="-", bg="#0d3c59",fg="yellow",font=(15))
lbl_10.grid(row=4,column=1)
lbl_11 = tk.Label(frm_checkout,text="-", bg="#0d3c59",fg="yellow",font=(15))
lbl_11.grid(row=5,column=1)
optn_1 = tk.OptionMenu(frm_checkout,selected_customer,*func.list_customers(), command=lambda x: func.fetch_customer_details(selected_customer,lbl_7,lbl_8,lbl_9,lbl_10,lbl_11))
optn_1.grid(row=0,column=1)
# img_btn = tk.PhotoImage(file="checkButton.png")
# btn_chk = tk.Button(frm_checkout,text="",image=img_btn,command=lambda : func.fetch_customer_details(selected_customer,lbl_7,lbl_8,lbl_9,lbl_10,lbl_11))
# btn_chk.grid(row=0,column=2)

# Adding the next button
# img_btn = tk.PhotoImage(file="nextButton.png")
btn_next = tk.Button(frm_checkout,text="Next",bg="#0d3c59", fg="#79c0ec",command=lambda: func.perform_checkout(frm_checkout,selected_customer.get()))
btn_next.grid(row=6,column=1)

for i in range(6):
    frm_checkout.rowconfigure(i,weight=1)
frm_checkout.columnconfigure(0,weight=1)
frm_checkout.columnconfigure(1,weight=1)


root.mainloop()