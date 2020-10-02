from tkinter import *
from tkinter import messagebox
from tkcalendar import *
from firebase import firebase
firebase=firebase.FirebaseApplication('https://flight-search-fadaf.firebaseio.com/',None)

class Flight1:
    def __init__(self, master):
        self.root = master
        self.root.title("Flight_info")
        self.root.geometry("500x500")
        self.root.configure(bg='Yellow')

        self.source1 = Label(self.root, text="SOURCE:", font=("Arial", 10, "italic"), fg="Red")
        self.source1.place(x=20, y=50)

        self.result = firebase.get('fli/', None)
        flight = []
        for lg in self.result:
            flight.append(self.result[lg]["b"])
        flight.insert(0, "--select--")
        self.varairli = StringVar()
        self.varairli.set("--select--")

        self.air = OptionMenu(self.root, self.varairli, *flight)
        self.air.place(x=140, y=50)

        self.Dest1 = Label(self.root, text="DESTINATION:", font=("Arial", 10, "italic"), fg="Red")
        self.Dest1.place(x=20, y=90)

        self.result = firebase.get('fli/', None)
        flight1 = []
        for lg in self.result:
            flight1.append(self.result[lg]["b"])
        flight1.insert(0, "--select--")
        self.varairli3 = StringVar()
        self.varairli3.set("--select--")

        self.air = OptionMenu(self.root, self.varairli3, *flight1)
        self.air.place(x=140, y=90)

        self.Date = Label(self.root, text="Time:", font=("Arial", 10, "italic"), )
        self.Date.place(x=20, y=130)
        self.cal = DateEntry(self.root, width=12, year=2020, month=6, day=22, background='darkblue', foreground='white',borderwidth=2)
        self.cal.place(x=140, y=130)

        self.Dest1 = Label(self.root, text="Passenger count:", font=("Arial", 10, "italic"), fg="Red")
        self.Dest1.place(x=20, y=180)

        self.pc = Entry(self.root, width=30, bg="light yellow")
        self.pc.place(x=140, y=180)

        self.Date = Label(self.root, text="Airline:", font=("Arial", 10, "italic"), )
        self.Date.place(x=20, y=230)

        self.result = firebase.get('Adrop/', None)
        airline11 = []
        for lg in self.result:
            airline11.append(self.result[lg]["d"])
        airline11.insert(0, "--select--")
        self.varaa = StringVar()
        self.varaa.set("--select--")
        self.aird1 = OptionMenu(self.root, self.varaa, *airline11)
        self.aird1.place(x=140, y=230)

        self.btnSign = Button(self.root, text="SEARCH", width=10, command=self.save22)
        self.btnSign.place(x=180, y=280)

    def save22(self):
        messagebox.showinfo("facility_Name", "Please enter facility")






#
# root = Tk()
# app =Flight1(root)
# root.mainloop()
