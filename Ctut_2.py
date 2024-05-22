import customtkinter as ctk
root=ctk.CTk()

def hello():
    my_label.configure(text=my_button.cget("text"))

ctk.set_appearance_mode("dark") # Modes : system(default),light,dark
ctk.set_default_color_theme("blue") # Themes : blue(default),dark-blue,green
root.geometry("400x400")
root.title("Buttons")

# by default border_color is "grey"
# by default state is "normal"

my_button=ctk.CTkButton(root,
                        text="Hello World!!!",
                        command=hello,
                        height=100,
                        width=200,
                        font=("Helvetica",24,"bold"),
                        text_color="black",
                        fg_color="red",
                        hover_color="green",
                        corner_radius=50,
                        bg_color="white",
                        border_width=10,
                        border_color="yellow",
                        state="disabled")
my_button.pack(pady=80)

my_label=ctk.CTkLabel(root,text="")
my_label.pack(pady=20)


root.mainloop()