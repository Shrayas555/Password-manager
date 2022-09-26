from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# # ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password():


    input2.delete(0, 'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list=[random.choice(letters) for char in range(nr_letters)]


    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    input2.insert(END,f'{password}')
    pyperclip.copy(password)

# # ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=input.get()
    password=input2.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title='OOPS',message='Please check for empty field.')
    else:
        isok = messagebox.askokcancel(title=website,
                                      message=f'These are the details entered\n {website}:{password}\n is it okay to save?')
        if isok:

            with open('data.txt',mode='a') as file:
                file.write(f'{website}  |  {password}\n')
                input.delete(0,'end')
                input2.delete(0,'end')

# ---------------------------- UI SETUP ------------------------------- #




window=Tk()
window.title('Password Generator')
window.config(padx=50, pady=50)
canvas=Canvas(width=200,height=200)
a=PhotoImage(file='logo.png')
img=canvas.create_image(100,100,image=a)
canvas.grid(column=1,row=0)

web=Label(text='Website:')
web.grid(row=1,column=0)

input=Entry(width=35)
input.focus()
input.grid(column=1,row=1,columnspan=2)

email1=Label(text='EMAIL:')
email1.grid(row=2,column=0)

input1=Entry(width=35)
input1.insert(END,'shrayas@gmail.com')
input1.grid(column=1,row=2,columnspan=2)

pass1=Label(text='Password:')
pass1.grid(row=3,column=0)

input2=Entry(width=18)
input2.grid(column=1,row=3)

button=Button(text='Generate password',width=13,command=password)
button.grid(row=3,column=2)

button2=Button(width=33,text='ADD',command=save)

button2.grid(column=1,row=4,columnspan=2)


















window.mainloop()