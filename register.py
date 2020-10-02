from tkinter import *
from tkinter import messagebox
import re
import shutil
import datetime
from PIL import Image, ImageTk
from tkinter import filedialog
from flight_ui.welcome import Welcome
from firebase import firebase
firebase=firebase.FirebaseApplication('https://flight-search-fadaf.firebaseio.com/',None)

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("500x500")
        self.root.configure(bg='light blue')

        im = Image.open("../images/wel.jpg")
        im = im.resize((700, 700), Image.ANTIALIAS)

        self.tkimage = ImageTk.PhotoImage(im)

        self.myvar = Label(self.root, image=self.tkimage)
        self.myvar.place(x=0, y=0)

        self.Name = Label(self.root, text="Name:", font=("Arial", 10, "italic"),bg="light yellow")
        self.Name.place(x=20, y=100)

        self.txtName = Entry(self.root, width=30,bg="light yellow")
        self.txtName.place(x=150, y=100)

        self.Username = Label(self.root, text="Username:", font=("Arial", 10, "italic"),bg="light yellow")
        self.Username.place(x=20, y=140)

        self.txtUname = Entry(self.root, width=30,bg="light yellow")
        self.txtUname.place(x=150, y=140)

        self.IM = Label(self.root, text="Select image:", font=("Arial", 10, "italic"), bg="light yellow")
        self.IM.place(x=20, y=30)

        self.Email = Label(self.root, text="Email:", font=("Arial", 10, "italic"),bg="light yellow")
        self.Email.place(x=20, y=180)

        self.txtEmail = Entry(self.root, width=30,bg="light yellow")
        self.txtEmail.place(x=150, y=180)
        E = self.txtEmail.get()

        self.Password = Label(self.root, text="Password:", font=("Arial", 10, "italic"),bg="light yellow")
        self.Password.place(x=20, y=220)

        self.txtpassword = Entry(self.root, width=30, show="*",bg="light yellow")
        self.txtpassword.place(x=150, y=220)

        self.Confirm = Label(self.root, text="Confirm Password:", font=("Arial", 10, "italic"),bg="light yellow")
        self.Confirm.place(x=20, y=260)

        self.txtCon = Entry(self.root, width=30, show="*",bg="light yellow")
        self.txtCon.place(x=150, y=260)

        self.phno = Label(self.root, text="Phono:", font=("Arial", 10, "italic"),bg="light yellow")
        self.phno.place(x=20, y=300)

        self.txtphno = Entry(self.root, width=30,bg="light yellow")
        self.txtphno.place(x=150, y=300)

        # self.phno1 = Label(self.root, text="Enter ur petname:", font=("Arial", 10, "italic"), bg="light yellow")
        # self.phno1.place(x=20, y=320)
        #
        # self.txtphno1 = Entry(self.root, width=30, bg="light yellow")
        # self.txtphno1.place(x=150, y=320)

        self.btnSign = Button(self.root, text="Sign in", width=10, command = self.save,bg="blue")
        self.btnSign.place(x=200, y=360)

        self.path = ""

        btnSelect = Button(self.root, text="Select Image",command= self.openfile)
        btnSelect.place(x=150, y=20)

        btnSave = Button(self.root, text="Save Image",command= self.save11)
        btnSave.place(x=250, y=20)

        self.frame = Frame(self.root, width = 50, height = 50 , bg="white")
        self.frame.place(x=350, y=30)



    def openfile(self):
        self.path = filedialog.askopenfilename(initialdir="/", title="select file",filetypes=(("png files","*.png"),("jpeg files", "*,jpg"),("all files","*.*")))

        im1 = Image.open(self.path)
        im1 = im1.resize((50, 50), Image.ANTIALIAS)


        tkimage = ImageTk.PhotoImage(im1)


        myvar = Label(self.frame, image = tkimage)
        myvar.image = tkimage
        myvar.pack()

    def save11(self):
        shutil.copyfile(self.path,"../images/dd/aa.png")
        messagebox.showinfo("test","msg")
    def check(self, E):
        Em = re.compile('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
        return Em.match(E)

    def checknum(self, N):
        Em1 = re.compile("(0/91)?[7-9][0-9]{9}")
        return Em1.match(N)

    def save(self):

        if (len(self.txtName.get()) == 0):
            messagebox.showerror("Name", "Please enter Name")
            return

        if (len(self.txtUname.get()) == 0):
            messagebox.showerror("Name", "Please enter Username")

            return
        if (not self.checknum(self.txtphno.get())):
            messagebox.showerror("num", "Please enter Valid Number")

        if (self.txtpassword.get() != self.txtCon.get()):
            messagebox.showerror("password", "Please confirm password")
            return

        if (not self.check(self.txtEmail.get())):
            messagebox.showerror("Email", "Please enter Valid Email")
            return

        if (len(self.txtpassword.get()) < 8):
            messagebox.showerror("password", "Password must be atlest 8 digit")
            return

        # if (len(self.txtphno1.get()) == 0):
        #     messagebox.showinfo("facility_Name", "Please enter password")



        else:
            shutil.copyfile(self.path, "../images/dd/"+self.txtName.get()+".png")
            data = {"uname":self.txtEmail.get(),"pass":self.txtpassword.get()}
            r = firebase.post('/Register/loginn', data)
            data1 = {"name": self.txtName.get(), "Username": self.txtUname.get(),"Phone_no":self.txtphno.get(),"Password":self.txtpassword.get(),"Email_Id":self.txtEmail.get(),"Confirm_Password":self.txtpassword.get(),"DP_Url":self.txtName.get()+".png"}
            r1 = firebase.post('/Register/', data1)
            data2 = {"security":  self.txtphno.get()}
            r = firebase.post('/security', data2)
            self.root.destroy()
            from flight_ui.login import Login
            self.root = Tk()
            app = Login(self.root)
            self.root.mainloop()