from tkinter import *
from tkinter import messagebox
from firebase import firebase
from PIL import Image, ImageTk
firebase=firebase.FirebaseApplication('https://flight-search-fadaf.firebaseio.com/',None)


class facility1:
    def __init__ (self, master):
        self.root = master
        self.root.title("Facility")
        self.root.geometry("500x500")
        self.root.configure(bg='light pink')

        im = Image.open("../images/k.jfif")
        im = im.resize((500, 500), Image.ANTIALIAS)

        self.tkimage = ImageTk.PhotoImage(im)

        self.myvar = Label(self.root, image=self.tkimage)
        self.myvar.place(x=0, y=0)

        self.Name = Label(self.root, text="Facility name:", font=("Arial", 10, "italic"),bg="light pink")
        self.Name.place(x=20, y=30)

        self.txtName = Entry(self.root, width=30)
        self.txtName.place(x=150, y=30)

        self.Username = Label(self.root, text="Facility price:", font=("Arial", 10, "italic"),bg="light pink")
        self.Username.place(x=20, y=80)

        self.txtprice = Entry(self.root, width=30)
        self.txtprice.place(x=150, y=80)

        self.Email = Label(self.root, text="Facility type:", font=("Arial", 10, "italic"),bg="light pink")
        self.Email.place(x=20, y=120)

        self.txttype = Entry(self.root, width=30)
        self.txttype.place(x=150, y=120)

        self.btnSign = Button(self.root, text="SAVE", width=10,command=self.save1,bg="yellow")
        self.btnSign.place(x=250, y=400)

        # self.result = firebase.get('Air/',None)
        # airlines = []
        # for lg in self.result:
        #     airlines.append(self.result[lg]["a"])
        # airlines.insert(0,"--select--")
        # self.varairline1 = StringVar()
        # self.varairline1.set("--select--")
        #
        # self.air = OptionMenu(self.root, self.varairline1, *airlines)
        # self.air.place(x=80, y=250)

    def save1(self):
        if (len(self.txtName.get()) == 0):
            messagebox.showinfo("facility_Name","Please enter facility")
            return
        if (len(self.txtprice.get()) == 0):
            messagebox.showinfo("facility_Name","Please enter price")
            return
        if (len(self.txttype.get()) == 0):
            messagebox.showinfo("facility_Name","Please enter type")
            return
        else:
            data = {"facility_name":self.txtName.get(),"facility_price":self.txtprice.get(),"facility_type":self.txttype.get()}
            # ,"airlinee":self.varairline1.get()}
            r = firebase.post('/facilities/', data)
            return