import random
import threading
import time
import tkinter
from datetime import datetime, timedelta
from tkinter import *
from numpy import asarray
from tkinter.font import Font
from tkinter import messagebox, ttk
import customtkinter
from PIL import ImageTk, Image
import pygame
import pandas as pd

def welcome_audio():
    time.sleep(0.6)
    pygame.mixer.init()
    pygame.mixer.music.load("audio file/welcom-audio.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def create_toplevel(self, inside_text, btn_text):
    window = customtkinter.CTkToplevel(self, bg="#79C4E4")

    window.attributes('-topmost',True)
    window.geometry("400x200+425+225")
    window.overrideredirect(True)
    text1 = "Please Add your Belongings inside the Cart."
    # window.configure(text=text1)

    def close():
        window.destroy()

    frame = customtkinter.CTkFrame(master=window,
                                   width=700,
                                   height=200,
                                   fg_color="#D8E9F0",
                                   corner_radius=10)
    frame.pack(padx=20, pady=20)

    # create label on CTkToplevel window
    label = customtkinter.CTkLabel(frame, text=inside_text,text_color="black")
    label.pack(side="top", fill="both", expand=True, padx=40, pady=40)
    button = customtkinter.CTkButton(master=frame, width=140,
                                     height=50,
                                     fg_color="#00FF65",
                                     bg_color="#D8E9F0",
                                     border_width=0,
                                     corner_radius=20, text=btn_text, command=close)
    button.pack(pady=10)
    frame.pack_propagate(False)



audio_thread = threading.Thread(target=welcome_audio)
audio_thread.start()

from pyzbar import pyzbar
import cv2

total_unscanned_items = []
check = []
total = []
scan_or_not = []
img = Image.open('images/back.jpg')
numpydata = asarray(img)
global count
count = 0


def read_barcodes(frame):
    if len(check) == 0:
        barcodes = pyzbar.decode(frame)
        for barcode in barcodes:
            x, y, w, h = barcode.rect
            # 1
            barcode_info = barcode.data.decode('utf-8')
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # 2
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
            # 3

            import pandas as pd
            try:
                df = pd.read_csv("Product Details/product_details.csv")
                product_checker = list(df["Barcode"].values)
                print(product_checker)
                print(barcode_info)

                if str(barcode_info)[0] == "0":
                    barcode_info = str(barcode_info)[1:]
                try:
                    index = product_checker.index(f"{str(barcode_info)}")
                except:
                    index = product_checker.index(f"{barcode_info}")
                price = df["Price"][index]
                product = df["Product"][index]
                print("-----------------------------------")
                print(f"Product name: {product}")
                print(f"Product price: {price}")
                total.append(price)
                add_record(product, 1, round(price, 2))

                print(f"total price: {sum(total)} PKR")
                print("-----------------------------------")

                pygame.mixer.init()
                pygame.mixer.music.load("audio file/beep.wav")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)

                message = f"""
    Your PRODUCT is added
    Product name: {product}
    Product Price: {price}
    Total price: {round(sum(total), 2)}$
    Please Put Product into Cart
    """

                # scan_or_not.append(1)
                messagebox.showinfo("Thanks", message)
                create_toplevel(home_screen, message, "Continue")
                # nine_hours_from_now = datetime.now() + timedelta(seconds=3)
                # check.append(nine_hours_from_now)

                # scan_or_not.append(1)



            except Exception as e:
                print(e)
                pass
        return frame
    else:

        return numpydata


def show_frame(frame, file, what):
    if what is True:
        create_toplevel(home_screen, "Please Put your Belongings Inside the Cart", "Continue")
    frame.tkraise()
    bg.config(file=file)

root = customtkinter.CTk()
root.geometry("1266x768")
root.wm_attributes('-fullscreen', 'true')
# Define image
splash_screen = customtkinter.CTkFrame(root, width=1366, height=768)
home_screen = customtkinter.CTkFrame(root, width=1366, height=768)
grocery_screen = customtkinter.CTkFrame(root, width=1366, height=768)

bg = PhotoImage(file='images/background - home.png')
# bg = PhotoImage(file='images/background - grocery.png')


my_canvas = Canvas(home_screen, width=1366, height=768)
my_canvas_2 = Canvas(grocery_screen, width=1366, height=768)
my_canvas_3 = Canvas(splash_screen, width=1366, height=768)

my_canvas.pack(fill="both", expand=True)
my_canvas_2.pack(fill="both", expand=True)
my_canvas_3.pack(fill="both", expand=True)

my_canvas.create_image(0, 0, image=bg, anchor="nw")
my_canvas_2.create_image(0, 0, image=bg, anchor="nw")
my_canvas_3.create_image(0, 0, image=bg, anchor="nw")


def button_function():
    print("button pressed")


