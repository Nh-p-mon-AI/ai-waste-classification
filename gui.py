from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.geometry('1000x500')
root.resizable(width=0, height=0)
root.title("Garbage classification")

myLabel = Label(root, image=None)
myLabel.pack(pady=30)

myResult = Label(root, text=None, fg="#000")
myResult.pack(side=BOTTOM, pady=50)


def chooseImage():
    global myLabel
    global path
    path = filedialog.askopenfilename(
        filetypes=[("Image File", '.jpg', ".png")])
    if path:
        image = Image.open(path).resize([600, 300])
        tkimage = ImageTk.PhotoImage(image)
        myLabel.config(image=tkimage)
        myLabel.image = tkimage


def resultImage():
    global myResult
    # YOUR CODE
    if path:
        myText = "THIS IS A PHOTO"
        myResult.config(text=myText, fg="blue")
        myResult.text = myText


chooseImageButton = Button(
    root, text="CHOOSE IMAGE", command=chooseImage, pady=20, padx=40, borderwidth=4
).place(x=80, y=400)

resultGarbageButton = Button(
    root, text="RESULT", command=resultImage, pady=20, padx=40, borderwidth=4
).place(x=800, y=400)

root.mainloop()
