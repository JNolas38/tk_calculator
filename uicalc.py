import tkinter as tk

sheet = "0"
memory = ""

def update_sheet (symbol):
    global sheet
    if sheet == "0":
        delete_char()
    sheet += str(symbol)
    screen.delete(1.0, "end") #deletes everything on the screen
    screen.insert(1.0, sheet) #add current sheet to the screen

def eval_sheet():
    global sheet
    try:
        sheet = str(eval(sheet))
        screen.delete(1.0, "end")
        screen.insert(1.0, sheet)
    except:
        screen.delete(1.0, "end")
        screen.insert(1.0, "Math Error")
        sheet="0"


def delete_char():
    global sheet
    sheet = sheet[:-1]
    if sheet == "":
        sheet = "0"
    screen.delete(1.0, "end")
    screen.insert(1.0, sheet)

def clear_all ():
    global sheet
    sheet = "0"
    screen.delete(1.0, "end")
    screen.insert(1.0, sheet)

def call_memory ():
    global sheet
    global memory
    if memory == "":
        memory = sheet
    else:
        update_sheet(memory)
        memory = ""


root = tk.Tk() #creates object
root.configure(bg="blue")


root.geometry("293x268") #defines object size

screen = tk.Text(root, height=1, width=16, font=("Arial", 24)) #creates the textbox
screen.grid(columnspan=5) #specifies where the screen will be

#buttons
btn_1 =tk.Button(root, text="1", command=lambda: update_sheet(1), width=5, font=("Arial", 14), activebackground="black", activeforeground="white")
btn_1.grid(row=2, column=1, pady=3)
btn_2 =tk.Button(root, text="2", command=lambda: update_sheet(2), width=5, font=("Arial", 14), activebackground="black", activeforeground="white")
btn_2.grid(row=2, column=2)
btn_3 =tk.Button(root, text="3", command=lambda: update_sheet(3), width=5, font=("Arial", 14), activebackground="black", activeforeground="white")
btn_3.grid(row=2, column=3)
btn_4 =tk.Button(root, text="4", command=lambda: update_sheet(4), width=5, font=("Arial", 14), activebackground="black", activeforeground="white")
btn_4.grid(row=3, column=1, pady=3)
btn_5 =tk.Button(root, text="5", command=lambda: update_sheet(5), width=5, font=("Arial", 14), activebackground="black", activeforeground="white")
btn_5.grid(row=3, column=2)
btn_6 =tk.Button(root, text="6", command=lambda: update_sheet(6), width=5, font=("Arial", 14), activebackground="black", activeforeground="white")
btn_6.grid(row=3, column=3)
btn_7 =tk.Button(root, text="7", command=lambda: update_sheet(7), width=5, font=("Arial", 14), activebackground="black", activeforeground="white")
btn_7.grid(row=4, column=1, pady=3)
btn_8 =tk.Button(root, text="8", command=lambda: update_sheet(8), width=5, font=("Arial", 14), activebackground="black", activeforeground="white")
btn_8.grid(row=4, column=2)
btn_9 =tk.Button(root, text="9", command=lambda: update_sheet(9), width=5, font=("Arial", 14), activebackground="black", activeforeground="white")
btn_9.grid(row=4, column=3)
btn_0 =tk.Button(root, text="0", command=lambda: update_sheet(0), width=5, font=("Arial", 14), activebackground="black", activeforeground="white")
btn_0.grid(row=5, column=2)
btn_plus =tk.Button(root, text="+", command=lambda: update_sheet("+"), width=5, font=("Arial", 14), activebackground="black", activeforeground="white")
btn_plus.grid(row=2, column=4)
btn_minus =tk.Button(root, text="-", command=lambda: update_sheet("-"), width=5, font=("Arial", 14), activebackground="black", activeforeground="white")
btn_minus.grid(row=3, column=4)
btn_mult =tk.Button(root, text="x", command=lambda: update_sheet("*"), width=5, font=("Arial", 14), activebackground="black", activeforeground="white")
btn_mult.grid(row=4, column=4)
btn_div =tk.Button(root, text="/", command=lambda: update_sheet("/"), width=5, font=("Arial", 14), activebackground="black", activeforeground="white")
btn_div.grid(row=5, column=4)
btn_open =tk.Button(root, text="(", command=lambda: update_sheet("("), width=5, font=("Arial", 14), activebackground="black", activeforeground="white")
btn_open.grid(row=5, column=1, pady=3)
btn_close =tk.Button(root, text=")", command=lambda: update_sheet(")"), width=5, font=("Arial", 14), activebackground="black", activeforeground="white")
btn_close.grid(row=5, column=3)
btn_equals =tk.Button(root, text="=", command= eval_sheet, width=5, font=("Arial", 14), activebackground="black", activeforeground="white")
btn_equals.grid(row=6, column=1)
btn_mem =tk.Button(root, text="M", command= call_memory, width=5, font=("Arial", 14), bg="black", fg="white")
btn_mem.grid(row=6, column=2)
btn_del =tk.Button(root, text="DEL", command= delete_char, width=5, font=("Arial", 14), bg="red", fg="white", activebackground="red")
btn_del.grid(row=6, column=3)
btn_ac =tk.Button(root, text="AC", command= clear_all, width=5, font=("Arial", 14), bg="red", fg="white", activebackground="red")
btn_ac.grid(row=6, column=4)

screen.insert(1.0, sheet)
root.mainloop() #runs main loop