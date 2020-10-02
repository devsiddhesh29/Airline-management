from tkinter import *
from tkinter import messagebox
# import re
# from PIL import Image, ImageTk
# from flight_ui.welcome import Welcome
from firebase import firebase
firebase=firebase.FirebaseApplication('https://flight-search-fadaf.firebaseio.com/',None)

class forget:
    def __init__(self, root):
        self.root = root
        self.root.title("Forget password")
        self.root.geometry("500x500")
        self.root.configure(bg='light blue')

        self.Username1 = Label(self.root, text="Username:", font=("Arial", 10, "bold"), bg="Yellow")
        self.Username1.place(x=20, y=200)

        self.txtUname = Entry(self.root, width=30,show="*", bg="light blue")
        self.txtUname.place(x=100, y=200)

        self.Username11 = Label(self.root, text="confirm password:", font=("Arial", 10, "bold"), bg="Yellow")
        self.Username11.place(x=20, y=260)

        self.txtUname1 = Entry(self.root, width=30, show="*", bg="light blue")
        self.txtUname1.place(x=180, y=260)


        self.lblpassword1= Label(self.root, text="Password:", font=("Arial", 10, "bold"), bg="Yellow")
        self.lblpassword1.place(x=20, y=230)

        self.txtpassword1 = Entry(self.root, width=30, show="*", bg="light blue")
        self.txtpassword1.place(x=100, y=230)

        self.lblpassword1a = Label(self.root, text="enter phno:", font=("Arial", 10, "bold"), bg="Yellow")
        self.lblpassword1a.place(x=20, y=290)

        self.txtpassword1a = Entry(self.root, width=30, bg="light blue")
        self.txtpassword1a.place(x=100, y=290)

        self.btnLogIn = Button(self.root, text="Log In", width=10, command=self.sid, bg="pink")
        self.btnLogIn.place(x=150, y=330)


    def sid(self):

        if (len(self.txtUname.get()) == 0):
            messagebox.showinfo("facility_Name", "enter username")
            return
        if (len(self.txtpassword1.get()) == 0):
            messagebox.showinfo("facility_Name", "Please enter password")
            return
    #
    # def sid(self):
    #
    #     result = firebase.get('/security/', None)
    #     flag = 0
    #     data1 = {"security":self.txtpassword1a.get()}
    #     for x, y in result.items():
    #         if data1 == y:
    #             flag = 1
    #             from flight_ui.login import Login
    #             self.root.destroy()
    #             # from flight_ui.login import Login
    #             self.root = Tk()
    #             app = Login(self.root)
    #             self.root.mainloop()
    #
    #     if flag == 0:
    #         messagebox.showerror("Invalid Info", "please enter valid Info")

        else:
            data = firebase.get('/security/', None)
            r = firebase.post('/Register/loginn', data)
            self.root.destroy()
            from flight_ui.login import Login
            self.root = Tk()
            app = Login(self.root)
            self.root.mainloop()
            return

# root = Tk()
# app =forget(root)
# root.mainloop()

