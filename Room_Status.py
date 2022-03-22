# This frame is used to display the Occupied/Empty/All rooms.

import tkinter as tk
import Manav_func as func

root=tk.Tk() # temporary root window
# Creating a Tkinter frame to hold everything to be displayed by room_status
frm_room_status = tk.Frame(root,bg="#0d3c59") # do not forget to place the correct master window
frm_room_status.pack(fill=tk.BOTH)

# Label to indicate we are on Room Status page
lbl_room_status=tk.Label(frm_room_status, text="Room Status", font=("Segoe Script",20), bg="#0d3c59", fg="#0099ff")
lbl_room_status.pack(fill=tk.X)

# Checkboxes to select display category
selected_option = tk.StringVar() #
selected_option.set("All")
# Frame to hold selection options
frm_select_room = tk.Frame(frm_room_status, bg="#0d3c59")
frm_select_room.pack(fill=tk.X)
chb_occupied=tk.Radiobutton(frm_select_room, text="Occupied", variable=selected_option, value="Occupied", bg="#0d3c59", fg="#0099ff", font=(14))
chb_empty=tk.Radiobutton(frm_select_room, text="Empty", variable=selected_option, value="Empty", bg="#0d3c59", fg="#0099ff", font=(14))
chb_all=tk.Radiobutton(frm_select_room, text="All", variable=selected_option, value="All", bg="#0d3c59", fg="#0099ff", font=(14))
chb_occupied.pack(side=tk.LEFT)
chb_empty.pack(side=tk.LEFT)
chb_all.pack(side=tk.LEFT)

# Creating a Frame to display the Table
frm_table = tk.Frame(frm_room_status, bg="#0d3c59")
frm_table.pack()
# Now creating a table i.e. a bunch of labels
func.create_room_table(frm_table,selected_option)
# Adding scrollbar
vscroll = tk.Scrollbar(frm_room_status,orient=tk.VERTICAL,command=frm_table.yview)
frm_table.config(yscrollcommand=vscroll.set)
vscroll.pack(side=tk.RIGHT, fill=tk.Y)

root.mainloop()