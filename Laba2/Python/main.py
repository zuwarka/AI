from tkinter import *

def max_min():
    n = int(EntryA.get())
    f = int(EntryB.get())

    EntryA.delete(0, END)
    EntryA.insert(0, n)
    EntryB.delete(0, END)
    EntryB.insert(0, f)
    root = Tk()
    root.title("Result")
    canvas_m = Canvas(root, width=350, height=100)
    canvas_m.pack()
    frame_m = Frame(root)
    frame_m.place(relx = 0.15, rely = 0.15, relheight = 0.7, relwidth = 0.7)

    if n < f:
        Label(
            frame_m,
            text = "The first num is less than the second"
        ).grid()
    elif n > f:
        Label(
            frame_m,
            text = "The first num is more than the second"
        ).grid()
    elif n == f:
        Label(
            frame_m,
            text = "The first num is equal to than the second"
        ).grid()

window = Tk()
window.title("Laba 3 AI")

canvas = Canvas(window, width = 300, height = 150)
canvas.pack()

frame = Frame(window)
frame.place(relx = 0.15, rely = 0.15, relheight = 0.7, relwidth = 0.7)

label1 = Label(frame, text = "Input fisrt num").grid(row = 0, sticky = W)
label2 = Label(frame, text = "Input second num").grid(row = 1, sticky = W)

EntryA = Entry(frame, width = 10, font = "Roboto 16")
EntryA.grid(row = 0, column = 1, sticky = E)
EntryB = Entry(frame, width = 10, font = "Roboto 16")
EntryB.grid(row = 1, column = 1, sticky = E)

res = Button(frame, text = "Result", command = max_min)
res.grid(row = 2, sticky = W)

window.mainloop()
