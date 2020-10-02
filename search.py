# from tkinter import *
# from flight_ui.book import Searchfli
# from tkinter import messagebox
# #from flight_ui.searchh import Searchfli
# #from firebase import firebase
#
# class search1:
#     def __init__ (self, master):
#         self.root = master
#         self.root.title("Airline")
#         self.root.geometry("650x500+500+400")
#         self.root.configure(bg='light Yellow')
#
#         self.Name = Label(self.root, text="From:", font=("Arial", 10, "italic"), fg = "Red")
#         self.Name.place(x=40, y=30)
#
#         self.Username = Label(self.root, text="To:", font=("Arial", 10, "italic"), fg = "Red")
#         self.Username.place(x=40, y=100)
#
#         self.Email = Label(self.root, text=" Booking Date:", font=("Arial", 10, "italic"), fg = "Red")
#         self.Email.place(x=40, y=170)
#
#         self.noofpass = Label(self.root, text=" No of Passenger:", font=("Arial", 10, "italic"), fg="Red")
#         self.noofpass.place(x=40, y=220)
#
#         self.noofpass = Label(self.root, text="Gender:", font=("Arial", 10, "italic"), fg="Red")
#         self.noofpass.place(x=40, y=270)
#
#         self.btnSign = Button(self.root, text="SEARCH", width=10,command = self.save)
#         self.btnSign.place(x=180, y=400)
#
#         source = ["Delhi", "Pune", "Mumbai"]
#         self.vara = StringVar()
#         self.vara.set("enter source")
#
#         self.air = OptionMenu(self.root, self.vara, *source)
#         self.air.place(x=170, y=30)
#
#         Destination = ["Delhi", "Pune", "Mumbai"]
#         self.vara1 = StringVar()
#         self.vara1.set("enter Destination")
#
#         self.air = OptionMenu(self.root, self.vara1, *Destination)
#         self.air.place(x=170, y=100)
#
#         Date= [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
#         self.vara2 = StringVar()
#         self.vara2.set("Date")
#
#         self.air = OptionMenu(self.root, self.vara2, *Date)
#         self.air.place(x=170, y=170)
#
#         Month= ["Jan", "Feb", "Mar", "Apr"]
#         self.vara3 = StringVar()
#         self.vara3.set("Month")
#
#         self.air = OptionMenu(self.root, self.vara3, *Month)
#         self.air.place(x=250, y=170)
#
#         Year = [2016,2017,2018,2019,2020]
#         self.vara4 = StringVar()
#         self.vara4.set("Year")
#
#         self.air = OptionMenu(self.root, self.vara4, *Year)
#         self.air.place(x=340, y=170)
#
#         passenger = [1,2,3,4,5,6,7,8,9,10]
#         self.vara4 = StringVar()
#         self.vara4.set("no of passenger")
#
#         self.air = OptionMenu(self.root, self.vara4, *passenger)
#         self.air.place(x=170, y=220)
#
#
#         gender = ["Male","Female","Other"]
#         self.vara4 = StringVar()
#         self.vara4.set("Enter your Gender")
#
#         self.air = OptionMenu(self.root, self.vara4, *gender)
#         self.air.place(x=170, y=270)
#
#     def save(self):
#         self.root.destroy()
#         self.root = Tk()
#         signin = Searchfli(self.root)
#         self.root.mainloop()

        # messagebox.showinfo("facility", "you selected")

    # def submit(self, class_name):
        # self.new = Toplevel(self.root)
        # class_name(self.new)

        # self.root.destroy()
        # self.root = Tk()
        # app = Searchfli(self.root)
        # self.root.mainloop()