import tkinter as tk 
from tkinter import messagebox

master_password = "69yesdaddy"

def add():
    name = account_entry.get()
    pwd = password_entry.get()
    
    with open('password.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")
    
    account_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

def view():
    view_window = tk.Toplevel(root)
    view_window.title("View Passwords")
    
    master_pass_label = tk.Label(view_window, text="Enter Master Password")
    master_pass_label.pack()
    master_pass_entry = tk.Entry(view_window, show="#")
    master_pass_entry.pack()
    
    def check_master_password():
        if master_password == master_pass_entry.get():
            view_password()
        else:
            messagebox.showerror("Error", "Incorrect master password!")
            
    submit_button = tk.Button(view_window, text="Submit", command=check_master_password)
    submit_button.pack()

def view_password():
    view_password_window = tk.Toplevel(root) 
    view_password_window.title("View Passwords")
    
    table = tk.Frame(view_password_window)
    table.pack()
    
    headers = ["Accounts", "Password"]
    for i, header in enumerate(headers):
        tk.Label(table, text=header).grid(row=0, column=i, padx=5, pady=5)
    
    with open('password.txt', 'r') as f:
        for i, line in enumerate(f.readlines()):
            account, pwd = line.strip().split("|")
            tk.Label(table, text=account).grid(row=i+1, column=0, padx=5, pady=5)
            tk.Label(table, text=pwd).grid(row=i+1, column=1, padx=5, pady=5)

root = tk.Tk()
root.title("Daddy's Secrets / Password Manager")

tk.Label(root, text="Account:").grid(row=0, column=0, padx=10, pady=10)
account_entry = tk.Entry(root)
account_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, show="#")
password_entry.grid(row=1, column=1, padx=10, pady=10)

add_button = tk.Button(root, text="Add Password", command=add)
add_button.grid(row=2, column=0, columnspan=2, pady=10)

view_button = tk.Button(root, text="View Passwords", command=view)
view_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
