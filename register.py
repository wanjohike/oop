# import tkinter as tk
# from tkinter import messagebox
# import mysql.connector

# # Database connection
# def connect_db():
#     return mysql.connector.connect(
#         host="localhost",
#         user="yourusername",
#         password="yourpassword",
#         database="yourdatabase"
#     )

# # Registration function
# def register_user():
#     username = entry_username.get()
#     password = entry_password.get()
    
#     if username and password:
#         db = connect_db()
#         cursor = db.cursor()
#         cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
#         db.commit()
#         db.close()
#         messagebox.showinfo("Success", "Registration successful!")
#     else:
#         messagebox.showwarning("Input Error", "Please enter both username and password.")

# # Login function
# def login_user():
#     username = entry_username.get()
#     password = entry_password.get()
    
#     db = connect_db()
#     cursor = db.cursor()
#     cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
#     result = cursor.fetchone()
#     db.close()
    
#     if result:
#         messagebox.showinfo("Success", "Login successful!")
#     else:
#         messagebox.showerror("Error", "Invalid username or password.")

# # Tkinter GUI setup
# root = tk.Tk()
# root.title("Login and Registration")

# tk.Label(root, text="Username").grid(row=0, column=0)
# entry_username = tk.Entry(root)
# entry_username.grid(row=0, column=1)

# tk.Label(root, text="Password").grid(row=1, column=0)
# entry_password = tk.Entry(root, show="*")
# entry_password.grid(row=1, column=1)

# tk.Button(root, text="Register", command=register_user).grid(row=2, column=0)
# tk.Button(root, text="Login", command=login_user).grid(row=2, column=1)

# root.mainloop()


import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

# Database connection
def connect_db():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="22",
            database="registration"
        )
    except Error as e:
        messagebox.showerror("Database Error", f"Error connecting to database: {e}")
        return None

# Registration function
def register_user():
    username = entry_username.get()
    password = entry_password.get()
    
    if username and password:
        db = connect_db()
        if db:
            try:
                cursor = db.cursor()
                cursor.execute("INSERT INTO user (username, password) VALUES (%s, %s)", (username, password))
                db.commit()
                messagebox.showinfo("Success", "Registration successful!")
            except Error as e:
                messagebox.showerror("Database Error", f"Error inserting data: {e}")
            finally:
                db.close()
        else:
            messagebox.showerror("Database Error", "Failed to connect to the database.")
    else:
        messagebox.showwarning("Input Error", "Please enter both username and password.")

# Login function
def login_user():
    username = entry_username.get()
    password = entry_password.get()
    
    db = connect_db()
    if db:
        try:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM user WHERE username=%s AND password=%s", (username, password))
            result = cursor.fetchone()
            
            if result:
                messagebox.showinfo("Success", "Login successful!")
            else:
                messagebox.showerror("Error", "Invalid username or password.")
        except Error as e:
            messagebox.showerror("Database Error", f"Error querying data: {e}")
        finally:
            db.close()
    else:
        messagebox.showerror("Database Error", "Failed to connect to the database.")

# Tkinter GUI setup
root = tk.Tk()
root.title("Login and Registration")

tk.Label(root, text="Username").grid(row=0, column=0)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1)

tk.Label(root, text="Password").grid(row=1, column=0)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1)

tk.Button(root, text="Register", command=register_user).grid(row=2, column=0)
tk.Button(root, text="Login", command=login_user).grid(row=2, column=1)

root.mainloop()
