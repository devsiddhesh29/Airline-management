from tkinter import *
from flight_ui.Facility1 import facility1
#from firebase import firebase



class Searchfli:
    def __init__ (self, win):
        self.root = win
        self.root.title("Flight List")
        self.root.geometry("800x800")
        self.root.configure(bg='light blue')


        self.lab1=Label(self.root, text="Select Ur Flight:", font=("Comic Sans MS", 20, "italic"))
        self.lab1.pack()



        self.button1 = Button(self.root, text="", width=80, height=8,command=self.open_window)
        self.button1.place(x=20, y=80)
        a="1234"
        self.txt = Label(self.root, text="Flight Name : King Fisher \nFlight Number :"+ a+"\nFaclities : Water is Free , Cold drink\n\n Ratings : 4 Stared", font=("Comic Sans MS", 10, "italic"))
        self.txt.place(x=40, y=90)

        self.button1 = Button(self.root, text="", width=80, height=8,command=self.open_window)
        self.button1.place(x=20, y=220)
        a = "3421"
        self.txt = Label(self.root,
                         text="Flight Name : Airbus \nFlight Number :" + a + "\nFaclities : Water is Free , Cold drink\n\n Ratings : 4.5 Stared",
                         font=("Comic Sans MS", 10, "italic"))
        self.txt.place(x=40, y=230)

        self.button1 = Button(self.root, text="", width=80, height=8,command=self.open_window)
        self.button1.place(x=20, y=360)
        a = "8741"
        self.txt = Label(self.root,
                         text="Flight Name : Fly Emirates \nFlight Number :" + a + "\nFaclities : Water is Free , Cold drink\n\n Ratings : 4.3 Stared",
                         font=("Comic Sans MS", 10, "italic"))
        self.txt.place(x=40, y=370)

        self.button1 = Button(self.root, text="", width=80, height=8,command=self.open_window)
        self.button1.place(x=20, y=500)
        a = "5412"
        self.txt = Label(self.root,
                         text="Flight Name : Singapore Airlines \nFlight Number :" + a + "\nFaclities : Water is Free , Cold drink\n\n Ratings : 4.2 Stared",
                         font=("Comic Sans MS", 10, "italic"))
        self.txt.place(x=40, y=510)

    def open_window(self):
        self.root.destroy()
        self.root = Tk()
        app = facility1(self.root)
        self.root.mainloop()