total_amount = [0.00]
items_in_cart = [0]
unscanned_items = [0]
font_name = "Nunito"

# unscanned_items_label = customtkinter.CTkLabel(master=home_screen, text=f"Unscanned items: {sum(items_in_cart)}",
#                                                text_color="#000000",
#                                                text_font=(font_name, 20), bg_color="#ffffff")

# unscanned_items_label.place(relx=0.842, rely=0.57, anchor=tkinter.CENTER)

items_in_cart_label = customtkinter.CTkLabel(master=home_screen, text=f"Items in Cart: {sum(items_in_cart)}",
                                             text_color="#000000",
                                             text_font=(font_name, 20), bg_color="#ffffff")

items_in_cart_label.place(relx=0.862, rely=0.63, anchor=tkinter.CENTER)

total_label = customtkinter.CTkLabel(master=home_screen, text=f"Total: {round(sum(total_amount), 2)}$",
                                     text_color="#000000",
                                     text_font=(font_name, 35), bg_color="#ffffff")

total_label.place(relx=0.8, rely=0.77, anchor=tkinter.CENTER)

# -------------------------------------------------------------------------------------------------
cap = cv2.VideoCapture(0)

new_man = Label(home_screen, height=250, width=420)
item = my_canvas.create_window(670, 165, anchor="nw", window=new_man)
new_man.place(relx=0.627, rely=0.2)

from PIL import ImageTk, Image


def video_stream():
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    new_man.imgtk = imgtk
    # my_canvas.itemconfig(item,)
    new_man.configure(image=imgtk)
    read_barcodes(frame)
    # if len(check) > 0 and datetime.now() >= check[0]:
    #        check.clear()
    # lmain.imgtk = imgtk
    # lmain.configure(image=imgtk)
    new_man.after(1, video_stream)
    # lmain.after(1, video_stream)


# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------

style = ttk.Style()

style.configure("Treeview",
                background="#ffffff",
                foreground="#000000",
                rowheight=33,
                fieldbackground="#ffffff",
                font=('Nunito', 12)

                )
style.configure("Treeview.Heading", font=('Nunito', 14, 'bold'))
# Change selected color
style.map('Treeview',
          background=[('selected', '#00FF65')],
          foreground=[('selected', '#000000')])

# Create Treeview Frame
tree_frame = Frame(home_screen)
start = [165]

my_canvas.create_window(50, sum(start), anchor="nw", window=tree_frame)
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Configure The Canvas
tv = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended", height=13)

tv['columns'] = ('Product Name', 'Amount', 'Price')
tv.column('#0', width=0, stretch=NO)
tv.column('Product Name', anchor=CENTER, width=220)
tv.column('Amount', anchor=CENTER, width=200)
tv.column('Price', anchor=CENTER, width=190)

tv.heading('#0', text='', anchor=CENTER)
tv.heading('Product Name', text='Product Name', anchor=CENTER)
tv.heading('Amount', text='Amount', anchor=CENTER)
tv.heading('Price', text='Price', anchor=CENTER)

"""tv.insert(parent='', index=1, iid=1, text='', values=('2', 'Anil', 'Bravo'))
tv.insert(parent='', index=2, iid=2, text='', values=('3', 'Vinod', 'Charlie'))
tv.insert(parent='', index=3, iid=3, text='', values=('4', 'Vimal', 'Delta'))
tv.insert(parent='', index=4, iid=4, text='', values=('5', 'Manjeet', 'Echo'))
"""
tv.pack()
tree_scroll.config(command=tv.yview)
tree_frame.place(relx=0.08, rely=0.2)

################ BUTTONS
################ BUTTONS
# ----
def add_one():
    selected = tv.selection()[0]
    values = list(tv.item(selected)["values"])
    product_name = values[0]
    product_amount = int(values[1])
    product_selected_price = float(values[2])
    df = pd.read_csv("Product Details/product_details.csv")
    product_checker = list(df["Product"].values)
    index = product_checker.index(str(product_name))
    product_price = df["Price"][index]

    print(product_name)
    new_price = product_selected_price + float(product_price)
    check = tv.item(selected, values=(product_name, product_amount + 1, new_price))

    total_bill_price = []
    a = tv.get_children()
    for single in range(len(a)):
        b = float(list(tv.item(a[single])["values"])[2])
        print(b)
        total_bill_price.append(b)

    total_label.config(text=f"Total:  {round(sum(total_bill_price), 2)}$")
    total.clear()
    total.append(round(sum(total_bill_price), 2))

    print(check)

