from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from firebase import firebase
firebase=firebase.FirebaseApplication('https://flight-search-fadaf.firebaseio.com/',None)

class airline1:
    def __init__ (self, master):
        self.root = master
        self.root.title("Airline")
        self.root.geometry("500x500")
        self.root.configure(bg='light green')

        im = Image.open("../images/p.jpg")
        im = im.resize((500, 500), Image.ANTIALIAS)

        self.tkimage = ImageTk.PhotoImage(im)

        self.myvar = Label(self.root, image=self.tkimage)
        self.myvar.place(x=0, y=0)

        self.Name = Label(self.root, text="Airline name:", font=("Comic Sans MS", 10, "italic"))
        self.Name.place(x=20, y=30)

        self.txtfName = Entry(self.root, width=30)
        self.txtfName.place(x=150, y=30)

        self.Username = Label(self.root, text= "Airline price:", font=("Comic Sans MS", 10, "italic"))
        self.Username.place(x=20, y=80)

        self.txtfprice = Entry(self.root, width=30)
        self.txtfprice.place(x=150, y=80)

        self.Email = Label(self.root, text="Airline type:", font=("Comic Sans MS", 10, "italic"))
        self.Email.place(x=20, y=120)

        self.txtftype = Entry(self.root, width=30)
        self.txtftype .place(x=150, y=120)

        self.btnSign = Button(self.root, text="SAVE", width=10,command=self.air)
        self.btnSign.place(x=120, y=220)

        # classes= ["Economy","First_Class","Business_Class"]
        # self.vara4 = StringVar()
        # self.vara4.set("select class")
        #
        # self.air = OptionMenu(self.root, self.vara4, *classes)
        # self.air.place(x=20, y=170)

    def air(self):
        if (len(self.txtfName.get()) == 0):
            messagebox.showinfo("Airline_Name","Please enter Airline")
            return
        if (len(self.txtfprice.get()) == 0):
            messagebox.showinfo("Airline_Name","Please enter price")
            return
        if (len(self.txtftype.get()) == 0):
            messagebox.showinfo("Airline_Name","Please enter type")
            return
        else:
            data = {"Airline_name": self.txtfName.get(), "Airline_price": self.txtfprice.get(),"Airline_type": self.txtftype .get()}
                    # "classes":self.vara4.get()}
            result = firebase.post('/Airline/', data)
            self.root.mainloop()
            return

# root = Tk()
# app = airline1(root)
# root.mainloop()