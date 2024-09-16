# create a tkinter window for registration with the following fields;
# username
# firstname, surname, email, password,repeat password, phone number
# login button
# registration button
# exit button

# create a login page containing username and password fields
# login, reigstration and exit buttons

# download and install Xampp

import tkinter as tk
import mysql.connector#this is for connection to the database

# set up the database connection
def connect_db():
    return mysql.connector.connect(
        host = 'localhost',
        user = 'admin',
        password='1234',
        database ='retail'
    )


# define the function to register the user
def register_user():
    user = userentry.get()
    fName = fnameentry.get()
    sName = snameentry.get()
    password = passentry.get()
    repassword = repassentry.get()
    phone = phone_entry.get()

    if repassword != password:
        print("Password Missmatch")

    else:
        print('registration successful')





main_home = tk.Tk()
main_home.title("Registration Form")
main_home.geometry('400x300')
main_home.resizable(False,False)

# username (label) and userentry(textbox) widgets
username = tk.Label(main_home, text="Username")
username.grid(row=0, column=0)

userentry = tk.Entry(main_home)
userentry.grid(row=0, column=1)

# firstname label and textbox 
fname = tk.Label(main_home, text="First Name")
fname.grid(row=1, column=0)

fnameentry = tk.Entry(main_home)
fnameentry.grid(row=1, column=1)

# surname fields
# firstname label and textbox 
sname = tk.Label(main_home, text="Surname")
sname.grid(row=2, column=0)

snameentry = tk.Entry(main_home)
snameentry.grid(row=2, column=1)


# password
password = tk.Label(main_home, text="Password")
password.grid(row=3, column=0)

passentry = tk.Entry(main_home)
passentry.grid(row=3, column=1)

# password confirmation
repassword = tk.Label(main_home, text="Retype Password")
repassword.grid(row=4, column=0)

repassentry = tk.Entry(main_home)
repassentry.grid(row=4, column=1)

# password confirmation
phone = tk.Label(main_home, text="Phone Number")
phone.grid(row=5, column=0)

phone_entry = tk.Entry(main_home)
phone_entry.grid(row=5, column=1)

# create a frame to hold the buttons

# button_frame = tk.Frame(main_home, borderwidth=5, relief="sunken")

login = tk.Button(main_home, text="Login")
login.grid(row=6, column=0)

register = tk.Button(main_home, text="Register")
register.grid(row=6, column=1)

exit = tk.Button(main_home, text="Exit", command=exit)
exit.grid(row=6, column=2)


main_home.mainloop()