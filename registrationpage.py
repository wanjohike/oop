# import tkinter as tk
# import mysql.connector  # this is for connection to the database

# # set up the database connection
# def connect_db():
#     return mysql.connector.connect(
#         host='localhost',
#         user='admin',
#         password='1234',
#         database='retail'
#     )

# # define the function to register the user
# def register_user():
#     user = userentry.get()
#     fName = fnameentry.get()
#     sName = snameentry.get()
#     password = passentry.get()
#     repassword = repassentry.get()
#     phone = phone_entry.get()

#     if repassword != password:
#         print("Password Mismatch")
#     else:
#         print('Registration successful')

# main_home = tk.Tk()
# main_home.title("Registration Form")
# main_home.geometry('400x300')
# main_home.resizable(False, False)

# # Create a frame to hold the widgets with a different background color
# frame = tk.Frame(main_home, bg='lightblue')
# frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# # username (label) and userentry(textbox) widgets
# username = tk.Label(frame, text="Username", bg='white')
# username.grid(row=0, column=0, padx=5, pady=5)

# userentry = tk.Entry(frame)
# userentry.grid(row=0, column=1, padx=5, pady=5)

# # firstname label and textbox 
# fname = tk.Label(frame, text="First Name", bg='lightblue')
# fname.grid(row=1, column=0, padx=5, pady=5)

# fnameentry = tk.Entry(frame)
# fnameentry.grid(row=1, column=1, padx=5, pady=5)

# # surname fields
# sname = tk.Label(frame, text="Surname", bg='lightblue')
# sname.grid(row=2, column=0, padx=5, pady=5)

# snameentry = tk.Entry(frame)
# snameentry.grid(row=2, column=1, padx=5, pady=5)

# # password
# password = tk.Label(frame, text="Password", bg='lightblue')
# password.grid(row=3, column=0, padx=5, pady=5)

# passentry = tk.Entry(frame, show='*')
# passentry.grid(row=3, column=1, padx=5, pady=5)

# # password confirmation
# repassword = tk.Label(frame, text="Retype Password", bg='lightblue')
# repassword.grid(row=4, column=0, padx=5, pady=5)

# repassentry = tk.Entry(frame, show='*')
# repassentry.grid(row=4, column=1, padx=5, pady=5)

# # phone number
# phone = tk.Label(frame, text="Phone Number", bg='lightblue')
# phone.grid(row=5, column=0, padx=5, pady=5)

# phone_entry = tk.Entry(frame)
# phone_entry.grid(row=5, column=1, padx=5, pady=5)

# # buttons
# login = tk.Button(main_home, text="Login")
# login.grid(row=6, column=0, padx=5, pady=5)

# register = tk.Button(main_home, text="Register", command=register_user)
# register.grid(row=6, column=1, padx=5, pady=5)

# exit = tk.Button(main_home, text="Exit", command=main_home.quit)
# exit.grid(row=6, column=2, padx=5, pady=5)

# main_home.mainloop()


import tkinter as tk
import mysql.connector  # this is for connection to the database

# set up the database connection
def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='retail'
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
        print("Password Mismatch")
    else:
        db = connect_db()
        cursor = db.cursor()
        
        """ Allows Python code to execute PostgreSQL command in a database session. 
        Cursors are created by the connection.cursor() method: 
        they are bound to the connection for the entire lifetime and all the commands are executed 
        in the context of the database session wrapped by the connection."""

        sql = "INSERT INTO users (username, fname, sname, pass, pno) VALUES (%s, %s, %s, %s, %s)"
        val = (user, fName, sName, password, phone)
        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        db.close()
        print('Registration successful')

main_home = tk.Tk()
main_home.title("Registration Form")
main_home.geometry('400x300')
main_home.resizable(False, False)

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
sname = tk.Label(main_home, text="Surname")
sname.grid(row=2, column=0)

snameentry = tk.Entry(main_home)
snameentry.grid(row=2, column=1)

# password
password = tk.Label(main_home, text="Password")
password.grid(row=3, column=0)

passentry = tk.Entry(main_home, show='*')
passentry.grid(row=3, column=1)

# password confirmation
repassword = tk.Label(main_home, text="Retype Password")
repassword.grid(row=4, column=0)

repassentry = tk.Entry(main_home, show='*')
repassentry.grid(row=4, column=1)

# phone number
phone = tk.Label(main_home, text="Phone Number")
phone.grid(row=5, column=0)

phone_entry = tk.Entry(main_home)
phone_entry.grid(row=5, column=1)

# create a frame to hold the buttons
login = tk.Button(main_home, text="Login")
login.grid(row=6, column=0)

register = tk.Button(main_home, text="Register", command=register_user)
register.grid(row=6, column=1)

exit = tk.Button(main_home, text="Exit", command=main_home.quit)
exit.grid(row=6, column=2)

main_home.mainloop()
