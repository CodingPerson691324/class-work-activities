from tkinter import *

root = Tk()
root.title('getting started with widgets')
root.geometry('400x300')

lbl1 = Label(text = 'full name', bg='#3895D3', fg='white')
lbl2 = Label(text = 'enter email id', bg = '#3895D3', fg = 'white')
lbl3 = Label(text = 'enter password', bg = '#3895D3', fg = 'white')

name_entry = Entry()
email_entry = Entry()
pass_entry = Entry(show='*')

def display():
    name = name_entry.get()
    greet = 'hey '+name
    message = '\ncongrats for your new account'
    textbox.insert(END, greet)
    textbox.insert(END, message)

textbox = Text(bg='#BEBEBE', fg='black')

btn = Button(text = "create account", command=display)

lbl1.pack()
name_entry.pack()
lbl2.pack()
email_entry.pack()
lbl3.pack()
pass_entry.pack()
btn.pack()
textbox.pack()

root.mainloop()