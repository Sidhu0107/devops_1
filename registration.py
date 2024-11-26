import tkinter as tk
from tkinter import messagebox

def register():
    username = entry_username.get()
    email = entry_email.get()
    password = entry_password.get()

    if username and email and password:
        # Here you can add code to save the user data to a database
        messagebox.showinfo("Registration", "Registration Successful!")
    else:
        messagebox.showwarning("Registration", "Please fill out all fields.")

# Create the main window
root = tk.Tk()
root.title("Registration Page")

# Create and place the username label and entry
label_username = tk.Label(root, text="Username:")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Create and place the email label and entry
label_email = tk.Label(root, text="Email:")
label_email.pack(pady=5)
entry_email = tk.Entry(root)
entry_email.pack(pady=5)

# Create and place the password label and entry
label_password = tk.Label(root, text="Password:")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Create and place the register button
button_register = tk.Button(root, text="Register", command=register)
button_register.pack(pady=20)

# Run the main event loop
root.mainloop()
