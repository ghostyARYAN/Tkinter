from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("640x360")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 360,
    width = 640,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 354, y = 273,
    width = 200,
    height = 50)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    454.0, 235.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#d4ecdd",
    highlightthickness = 0)

entry0.place(
    x = 329, y = 220,
    width = 250,
    height = 28)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    454.0, 119.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#d4ecdd",
    highlightthickness = 0)

entry1.place(
    x = 329, y = 104,
    width = 250,
    height = 28)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    454.0, 177.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#d4ecdd",
    highlightthickness = 0)

entry2.place(
    x = 329, y = 162,
    width = 250,
    height = 28)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    454.0, 57.0,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#d4ecdd",
    highlightthickness = 0)

entry3.place(
    x = 329, y = 42,
    width = 250,
    height = 28)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    248.5, 176.0,
    image=background_img)

window.resizable(False, False)
window.mainloop()