def remove_one():
    if len(total_amount) > 0:
        selected = tv.selection()[0]
        values = list(tv.item(selected)["values"])
        product_name = values[0]

        amount = int(values[1])
        if int(amount) > 1:
            print(product_name)
            MsgBox = messagebox.askquestion('Remove Product', 'Are you sure you want to remove product amount by 1?',
                                            icon='warning')

            if MsgBox == 'yes':
                print(selected)
                print(selected[0])

                price = round(float(values[2]), 2)
                amount = int(values[1])
                df = pd.read_csv("Product Details/product_details.csv")
                product_checker = list(df["Product"].values)
                index = product_checker.index(str(product_name))
                product_price = df["Price"][index]
                print(amount)

                tv.delete(selected)
                global count
                if int(amount) > 1:
                    if count % 2 == 0:
                        tv.insert(parent='', index=0, iid=count, text="",
                                  values=(product_name, amount - 1, round(price - float(product_price), 2)))
                    else:

                        tv.insert(parent='', index=0, iid=count, text="",
                                  values=(product_name, amount - 1, round(price - float(product_price), 2)))
                count += 1
                total_bill_price = []
                a = tv.get_children()
                for single in range(len(a)):
                    b = float(list(tv.item(a[single])["values"])[2])
                    total_bill_price.append(b)

                total_label.config(text=f"Total:  {round(sum(total_bill_price), 2)}$")
                total.clear()
                total.append(round(sum(total_bill_price), 2))
            else:
                pass


def delete_one():
    if len(total_amount) > 0:
        selected = tv.selection()[0]
        values = list(tv.item(selected)["values"])
        product_name = values[0]

        amount = int(values[1])
        if int(amount) == 1:
            print(product_name)
            MsgBox = messagebox.askquestion('Remove Product', 'Are you sure you want to remove product amount by 1?',
                                            icon='warning')

            if MsgBox == 'yes':
                print(selected)
                print(selected[0])

                price = round(float(values[2]), 2)
                amount = int(values[1])
                df = pd.read_csv("Product Details/product_details.csv")
                product_checker = list(df["Product"].values)
                index = product_checker.index(str(product_name))
                product_price = df["Price"][index]
                print(amount)

                tv.delete(selected)
                global count
                if int(amount) > 1:
                    if count % 2 == 0:
                        tv.insert(parent='', index=0, iid=count, text="",
                                  values=(product_name, amount - 1, round(price - float(product_price), 2)))
                    else:

                        tv.insert(parent='', index=0, iid=count, text="",
                                  values=(product_name, amount - 1, round(price - float(product_price), 2)))
                count += 1
                total_bill_price = []
                a = tv.get_children()
                for single in range(len(a)):
                    b = float(list(tv.item(a[single])["values"])[2])
                    total_bill_price.append(b)

                total_label.config(text=f"Total:  {round(sum(total_bill_price), 2)}$")
                total.clear()
                total.append(round(sum(total_bill_price), 2))
            else:
                pass

# ----


add = customtkinter.CTkButton(master=home_screen, width=120,
                              height=47,
                              fg_color="#00FF65",
                              bg_color="#ffffff",
                              border_width=0,
                              text="ADD",
                              text_color="black",
                              command=add_one
                              )

add.place(relx=0.08, rely=0.8)

minus = customtkinter.CTkButton(master=home_screen, width=120,
                                height=47,
                                fg_color="#CBC3E3",
                                bg_color="#ffffff",
                                border_width=0,
                                text="REMOVE",
                                text_color="black",
                                command=remove_one
                                )

minus.place(relx=0.200, rely=0.8)

apply_code = customtkinter.CTkButton(master=home_screen, width=120,
                                     height=47,
                                     fg_color="#FFFF66",
                                     bg_color="#ffffff",
                                     border_width=0,
                                     text_color="black",
                                     text="COUPON CODE"
                                     )

apply_code.place(relx=0.320, rely=0.8)

delete = customtkinter.CTkButton(master=home_screen, width=120,
                                 height=47,
                                 fg_color="#FF7F7F",
                                 bg_color="#ffffff",
                                 border_width=0,
                                 text="DELETE",
                                 text_color="black",
                                 command=delete_one
                                 )

delete.place(relx=0.440, rely=0.8)
video_stream()
################


"""
start = [165]

my_canvas.create_window(50, sum(start), anchor="nw", window=tree_frame)
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create Treeview
tv = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
tv.pack()

tree_scroll.config(command=tv.yview)

# Define Our Columns
tv['columns'] = ("Name", "ID", "Favorite Pizza")
tv.column("#0", width=0, stretch=NO)
tv.column("Name", anchor=W, width=240)
tv.column("ID", anchor=CENTER, width=150)
tv.column("Favorite Pizza", anchor=W, width=200)

tv.heading("#0", text="", anchor=W)
tv.heading("Name", text="Name", anchor=W)
tv.heading("ID", text="Amount", anchor=CENTER)
tv.heading("Favorite Pizza", text="Product Price", anchor=W)
tv.insert(parent='', index=0, iid=0, values=("vineet", "e11", 1000000.00))
tree_frame.place(relx=0.08, rely=0.2)
"""


