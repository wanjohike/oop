# create the login page containing the username and password fields
# add the login, reigster and exit buttons

import tkinter as tk

main_home = tk.Tk()
main_home.title("Login Form")
main_home.geometry('400x300')
main_home.resizable(False,False)

# function to close the program
def exit():
    main_home.destroy()

#username and password field
title = tk.Label(main_home, text="Please Enter your Username and Password to Login")
title.grid(row=0, column=0, columnspan=2)

username = tk.Label(main_home, text="Username")
username.grid(row=1, column=0)

userentry = tk.Entry(main_home)
userentry.grid(row=1, column=1)

password = tk.Label(main_home, text="Password")
password.grid(row=2, column=0)

passentry = tk.Entry(main_home)
passentry.grid(row=2, column=1)

login = tk.Button(main_home, text="Login")
login.grid(row=3, column=0)

register = tk.Button(main_home, text="Register")
register.grid(row=3, column=1)

exit = tk.Button(main_home, text="Exit", command=exit)
exit.grid(row=3, column=2)

main_home.mainloop()