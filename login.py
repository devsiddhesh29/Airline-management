from flight_ui.welcome import *
from flight_ui.register import *
# from flight_ui.forgetpass import *
from PIL import Image, ImageTk
from firebase import firebase

firebase=firebase.FirebaseApplication('https://flight-search-fadaf.firebaseio.com/',None)


class Login:
    def __init__(self, win):
        self.root = win
        self.root.title("Login")
        self.root.geometry("500x500")
        self.root.configure(bg='light green')

        im = Image.open("../images/hi.png")
        im = im.resize((500, 500), Image.ANTIALIAS)
        self.tkimage = ImageTk.PhotoImage(im)
        self.myvar = tk.Label(self.root, image=self.tkimage)
        self.myvar.place(x=0, y=0)

        # im1 = Image.open("../images/aa.png")
        # im1 = im1.resize((500, 500), Image.ANTIALIAS)
        # self.tkimage = ImageTk.PhotoImage(im1)
        # self.myvar1 = tk.Label(self.root, image=self.tkimage)
        # self.myvar1.place(x=0, y=0)

        self.Username1 = Label(self.root, text="Username:", font=("Arial", 10, "bold"),bg = "Yellow")
        self.Username1.place(x=20, y=200)

        self.txtUname = Entry(self.root, width=30,bg = "light blue")
        self.txtUname.place(x=100, y=200)

        self.lblpassword = Label(self.root, text="Password:", font=("Arial", 10, "bold"),bg = "Yellow")
        self.lblpassword.place(x=20, y=230)

        self.txtpassword = Entry(self.root, width=30, show="*",bg = "light blue")
        self.txtpassword.place(x=100, y=230)

        self.btnLogIn = Button(self.root, text="Log In", width=10, command=self.login,bg="pink")
        self.btnLogIn.place(x=150, y=260)

        self.forg = Button(self.root, text="Forget password", width=20, command=self.msg, bg="pink")
        self.forg.place(x=150, y=360)

        self.btnSignIn = Button(self.root, text="Sign In", width=10, command=self.register1,bg="pink")
        self.btnSignIn.place(x=150, y=300)
        self.root.mainloop()

    def login(self):

        result = firebase.get('Register/loginn/', None)
        flag = 0
        data = {"uname":self.txtUname.get(), "pass":self.txtpassword.get()}
        for x,y in result.items():
            if data == y:
                flag = 1
                self.root.destroy()
                self.root = tk.Tk()
                app = Welcome(self.root)
                self.root.mainloop()

        if flag==0:
            messagebox.showerror("Invalid Info","please enter valid Info")
        else:
            self.root.destroy()
            self.root = tk.Tk()
            app = Welcome(self.root)
            self.root.mainloop()


    def msg(self):
        # result =firebase.get('/security/', None)
        # flag = 0
        # data1 ={"secu"}
        self.root.destroy()
        from flight_ui.forgetpass import forget
        self.root = Tk()
        app = forget(self.root)
        self.root.mainloop()
        #messagebox.showerror("Invalid Info", "please enter valid Info")


    def register1(self):
        self.root.destroy()
        self.root = tk.Tk()
        signin = Register(self.root)
        self.root.mainloop()


tkwin = Tk()
obj1 = Login(tkwin)


