from tkinter import *

def clearscr():
    for widget in window.winfo_children():
        widget.destroy()

def insert_book():

    def getvals():
        clearscr()
        info = []
        info += Nvalue.get(),Pvalue.get(),Gvalue.get(),Cvalue.get(),PMvalue.get()
        print("You entered:", info)

    clearscr()

    Label(window, text = "Python Registration Form", font = "times 15 bold").grid(row = 0, column = 3)

    Name = Label(window, text = "Name")
    Name.grid(row = 1, column = 2)
    Phone = Label(window, text = "Phone")
    Phone.grid(row = 2, column = 2)
    Gender = Label(window, text = "Gender")
    Gender.grid(row = 3, column = 2)
    Country = Label(window, text = "Country")
    Country.grid(row = 4, column = 2)
    Pay_Mode = Label(window, text = "Payment Mode")
    Pay_Mode.grid(row = 5, column = 2)

    Nvalue = StringVar()
    Pvalue = StringVar()
    Gvalue = StringVar()
    Cvalue = StringVar()
    PMvalue = StringVar()
    #checkvalue = IntVar

    Name_entry = Entry(window, textvariable = Nvalue)
    Name_entry.grid(row = 1, column = 3)
    Phone_entry = Entry(window, textvariable = Pvalue)
    Phone_entry.grid(row = 2, column = 3)
    Gender_entry = Entry(window, textvariable = Gvalue)
    Gender_entry.grid(row = 3, column = 3)
    Country_entry = Entry(window, textvariable = Cvalue)
    Country_entry.grid(row = 4, column = 3)
    Pay_Mode_entry = Entry(window, textvariable = PMvalue)
    Pay_Mode_entry.grid(row = 5, column = 3)

    #Check_btn = Checkbutton(text = "Remember me?", variable = checkvalue)
    #Check_btn.grid(row = 6, column = 3)

    Button(text="Submit", command=getvals).grid(row = 7, column = 3)

def admin_screen():
    clearscr()
    print("admin_screen")

    Label(window, text = "What action do you want to perform?", font = "times 15 bold").place(anchor = CENTER, relx = .5, y = 50)

    Button(text="View Available Books").place(anchor = CENTER, relx = .5, y = 80)
    Button(text="Add New Books").place(anchor = CENTER, relx = .5, y = 110)
    Button(text="Delete Books").place(anchor = CENTER, relx = .5, y = 140)
    Button(text="Set Book availability as ISSUED").place(anchor = CENTER, relx = .5, y = 170)
    Button(text="Set Book availibility as AVAILABLE").place(anchor = CENTER, relx = .5, y = 200)

def student_screen():

    def search_options():
        clearscr()
        Label(window, text = "How do you wanna search?", font = "times 15 bold").place(anchor = CENTER, relx = .5, y = 70)

        Button(text="Search via Book Name").place(anchor = CENTER, relx = .5, y = 105)
        Button(text="Search via Authur Name").place(anchor = CENTER, relx = .5, y = 140)
        Button(text="Search via Book Genre").place(anchor = CENTER, relx = .5, y = 175)

    clearscr()
    print("admin_screen")

    Label(window, text = "What action do you want to perform?", font = "times 15 bold").place(anchor = CENTER, relx = .5, y = 90)

    Button(text="View Available Books").place(anchor = CENTER, relx = .5, y = 125)
    Button(text="Search for a book", command=search_options).place(anchor = CENTER, relx = .5, y = 160)

def main_menu():
    lbl1=Label(window, text="The Library Management System", fg='Blue', font=("Helvetica", 25))
    lbl1.place(x = 10, y = 50)
    lbl2=Label(window, text="I am a..", fg='Blue', font=("Helvetica", 20))
    lbl2.place(x = 200, y = 100)

    Button(text="Admin", command=admin_screen).place(x = 170, y = 150)
    Button(text="Student", command=student_screen).place(x = 270, y = 150)

window = Tk()
window.geometry("500x300")

main_menu()

window.mainloop()
