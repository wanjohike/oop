import tkinter as tk
def button_click(value):
    
    current_text = display.get()#tk.END refers to the position after the existing text. 
    display.delete(0, tk.END)
    display.insert(tk.END, current_text + str(value))
def clear_display():
    
    display.delete(0, tk.END)


def set_theme(theme):
    """
    Set the theme of the calculator.
    
    Parameters:
        theme (str): The theme to use. Can be either 'dark' or 'light'.
    """
    # Set the background color of the root (main window)
    if theme == 'dark':
        root.configure(bg='#333333')
        # Set the background color of the display
        display.configure(bg='#555555', fg='#ffffff')
    elif theme == 'light':
        root.configure(bg='#ADD8E6')
        # Set the background color of the display
        display.configure(bg='#ffffff', fg='#000000')
    else:
        raise ValueError("Invalid theme. Must be either 'dark' or 'light'")



def calculate():
    """
    Evaluate the mathematical expression in the display and display the result.

    This function is called when the "=" button is clicked.

    Parameters:
        None

    Returns:
        None
    """
    # Exception handling. This ensures that the program does not crash if the
    # expression is invalid or if there is some other error.
    try:
        # Get the expression from the display
        expression = display.get()
        # Evaluate the expression using the eval() function
        result = eval(expression)
        # Delete the current contents of the display
        display.delete(0, tk.END)
        # Insert the result into the display
        display.insert(tk.END, result)
    except Exception as e:
        # If there is an error, delete the current contents of the display
        display.delete(0, tk.END)
        # Insert the string "Error" into the display
        display.insert(tk.END, "Error")


#create the main window. you can call it anything, for instance main, being that its
#the first window 
root = tk.Tk()
root.title("My Calculator")
root.geometry("400x500")
root.resizable(False, False)#the window will not be resized
# root.eval('tk::PlaceWindow . center')
root.configure(bg="#ADD8E6")#set background color of the window

# menu bar
menu_bar = tk.Menu(root)
root.configure(menu=menu_bar)
theme_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Theme', menu=theme_menu)
theme_menu.add_command(label="Light", command=lambda: set_theme('light'))
theme_menu.add_command(label="Dark", command=lambda: set_theme('dark'))
#see if you can define a function to allow users to change their background color for line 26
display = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="flat", justify="right")
display.pack(pady=20, padx=20, fill="both")
buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    '0', 'C', '=', '+'
]
#create a new window over the current window
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

row = 0
col = 0

for button in buttons:
    action = lambda x=button: button_click(x) if x != "=" and x != "C" else calculate() if x == "=" else clear_display()
   #defines an anonymous function (lambda function) with a default argument x set to button. 
   #This lambda function is used to determine what action to take based on the value of x.
    tk.Button(button_frame, text=button, width=9, height=3,bg="#79E5F2", command=action).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

#define a function to allow users to use the keyboard instead of clicking on the buttons

root.mainloop()
