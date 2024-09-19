import tkinter as tk
from tkinter import messagebox
from validate_email import validate_email
from tkcalendar import DateEntry
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
    gender = gender_var.get()
    # dob = dob_entry.get()
    # add email
    # add gender (male, female, rather not say)
    # date of birth
    email = emailentry.get()
    dob = dob_entry.get()

    if repassword != password:
        messagebox.showerror('Password Error', 'Password Mismatch')
    elif len(password) <=6:
        messagebox.showerror('Password Error', 'Password Must be more than 6 Characters')
    # validate the email
    elif validate_email(email)==False:
       messagebox.showinfo('Invalid Email','Please Check Email and Try Again')

    else:
       try:
        db = connect_db()
        cursor = db.cursor() #  use the cursor class to execute our sql code
        sql ='insert into registration (username, fname,sname,pass,phone,gender,email) values(%s, %s,%s,%s,%s,%s,%s)' 
        val = (user,fName,sName,password,phone,gender,email)
        cursor.execute(sql,val)
        db.commit()
        result=messagebox.askquestion('Registration Successful', 'Add New Record?')
        if result =='no':
           main_home.destroy()
        else:#clear the values in the widgets
           userentry.delete(0, tk.END)
           fnameentry.delete(0, tk.END)
           snameentry.delete(0, tk.END)
           emailentry.delete(0,tk.END)
           passentry.delete(0,tk.END)
           repassentry.delete(0,tk.END)
           phone_entry.delete(0,tk.END)
           gender_var.set(None)
           dob_entry.set_date('')

       except Error as e:
        messagebox.showerror('Database Error', f'Data could not be saved:{e}')
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

passentry = tk.Entry(main_home, show='*')
passentry.grid(row=3, column=1)

# password confirmation
repassword = tk.Label(main_home, text="Retype Password")
repassword.grid(row=4, column=0)

repassentry = tk.Entry(main_home, show='*')
repassentry.grid(row=4, column=1)

# password confirmation
phone = tk.Label(main_home, text="Phone Number")
phone.grid(row=5, column=0)

phone_entry = tk.Entry(main_home)
phone_entry.grid(row=5, column=1)

# email
email = tk.Label(main_home, text="Email")
email.grid(row=6, column=0)

emailentry = tk.Entry(main_home)
emailentry.grid(row=6, column=1)

# gender
gender_var =tk.StringVar()
gender_var.set(None)

gender_label = tk.Label(main_home,text='Gender')
gender_label.grid(row=7, column=0)

male_rb = tk.Radiobutton(main_home, text='Male', variable=gender_var,value='Male')
male_rb.grid(row=7, column=1)

female_rb = tk.Radiobutton(main_home, text='Female', variable=gender_var,value='Female')
female_rb.grid(row=7, column=2)

other_rb = tk.Radiobutton(main_home, text='Rather Not Say', variable=gender_var,value='Rather Not Say')
other_rb.grid(row=7, column=3)

# dateofbirth
dob_label = tk.Label(main_home,text='Date of Birth')
dob_label.grid(row=8, column=0)

dob_entry = DateEntry(main_home, date_patter='dd-mm-y')
dob_entry.grid(row=8, column=1)

login = tk.Button(main_home, text="Login")
login.grid(row=9, column=0)

register = tk.Button(main_home, text="Register", command = register_user)
register.grid(row=9, column=1)

exit = tk.Button(main_home, text="Exit", command=exit)
exit.grid(row=9, column=2)


main_home.mainloop()