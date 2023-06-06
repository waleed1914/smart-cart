import tkinter
from tkinter import *
from PIL import ImageTk, Image

import customtkinter

root = Tk()
root.title('Codemy.com - Set Image as Background')
root.geometry("1366x768")
root.wm_attributes('-fullscreen', 'true')
# Define image
bg = PhotoImage(file="images/background - grocery.png")

my_canvas = Canvas(root, width=1366, height=768)
my_canvas.pack(fill="both", expand=True)

my_canvas.create_image(0, 0, image=bg, anchor="nw")

grocery_frame = customtkinter.CTkFrame(master=root,
                                       width=1174,
                                       height=560,
                                       bg_color="#ffffff",
                                       fg_color="#ffffff",
                                       corner_radius=46)

grocery_frame.place(relx=0.499, rely=0.54, anchor=tkinter.CENTER)
y_point = 0
x_point = 0
for single in range(8):
    image1 = Image.open("product images/tomato_.jpg")
    product_frame = customtkinter.CTkFrame(master=grocery_frame,
                                           width=230,
                                           height=250,
                                           bg_color="#ffffff",
                                           fg_color="#D8E9F0",
                                           corner_radius=35)

    product_frame.grid(row=x_point, column=y_point, padx=10, pady=10)
    if y_point == 3:
        y_point = 0
        x_point += 1
    else:
        y_point += 1

    image1 = image1.resize((100, 100), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image1)

    label1 = tkinter.Label(master=product_frame, image=test)
    label1.pack(pady=10)

    font_name = "Nunito"

    customtkinter.CTkLabel(master=product_frame, text=f"Product Name",
                           text_color="#000000",
                           text_font=(font_name, 20), bg_color="#D8E9F0").pack(pady=1)

    customtkinter.CTkLabel(master=product_frame, text=f"Price: 20$ Per Kg",
                           text_color="#000000",
                           text_font=(font_name, 13), bg_color="#D8E9F0").pack(pady=0)

    customtkinter.CTkButton(master=product_frame, width=200,
                            height=27,
                            fg_color="#00FF65",
                            bg_color="#D8E9F0",
                            border_width=0,
                            corner_radius=4, text="Buy Now").pack(pady=5)

    product_frame.pack_propagate(False)


def button_function():
    print("button pressed")


grocery_shift_button = customtkinter.CTkButton(master=root, width=420,
                                               height=47,
                                               fg_color="#79C4E4",
                                               bg_color="#D8E9F0",
                                               border_width=0,
                                               corner_radius=30, text="Back to Cart", command=button_function)
grocery_shift_button.place(relx=0.78, rely=0.1, anchor=tkinter.CENTER)

root.mainloop()
