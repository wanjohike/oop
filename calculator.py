import tkinter as tk
def button_click(value):
    current_text = display.get()#tk.END refers to the position after the existing text. 
    display.delete(0, tk.END)
    display.insert(tk.END, current_text + str(value))
def clear_display():
    display.delete(0, tk.END)
def calculate():
    #exception handling. this ensures that our program executes to the ens
    # and does not crash
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

#create the main window. you can call it anything, for instance main, being that its
#the first window 
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")
root.resizable(False, False)#the window will not be resized
root.configure(bg="#ADD8E6")#set background color of the window
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
    tk.Button(button_frame, text=button, width=9, height=3,bg="#79E5F2", command=action).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1
root.mainloop()
