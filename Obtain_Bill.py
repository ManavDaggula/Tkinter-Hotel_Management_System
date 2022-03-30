import tkinter as tk
import Manav_func as func
# func.obtain_bill("3")
root = tk.Tk()

l = tk.Label(root,text="Enter Bill Number")
l.grid(row=0,column=0)
t = tk.Entry(root)
t.grid(row=0,column=1)
b = tk.Button(root,text="Get Bill",command=lambda: func.obtain_bill(t.get()))
b.grid(row=1,column=0,columnspan=2)


root.mainloop()