def add_record(name, amount, price):
    global count
    check = []
    price = round(price, 2)

    try:
        a = tv.get_children()
        for single in range(len(a)):
            b = tv.item(a[single])["values"]
            if str(name) in str(b):
                check.append(1)
                # print("------------------------------------------------")
                # print("Sorry")
                x = a[single]
                tv.delete(x)

                if count % 2 == 0:
                    tv.insert(parent='', index='end', text=f'{count + 1}',
                              values=(name, int(list(b)[1]) + 1, float(list(b)[2]) + float(price)),
                              )
                else:
                    tv.insert(parent='', index='end', text=f'{count + 1}',
                              values=(name, int(list(b)[1]) + 1, float(list(b)[2]) + float(price)),
                              )

                    print("------------------------------------------------")

    except Exception as e:
        pass
    if len(check) == 0:
        if count % 2 == 0:
            tv.insert(parent='', index='end', iid=count, text="",
                      values=(name, amount, price), )
        else:
            tv.insert(parent='', index='end', iid=count, text="",
                      values=(name, amount, price), )

        count += 1
    total_bill_price = []
    a = tv.get_children()
    for single in range(len(a)):
        b = float(list(tv.item(a[single])["values"])[2])
        total_bill_price.append(b)

    total_label.config(text=f"Total: {round(sum(total_bill_price), 2)}$")


# -----------------------------------------------------------------

# -------------------------------------------------------------------------------------------------

def payment_details():
    messagebox.showinfo("showinfo", "Information")


# Use CTkButton instead of tkinter Button
payment_button = customtkinter.CTkButton(master=home_screen, width=350,
                                         height=47,
                                         text_color="black",   
                                         fg_color="#00FF65",
                                         bg_color="#ffffff",
                                         border_width=0,

                                         corner_radius=30, text="Proceed To Pay", command=payment_details)
payment_button.place(relx=0.788, rely=0.85, anchor=tkinter.CENTER)

grocery_shift_button_2 = customtkinter.CTkButton(master=grocery_screen, width=420,
                                                 height=47,
                                                 fg_color="#79C4E4",
                                                 bg_color="#D8E9F0",
                                                 border_width=0,
                                                 corner_radius=30, text="Back to Cart",
                                                 command=lambda: show_frame(home_screen,
                                                                            'images/background - home.png', False))
grocery_shift_button_2.place(relx=0.78, rely=0.1, anchor=tkinter.CENTER)

grocery_frame = customtkinter.CTkFrame(master=grocery_screen,
                                       width=1174,
                                       height=530,
                                       bg_color="#ffffff",
                                       fg_color="#ffffff",
                                       corner_radius=46)
from PIL import ImageTk, Image

grocery_frame.place(relx=0.499, rely=0.54, anchor=tkinter.CENTER)
y_point = 0
x_point = 0
image1 = Image.open("product images/tomato_.jpg")
for single in range(8):
    product_frame = customtkinter.CTkFrame(master=grocery_frame,
                                           width=220,
                                           height=200,
                                           bg_color="#ffffff",
                                           fg_color="#D8E9F0",
                                           corner_radius=25)

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
    random_price = random.randint(10, 200)

    customtkinter.CTkLabel(master=product_frame, text=f"Price: {random_price}$ Per Kg",
                           text_color="#000000",
                           text_font=(font_name, 13), bg_color="#D8E9F0").pack(pady=0)

    customtkinter.CTkButton(master=product_frame, width=200,
                            height=27,
                            fg_color="#00FF65",
                            bg_color="#D8E9F0",
                            border_width=0,
                            corner_radius=4, text="Buy Now").pack(pady=5)

    product_frame.pack_propagate(False)

grocery_shift_button = customtkinter.CTkButton(master=home_screen, width=420,
                                               height=47,
                                               fg_color="#79C4E4",
                                               bg_color="#D8E9F0",
                                               border_width=0,
                                               corner_radius=30, text="Shop Grocery",
                                               command=lambda: show_frame(grocery_screen,
                                                                          'images/background - grocery.png', False))
grocery_shift_button.place(relx=0.78, rely=0.1, anchor=tkinter.CENTER)
splash_screen.grid(row=0, column=0, sticky="nsew")
home_screen.grid(row=0, column=0, sticky="nsew")
grocery_screen.grid(row=0, column=0, sticky="nsew")

show_frame(splash_screen, 'images/background - welcome.png', False)


def change_background():
    #create_toplevel(home_screen, "Please Put your Belongings Inside the Cart", "Continue")
    show_frame(home_screen, 'images/background - home.png', True)


splash_screen.after(2000, func=change_background)



root.mainloop()
