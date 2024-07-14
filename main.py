from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import pygame
from PIL import Image, ImageTk
import PIL


pygame.mixer.init()

root = Tk()
root.title("PNG to JPEG Converter by Samuel")
root.geometry("500x500")
root.config(bg="#116562")

path_file = None

def sound1():
    pygame.mixer.music.load("sfx/sound1.mp3")
    pygame.mixer.music.play()

def sound2():
    pygame.mixer.music.load("sfx/sound2.mp3")
    pygame.mixer.music.play()

def sound3():
    pygame.mixer.music.load("sfx/sound3.mp3")
    pygame.mixer.music.play()

def sound4():
    pygame.mixer.music.load("sfx/sound4.mp3")
    pygame.mixer.music.play()

def sound5():
    pygame.mixer.music.load("sfx/sound5.mp3")
    pygame.mixer.music.play()

def file_browser():
    global path_file
    sound2()
    rep = filedialog.askopenfilenames(parent=root, filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("All files", "*")])
    if rep:
        path_file = rep[0]
        label2.configure(text=path_file.split("/")[-1])
        label3.configure(text="")
        with Image.open(path_file) as pic:
            pic = pic.resize((130, 130), Image.LANCZOS)
            pic = ImageTk.PhotoImage(pic)
        canvas.create_image(72, 72, image=pic)
        canvas.image = pic
        sound5()
       
def file_converter():
    global path_file
    if path_file is not None:
        with Image.open(path_file) as image:
            name = path_file.split("/")[-1]
            proper_name = name.split(".")[-2]
            image = image.convert('RGB')
            image.save("converted/" + proper_name + "_converted.jpg")
        label3.configure(text="Image successfully converted!", fg="orange", font=(None, 19))
        sound3()
    else:
        label3.configure(text="Please, select file!", fg="red", font=(None, 19))
        sound4()

def toggle():
    if toggle_button.config('text')[-1] == 'Dark Theme is On':
        toggle_button.config(text='Dark Theme is Off')
        root.config(bg="#116562")
        label.config(bg="#116562", fg="orange")
        label2.config(bg="#116562", fg="orange")
        label3.config(bg="#116562")
        toggle_button.config(bg="orange")
        btn1.config(bg="orange")
        btn2.config(bg="orange")
        container1.config(bg="#116562")
        canvas.configure(bg="white")
        sound1()
    else:
        toggle_button.config(text='Dark Theme is On')
        root.config(bg="#2F2F4F")
        label.config(bg="#2F2F4F", fg="orange")
        label2.config(bg="#2F2F4F", fg="orange")
        label3.config(bg="#2F2F4F")
        toggle_button.config(bg="orange")
        btn1.config(bg="orange")
        btn2.config(bg="orange")
        container1.config(bg="#2F2F4F")
        canvas.configure(bg="grey")
        sound1()


container1 = Frame(root, bg="#116562")
toggle_button = Button(text="Dark Theme is Off", bg="orange", command=toggle, borderwidth=5)
toggle_button.pack(in_=container1, side=RIGHT)
label = Label(text="Select Image", bg="#116562", fg="orange", font="bold")
label.pack(in_=container1, side=LEFT, padx=7)
container1.pack(side=TOP, fill=X)

btn1 = Button(text="Open files", command=file_browser, bg="orange", bd=5, borderwidth=5, width=8, height=1, font="bold")
btn1.pack(anchor=NW, padx=10, pady=10)
canvas = Canvas(width=140, height=140)
canvas.pack(pady=10)
label2 = Label(bg="#116562", fg="orange", width=15, height=2, font="bold")
label2.pack()
btn2 = Button(text="Convert", command=file_converter, bg="orange", bd=5, borderwidth=5, width=8, height=1, font="bold")
btn2.pack(anchor=NW, padx=10, pady=20)
label3 = Label(bg="#116562", fg="orange", width=25, height=2, font="bold")
label3.pack(pady=5)

root.mainloop()
