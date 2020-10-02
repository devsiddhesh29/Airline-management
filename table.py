import tkinter as tk
from tkinter import ttk


def show():
    tempList = [['JIM', '0.33'],['shubham', '0.67'],['Sanket', '0.96']]

    for i, (name, score) in enumerate(tempList, start=1):
        listBox.insert("", "end", values = (i, name, score))

scores = tk.Tk()
label = tk.Label(scores, text="High Scores", font=("Arial",30)).grid(row=0, columnspan=3)


cols = ('Positions', 'Name', 'Score')
listBox = ttk.Treeview(scores, column=cols,show="headings")

for col in cols:
    listBox.heading(col, text=col)

listBox.grid(row=1, column=0, columnspan =2)

showScore = tk.Button(scores,text="Show Scores", width=15, command = show).grid(row=4, column=0)
closeButton = tk.Button(scores, text="Close", width=15, command=exit).grid(row=4, column=1)

scores.mainloop()
