import random
import string
from tkinter import Tk, Label, Button, Entry

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_button_click():
    password_length = int(length_entry.get())
    password = generate_password(password_length)
    password_label.config(text="Generated Password: " + password)

root = Tk()
root.title("Random Password Generator")
root.geometry("300x200")

length_label = Label(root, text="Password Length:")
length_label.pack(pady=10)

length_entry = Entry(root)
length_entry.pack(pady=5)

generate_button = Button(root, text="Generate Password", command=generate_button_click)
generate_button.pack(pady=10)

password_label = Label(root, text="")
password_label.pack()

root.mainloop()
