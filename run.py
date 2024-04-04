import tkinter as tk
from tkinter import messagebox
import os
from main import check_path
def assign_path():
    global path_variable
    path_variable = entry.get()
    if os.path.exists(path_variable):
        messagebox.showinfo("Path Assigned", f"The cleaning of the folder is done , look at it :)")
        check_path(path_variable)
    else:
        messagebox.showerror("Error", "The entered path does not exist. Please enter a valid path.")

root = tk.Tk()
root.title("Path Assignment")
root.geometry("900x400") 

instructions_text = """Instructions:
1. Enter the path in the field below.
2. Click on 'Assign Path' button to proceed."""
instructions_label = tk.Label(root, text=instructions_text, justify=tk.LEFT)
instructions_label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack()

assign_button = tk.Button(root, text="Assign Path", command=assign_path)
assign_button.pack()

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
