import time
from tkinter import *
import threading

import pygame

root = Tk()
root.title('Codemy.com - Set Image as Background')
root.geometry("1366x768")
root.wm_attributes('-fullscreen', 'true')
# Define image
bg = PhotoImage(file="images/background - welcome.png")

my_canvas = Canvas(root, width=1366, height=768)
my_canvas.pack(fill="both", expand=True)

my_canvas.create_image(0, 0, image=bg, anchor="nw")


def welcome_audio():
    time.sleep(0.1)
    pygame.mixer.init()
    pygame.mixer.music.load("audio file/welcom-audio.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


audio_thread = threading.Thread(target=welcome_audio)
audio_thread.start()

root.mainloop()
