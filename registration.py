import tkinter as tk
from tkinter import messagebox
from dbconnector import connect_db
from mysql.connector import Error


# define the function to register the user
def register_user():
    user = userentry.get()
    fName = fnameentry.get()
    sName = snameentry.get()
    password = passentry.get()
    repassword = repassentry.get()
    phone = phone_entry.get()

    if repassword != password:
        messagebox.showerror('Password Error', 'Password Mismatch')

    else:
       try:
        db = connect_db()
        cursor = db.cursor() #  use the cursor cvlass to execute our sql code
        sql ='insert into registration (username, fname,surname,pass,phone) values(%s, %s,%s,%s,%s)' 
        val=(user,fName,sName,password,phone)
        cursor.execute(sql,val)
        db.commit()
        messagebox.showinfo('Success', 'Registration Successful')
       except Error as e:
        messagebox.showerror('Database Error', f'Data Could Not be Saved!!')
        cursor.close()#close the database connection
       finally:
        db.close()

# define a function for login into the system

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

register = tk.Button(main_home, text="Register", command = register_user)
register.grid(row=6, column=1)

exit = tk.Button(main_home, text="Exit", command=exit)
exit.grid(row=6, column=2)


main_home.mainloop()