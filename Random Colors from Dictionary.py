from tkinter import *
import random

root=Tk()
root.title("Random Color Generator")
root.geometry("400x400")

dictionary = {"Colors": ["OliveDrab2", "gainsboro", "MediumOrchid3", "cornsilk2", "khaki", "tomato", "grey87", 
                         "blanched almond", "papaya whip", "lemon chiffon", "indian red", "NavajoWhite2"]}

btn = Button(root, text = "Click Me", command = "change", bg = "white")
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

label = Label(root, text = "", bg = "white")
label.place(relx = 0.5, rely = 0.6, anchor = CENTER)

def change():
    random1 = random.randint(0,11)
    dictionary.get["Colors"][random1]
    root.configure(backgound = random1)
    label["text"] = str(random1)

root.mainloop()