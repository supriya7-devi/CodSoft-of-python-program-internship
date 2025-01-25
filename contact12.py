import tkinter as tk
from tkinter import messagebox,simpledialog
contacts={}
def add_contact():
    name=simpledialog.askstring("Add contact","Enter name:")
    if name in contacts:
        messagebox.showerror("Error","Contact already exists!")
        return 
    phone=simpledialog.askstring("Add contact","Enter Phone Number:")
    email=simpledialog.askstring("Add Contact","Enter Email:")
    address=simpledialog.askstring("Add Contact","Enter Address:")
    if name and phone and email and address:
        contacts[name]={"Phone":phone,"Email":email,"Address":address}
        messagebox.showinfo("Success","Contact added successgfully!")
    else:
        messagebox.showerror("Error","All fields are required!")
def view_contacts():
    if not contacts:
        messagebox.showinfo("Contacts","No contacts found.")
        return
    contact_list="\n".join(f"Name:{name},Phone:{details['Phone']},Email:{details['Email']},Address:{details['Address']}"
    for name,details in contacts.items())
    messagebox.showinfo("Contact List",contact_list)
def search_contact():
    query=simpledialog.askstring("Search Contact","Enter name or phone number:")
    for name,details in contacts.items():
         if query == name or query ==details['Phone']:
            contact_info=f"Name:{name}\nPhone:{details['Phone']}\nEmail:{details['Email']}\nAddress:{details['Address']}"
            messagebox.showerror("Contact Found",contact_info)
            return
         messagebox.showerror("Error","Contact not Found.")
def update_contact():
    name=simpledialog.askstring("Update Contact","Enter new phone number to update:")
    if name not in contacts:
        messagebox.showerror("Error","Contact not found.")
        return
    phone=simpledialog.askstring("Update Contact","Enter new phone number(leave blank to keep current):")
    email=simpledialog.askstring("Update Contact","Enter new email(leave blank to keep current):")
    address=simpledialog.askstring("Update Contact","Enter new address(leave blank to keep current):")
    if phone:
        contacts[name]["Phone"]=phone
    if email:
        contacts[name]["Email"]=email
    if address:
        contacts[name]["Address"]=address
        messagebox.showinfo("Success","Contact updated successfully!")
def delete_contact():
    name=simpledialog.askstring("Delete Contact","Enter the name of contact to delete:")
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Success","Contact delete successfully!")

    else:
        messagebox.showinfo("Error","Contact not found.")
root = tk.Tk()
root.title("CONTACT BOOK")
tk.Label(root,text="Contact Book",font=("Arial",16)).pack(pady=10)
tk.Button(root,text="Add Contact",command=add_contact,width=20).pack(pady=5)
tk.Button(root,text="View Contact",command=view_contacts,width=20).pack(pady=5)
tk.Button(root,text="Search Contact",command=search_contact,width=20).pack(pady=5)
tk.Button(root,text="Update Contact",command=update_contact,width=20).pack(pady=5)
tk.Button(root,text="Delete Contact",command=delete_contact,width=20).pack(pady=5)
tk.Button(root,text="Exit",command=root.quit,width=20).pack(pady=5)
root.mainloop()