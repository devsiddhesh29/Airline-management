import tkinter as tk
from PIL import Image, ImageTk
from flight_ui.Facility1 import facility1
from flight_ui.Airlinr1 import airline1
from flight_ui.flightse import Flight_info
from flight_ui.flight_s import Flight_in
# from flight_ui.search import search1
from firebase import firebase
firebase=firebase.FirebaseApplication('https://flight-search-fadaf.firebaseio.com/',None)

class Welcome:

    def __init__(self, win):
        self.win = win
        self.win.title("welcome page")
        self.win.geometry("600x500")
        self.win.configure(bg='light blue')

        im = Image.open("../images/air.png")
        im = im.resize((600, 500), Image.ANTIALIAS)

        self.tkimage = ImageTk.PhotoImage(im)

        self.myvar = tk.Label(self.win, image=self.tkimage)
        self.myvar.place(x=0, y=0)

        self.menubar = tk.Menu(self.win)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Add Facility", command = lambda: self.open_window(facility1))
        self.filemenu.add_command(label="Add Airline", command = lambda: self.open_window(airline1))

        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.flight = tk.Menu(self.menubar, tearoff=0)
        self.flight.add_command(label="flight search", command = lambda: self.open_window(Flight_in))
        self.flight.add_separator()
        self.flight.add_command(label="flight_search",command = lambda: self.open_window(Flight_info))

        self.menubar.add_cascade(label="Flight", menu=self.flight)

        self.win.config(menu=self.menubar)

    def open_window(self, class_name):
        self.new = tk.Toplevel(self.win)
        class_name(self.new)
         #messagebox.showinfo("Info", "thanks for view our page")f