# from customtkinter import *
# root=CTk()
# root.title("CustomTkinter")
# root.geometry("400x200")
# my_button=CTkButton(root,text="Click me")
# my_button.grid(row=0,column=0)
# root.mainloop()


import customtkinter as ctk
ctk.set_appearance_mode("dark") # Modes : system(default),light,dark
ctk.set_default_color_theme("green") # Themes : blue(default),dark-blue,green
root=ctk.CTk()
root.geometry("400x200")
root.title("CustomTkinter")
my_button=ctk.CTkButton(root,text="Hello World!!!")
my_button.pack(pady=80)
root.mainloop()
