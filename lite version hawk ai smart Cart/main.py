from tkinter import *
import customtkinter
import customtkinter


def show_frame(frame):
    frame.tkraise()


root = customtkinter.CTk()
# root.wm_attributes('-fullscreen', 'true')
root.state("zoomed")

welcome_screen = customtkinter.CTkFrame(root)

home_screen = customtkinter.CTkFrame(root)

bg = PhotoImage(file="images/background - welcome.png")
my_canvas = Canvas(welcome_screen, width=1366, height=368)
my_canvas.pack(fill="both", expand=True)
my_canvas.create_image(0, 0, image=bg, anchor="nw")

btn = customtkinter.CTkButton(master=welcome_screen, width=420,
                              height=47,
                              fg_color="#00FF65",
                              bg_color="#ffffff",
                              border_width=0,
                              corner_radius=30, text="Proceed To Pay", command=lambda: show_frame(home_screen))


btn_2 = customtkinter.CTkButton(master=home_screen, width=420,
                              height=47,
                              fg_color="#00FF65",
                              bg_color="#ffffff",
                              border_width=0,
                              corner_radius=30, text="Proceed To Pay", command=lambda: show_frame(welcome_screen))
btn_2.pack()
welcome_screen.grid(row=0, column=0, sticky="nsew")
home_screen.grid(row=0, column=0, sticky="nsew")
btn.pack()
show_frame(welcome_screen)
root.mainloop()
