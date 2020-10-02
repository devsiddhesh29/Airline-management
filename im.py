import datetime
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import shutil
from firebase import firebase
firebase=firebase.FirebaseApplication('https://flight-search-fadaf.firebaseio.com/',None)

class SelectImage:
    def __init__(self, master):
        self.master = master
        self.master.geometry("600x500")
        self.master.title("select Imaege")

        self.path = ""

        btnSelect = tk.Button(self.master, text="Select Image",command= self.openfile)
        btnSelect.place(x=30, y=20)

        btnSave = tk.Button(self.master, text="Select Image",command= self.save)
        btnSave.place(x=140, y=20)

        self.frame = tk.Frame(self.master, width = 250, height = 250 , bg="white")
        self.frame.place(x=30, y=60)

        self.master.mainloop()

    def openfile(self):
        self.path = tk.filedialog.askopenfilename(initialdir="/", title="select file",filetypes=(("png files","*.png"),("jpeg files", "*,jpg"),("all files","*.*")))

        im1 = Image.open(self.path)
        im1 = im1.resize((250, 250), Image.ANTIALIAS)


        tkimage = ImageTk.PhotoImage(im1)


        myvar = tk.Label(self.frame, image = tkimage)
        myvar.image = tkimage
        myvar.pack()

    def save(self):
        shutil.copyfile(self.path,"../images/dd/aa.png")
        messagebox.showinfo("test","msg")

root =tk.Tk()
im1 = SelectImage(root)


