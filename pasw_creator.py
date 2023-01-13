from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox as msg
from tkinter.font import Font
import random


def count():
    entry.delete(0, END)
    lenght = var1.get()
    weak = "absdefghijklmnopqrstuvwxyz0123456789"
    medium = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    strong = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()?"
    password = ""
    if var.get() == 0:
        for i in range(0, lenght):
            password = password + random.choice(weak)
        return password
    if var.get() == 1:
        for i in range(0, lenght):
            password = password + random.choice(medium)
        return password
    if var.get() == 2:
        for i in range(0, lenght):
            password = password + random.choice(strong)
        return password

def generate_password():
    generate = count()
    entry.insert(0, generate)
 
def save():
    file_name = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Text", '.txt'),))
    if file_name:
        with open(file_name + '.txt', 'w') as file_object:
            file_object.write(entry.get())
    entry.delete(0, END)
    status['text'] = f'Password Saved To: {file_name}'
    popup()

def popup():                                 
   msg.showinfo("Info", "Password Saved")


window = Tk()
window.title("Password Generator")
window.geometry("400x400")
window.config(bg="#FCFFE7")
var = IntVar()
var1 = IntVar()

looks = Font(
    family = 'Helvetica',
    size = 20,
    weight = 'bold',
    slant = 'roman',
)
looks1 = Font(
    family = 'Helvetica',
    size = 14,
    weight = 'normal',
    slant = "italic",
    underline = 1,
)
looks2 = Font(
    family = 'Helvetica',
    size = 14,
    weight = 'bold',
)

choose = Label(window, text="CHOOSE PASSWORD TYPE", font=looks, border=10, bg="#FCFFE7", fg="#2B3467")
weak = Radiobutton(window, text="WEAK", variable=var, value=0, font=("Helvetica", 14), bg="#FCFFE7", fg="#2B3467")
medium = Radiobutton(window, text="MEDIUM", variable=var, value=1, font=("Helvetica", 14), bg="#FCFFE7", fg="#2B3467")
strong = Radiobutton(window, text="STRONG", variable=var, value=2, font=("Helvetica", 14), bg="#FCFFE7", fg="#2B3467")
l_lenght = Label(window, text="SELECT LENGTH", font=("Helvetica", 14), border=5, bg="#FCFFE7", fg="#2B3467")
choose_lenght = ttk.Combobox(window, textvariable=var1, width=2)
choose_lenght['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,17, 18, 19, 20, 21, 22, 23, 24, 25,26)
choose_lenght.current(0)
generate_button = Button(window, text="GENERATE", command=generate_password, font=looks, fg="#2B3467", highlightbackground ="#FCFFE7", bd=10)
entry= Entry(window, width=23, font=("Helvetica", 20), bg="#FCFFE7", fg="#2B3467")
save = Button(window, text="SAVE YOUR PASSWORD", command=save, border=10, font=looks2, bg="#FCFFE7", fg="#EB455F", highlightbackground ="#FCFFE7", bd=10)
status = Label(window, text="Recomended to create a STRONG password", border=10, font=looks1, bg="#FCFFE7", fg="#2B3467")

choose.grid(row=0, column=0)
weak.grid(row=1, column=0)
medium.grid(row=2, column=0)
strong.grid(row=3, column=0)
l_lenght.grid(row=4, column=0)
choose_lenght.grid(row=5, column=0)
generate_button.grid(row=6, column=0, padx=100)
entry.grid(row=7, column=0)
save.grid(row=8, column=0)
status.grid(row=9, column=0)
window.mainloop()