from tkinter import *
from tkinter import messagebox
from tkcalendar import *
from tkinter import ttk
from firebase import firebase
firebase=firebase.FirebaseApplication('https://flight-search-fadaf.firebaseio.com/',None)

class Flight_in:
    def __init__(self, master):
        self.root = master
        self.root.title("Flight_info")
        self.root.geometry("500x500")
        self.root.configure(bg='Yellow')

        self.source = Label(self.root, text="SOURCE:", font=("Arial", 10, "italic"), fg="Red")
        self.source.place(x=20, y=50)

        self.result = firebase.get('fli/', None)
        flight = []
        for lg in self.result:
            flight.append(self.result[lg]["b"])
        flight.insert(0, "--select--")
        self.varairline2 = StringVar()
        self.varairline2.set("--select--")

        self.air = OptionMenu(self.root, self.varairline2, *flight)
        self.air.place(x=140, y=50)


        self.Dest = Label(self.root, text="DESTINATION:", font=("Arial", 10, "italic"), fg = "Red")
        self.Dest.place(x=20, y=90)

        self.result = firebase.get('fli/', None)
        flight1 = []
        for lg in self.result:
            flight1.append(self.result[lg]["b"])
        flight1.insert(0, "--select--")
        self.varairline3 = StringVar()
        self.varairline3.set("--select--")

        self.air = OptionMenu(self.root, self.varairline3, *flight1)
        self.air.place(x=140, y=90)

        self.Date = Label(self.root, text="Time:", font=("Arial", 10, "italic"), )
        self.Date.place(x=20, y=130)

        # self.txtDate11 = Entry(self.root, width=20, bg="light blue")
        # self.txtDate11.place(x=140, y=130)
        #
        # self.txtDate2 = Entry(self.root, width=20, bg="light blue")
        # self.txtDate2.place(x=300, y=130)
        self.cal = DateEntry(self.root, width=12, year=2020, month=6, day=22, background='darkblue', foreground='white',borderwidth=2)
        self.cal.place(x=140, y=130)

        self.Fac = Label(self.root, text="Facility:", font=("Arial", 10, "italic"), fg="Red")
        self.Fac.place(x=20, y=180)

        self.result = firebase.get('Air/', None)
        airlines = []
        for lg in self.result:
            airlines.append(self.result[lg]["a"])
        airlines.insert(0, "NO  facility  Charges")
        self.varair1 = StringVar()
        self.varair1.set("--select--")
        self.aird = OptionMenu(self.root, self.varair1, *airlines)
        self.aird.place(x=140, y=180)

        self.Date = Label(self.root, text="Airline:", font=("Arial", 10, "italic"), )
        self.Date.place(x=20, y=230)

        self.result = firebase.get('Adrop/', None)
        airline = []
        for lg in self.result:
            airline.append(self.result[lg]["d"])
        airlines.insert(0, "--select--")
        self.vara = StringVar()
        self.vara.set("--select--")
        self.aird1 = OptionMenu(self.root, self.vara, *airline)
        self.aird1.place(x=140, y=230)


        self.btnSign = Button(self.root, text="SEARCH", width=10, command=self.save2)
        self.btnSign.place(x=180, y=400)
    #
    # def show(self):
    #     tempList = [['JIM', '0.33'], ['shubham', '0.67'], ['Sanket', '0.96']]
    #
    #     for i, (name, score) in enumerate(tempList, start=1):
    #         listBox.insert("", "end", values=(i, name, score))
    #
    # scores = Tk()
    # label = Label(scores, text="High Scores", font=("Arial", 30)).grid(row=0, columnspan=3)
    #
    # cols = ('Positions', 'Name', 'Score')
    # listBox = ttk.Treeview(scores, column=cols, show="headings")
    #
    # for col in cols:
    #     listBox.heading(col, text=col)
    #
    # listBox.grid(row=1, column=0, columnspan=2)
    #
    # showScore = Button(scores, text="Show Scores", width=15, command=show).grid(row=4, column=0)
    # closeButton = Button(scores, text="Close", width=15, command=exit).grid(row=4, column=1)

    def save2(self):
        data = {"SOURCE": self.varairline2.get(), "DESTINATION": self.varairline3.get(), "FACILITY": self.varair1.get(), "AIRLINE": self.vara.get()}
        r = firebase.post('/Searchf/', data)
        return

# root = Tk()
# app =Flight_in(root)
# root.mainloop()
#

#

