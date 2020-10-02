from tkinter import *
# from flight_ui.book import Searchfli
from tkinter import messagebox
# #from flight_ui.searchh import Searchfli
from firebase import firebase
firebase=firebase.FirebaseApplication('https://flight-search-fadaf.firebaseio.com/',None)

class Flight_info:
    def __init__ (self, master):
        self.root = master
        self.root.title("Flight_info")
        self.root.geometry("500x500")
        self.root.configure(bg='Yellow')

        self.source = Label(self.root, text="SOURCE:", font=("Arial", 10, "italic"))
        self.source.place(x=20, y=30)

        self.txtSou= Entry(self.root, width=30, bg="light blue")
        self.txtSou.place(x=140, y=30)

        self.Dest = Label(self.root, text="DESTINATION:", font=("Arial", 10, "italic"))
        self.Dest.place(x=20, y=70)

        self.txtDest = Entry(self.root, width=30, bg="light blue")
        self.txtDest.place(x=140, y=70)

        self.Date = Label(self.root, text="Time:", font=("Arial", 10, "italic"),)
        self.Date.place(x=20, y=110)

        self.txtDate1 = Entry(self.root, width=20, bg="light blue")
        self.txtDate1.place(x=140, y=110)

        self.txtDate2 = Entry(self.root, width=20, bg="light blue")
        self.txtDate2.place(x=300, y=110)

        self.Fac = Label(self.root, text="Facility:", font=("Arial", 10, "italic"), fg="Red")
        self.Fac.place(x=20, y=150)

        self.result = firebase.get('Air/', None)
        airlines = []
        for lg in self.result:
            airlines.append(self.result[lg]["a"])
        airlines.insert(0,"--select--")
        self.varairline1 = StringVar()
        self.varairline1.set("--select--")

        self.air = OptionMenu(self.root, self.varairline1, *airlines)
        self.air.place(x=140, y=150)

        self.btnSign = Button(self.root, text="SAVE", width=10)
        self.btnSign.place(x=250, y=150)

        self.btnSign = Button(self.root, text="SEARCH", width=10,command = self.save1)
        self.btnSign.place(x=180, y=400)











    def save1(self):
        if (len(self.txtSou.get()) == 0):
            messagebox.showinfo("Flight_search", "Please enter Source")
            return
        if (len(self.txtDest.get()) == 0):
            messagebox.showinfo("Flight_search", "Please enter Destination")
            return
        if (len(self.txtDate1.get()) == 0):
            messagebox.showinfo("Flight_search", "Please enter Time")
            return
        else:
            data = {"source": self.txtSou.get(), "destination": self.txtDest.get(),"time": self.txtDate1.get()}
            r = firebase.post('/flight_se/', data)
            return


# root = Tk()
# app =Flight_info(root)
# root.mainloop()