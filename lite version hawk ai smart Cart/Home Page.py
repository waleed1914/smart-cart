import tkinter
from tkinter import *
from tkinter.font import Font

import customtkinter


def show_frame(frame):
    frame.tkraise()


root = customtkinter.CTk()
root.geometry("1366x768")
root.wm_attributes('-fullscreen', 'true')
# Define image


bg = PhotoImage(file="images/background - home.png")

my_canvas = Canvas(root, width=1366, height=768)
my_canvas.pack(fill="both", expand=True)

my_canvas.create_image(0, 0, image=bg, anchor="nw")


def button_function():
    print("button pressed")


total_amount = [100]
items_in_cart = [0]
unscanned_items = [0]
font_name = "Nunito"

unscanned_items_label = customtkinter.CTkLabel(master=root, text=f"Unscanned items: {sum(items_in_cart)}",
                                               text_color="#000000",
                                               text_font=(font_name, 20), bg_color="#ffffff")

unscanned_items_label.place(relx=0.842, rely=0.57, anchor=tkinter.CENTER)

items_in_cart_label = customtkinter.CTkLabel(master=root, text=f"Items in Cart: {sum(items_in_cart)}",
                                             text_color="#000000",
                                             text_font=(font_name, 20), bg_color="#ffffff")

items_in_cart_label.place(relx=0.862, rely=0.63, anchor=tkinter.CENTER)

total_label = customtkinter.CTkLabel(master=root, text=f"Total: {sum(total_amount)}", text_color="#000000",
                                     text_font=(font_name, 35), bg_color="#ffffff")

total_label.place(relx=0.86, rely=0.77, anchor=tkinter.CENTER)

# Use CTkButton instead of tkinter Button
payment_button = customtkinter.CTkButton(master=root, width=420,
                                         height=47,
                                         fg_color="#00FF65",
                                         bg_color="#ffffff",
                                         border_width=0,
                                         corner_radius=30, text="Proceed To Pay", command=button_function)
payment_button.place(relx=0.788, rely=0.85, anchor=tkinter.CENTER)

grocery_shift_button = customtkinter.CTkButton(master=root, width=420,
                                               height=47,
                                               fg_color="#79C4E4",
                                               bg_color="#D8E9F0",
                                               border_width=0,
                                               corner_radius=30, text="Shop Grocery", command=button_function)
grocery_shift_button.place(relx=0.78, rely=0.1, anchor=tkinter.CENTER)

root.mainloop()
