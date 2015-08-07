import csv
from tkinter import *
from tkinter import ttk, StringVar
from Lookup import *
from Route import *


"""Note: Jane has an extra DUB three times, meaning there are fewer itterations for her
I ahve changed this to AMS."""

class GUI():
    """This creates the GUI for the program"""

    def __init__(self):
        self.look=Lookup()#Creates an instance of the class Lookup called look
        self.background=Tk()
        self.background.wm_title("Choose an option")
        self.background.geometry("%dx%d+%d+%d" % (330, 200, 200, 150))
        self.background.configure(background='light sky blue')
        Label(self.background, text="Choose an option:", bg="white").pack(padx=10, pady=10)
        empOpt = Button(self.background, text="Choose an employee", command=self.employee, bg="white") #Calls the employee function of the class
        ownOpt = Button(self.background, text="Choose your own airports", command=self.ownAirports, bg="white")#Calls the ownAirports function of the class
        empOpt.pack(fill=X, pady=10)
        ownOpt.pack(fill=X, pady=10)

        self.background.mainloop()


    def ownAirports(self):
        """Function for creation of the GUI to select your own airports"""
        self.background.destroy()#Destroys the original GUI
        airports=[]
        airfile="airport.csv"
        curfile="countrycurrency.csv"
        ratefile="currencyrates.csv"
        airport_info=self.look.LookupAirport(airfile)#Calls the function LookupAirport and stores the returned data as airport_info
        for key in airport_info: # Creates a list of airports
          airports.append(key)
        airports.sort()
        self.look.LookupCounrtyCurrency(curfile)
        self.look.LookupCurrencyRate(ratefile)
        #New GUI
        background=Tk()
        background.wm_title("Select your own Airports")
        background.configure(background='light sky blue')
        background.geometry("%dx%d+%d+%d" % (375, 250, 200, 150))
        home=Label(background, text="Home Airport", bg="white").grid(pady=5,padx=5,column=0, row=0)
        self.box2=StringVar()
        box2 = ttk.Combobox(background, values=airports, textvariable=self.box2, state='readonly')#Combobox for user to select airport
        box2.set("Choose a Home Airport")
        box2.grid(pady=5, padx=5,column=1, row=0)
        visit1=Label(background, text="Visiting Airport", bg="white").grid(column=0, row=1)
        self.box3=StringVar()
        box3 = ttk.Combobox(background, values=airports, textvariable=self.box3, state='readonly')
        box3.set("Choose an airport to visit")
        box3.grid(pady=5, padx=5,column=1, row=1)
        visit2=Label(background, text="Visiting Airport", bg="white").grid(column=0, row=2)
        self.box4=StringVar()
        box4 = ttk.Combobox(background, values=airports,textvariable=self.box4, state='readonly')
        box4.set("Choose an airport to visit")
        box4.grid(pady=5, padx=5,column=1, row=2)
        visit3=Label(background, text="Visiting Airport", bg="white").grid(column=0, row=3)
        self.box5=StringVar()
        box5 = ttk.Combobox(background, values=airports,textvariable=self.box5, state='readonly')
        box5.set("Choose an airport to visit")
        box5.grid(pady=5, padx=5,column=1, row=3)
        visit4=Label(background, text="Visiting Airport", bg="white").grid(column=0, row=4)
        self.box6=StringVar()
        box6 = ttk.Combobox(background, values=airports,textvariable=self.box6, state='readonly')
        box6.set("Choose an airport to visit")
        box6.grid(pady=5, padx=5,column=1, row=4)
        self.answer=StringVar()
        answer=Label(background, textvariable=self.answer, bg="white").grid(column=1, row=5)
        button = Button(background, text="Select", command=self.own,bg="white")#Calls the function own when button pushed
        button.grid(pady=5, padx=5,column=1,row=6)
        background.mainloop()

    def employee(self):
        """Function for creation of the GUI to select an employee"""
        self.background.destroy()
        employees=[]
        airports=[]
        employfile="employees.csv"
        airfile="airport.csv"
        curfile="countrycurrency.csv"
        ratefile="currencyrates.csv"
        employee_info=self.look.LookupEmployee(employfile)
        self.look.LookupAirport(airfile)
        self.look.LookupCounrtyCurrency(curfile)
        self.look.LookupCurrencyRate(ratefile)
        for key in employee_info:
            employees.append(key)
        employees.sort()
        #New GUI
        background=Tk()
        background.wm_title("Select an Employee")
        background.geometry("%dx%d+%d+%d" % (400, 150, 150, 200))
        background.configure(background='light sky blue')
        Label(background, text="Choose an employee:", bg="white").grid(padx=10,pady=30,column=0, row=5)
        self.box1name=StringVar()
        self.answer=StringVar()
        box1 = ttk.Combobox(background, values=employees, textvariable=self.box1name, state='readonly')#Allows user to select an employee
        box1.set("Choose an employee")
        box1.grid(padx=30,column=0,row=6)
        answer=Label(background, textvariable=self.answer, bg="white").grid(column=0,row=8)
        button = Button(background, text="Select", command=self.select, bg="white")#Calls select
        button.grid(padx=10,column=1,row=6)
        background.mainloop()


    def select(self):
        """Computes the best possible route and its price when an employee is selected"""
        name = self.box1name.get()
        route=Route(self.look)
        bestRoute=route.getAirports(name)
        if len(bestRoute)==7:#If there are 6 airports
            self.answer.set("The best Route is: "+bestRoute[0]+" "+bestRoute[1]+" "+bestRoute[2]+" "+bestRoute[3]+" "+bestRoute[4]+" "+bestRoute[5]+"\nPrice= "+str(bestRoute[6]))#Prints string to the GUI
        if len(bestRoute)==8:#If there are seven airports
            self.answer.set("The best Route is: "+bestRoute[0]+" "+bestRoute[1]+" "+bestRoute[2]+" "+bestRoute[3]+" "+bestRoute[4]+" "+bestRoute[5]+" "+bestRoute[6]+"\nPrice= "+str(bestRoute[7]))
        f = open('Output.csv','w') # Writes to file
        wr = csv.writer(f, dialect='excel')
        wr.writerow(bestRoute)
        f.close()

    def own(self):
        """Computes the best possible route and its price when 5 airports are selected"""
        home=self.box2.get()
        visit1=self.box3.get()
        visit2=self.box4.get()
        visit3=self.box5.get()
        visit4=self.box6.get()
        airports=[home,visit1,visit2,visit3,visit4,home]
        route=Route(self.look)
        bestRoute=route.permutatuions(airports)
        if len(bestRoute)==7:
            self.answer.set("The best Route is: "+bestRoute[0]+" "+bestRoute[1]+" "+bestRoute[2]+" "+bestRoute[3]+" "+bestRoute[4]+" "+bestRoute[5]+"\nPrice= "+str(bestRoute[6]))
        if len(bestRoute)==8:
            self.answer.set("The best Route is: "+bestRoute[0]+" "+bestRoute[1]+" "+bestRoute[2]+" "+bestRoute[3]+" "+bestRoute[4]+" "+bestRoute[5]+" "+bestRoute[6]+"\nPrice= "+str(bestRoute[7]))
        f = open('Output.csv','w')
        wr = csv.writer(f, dialect='excel')
        wr.writerow(bestRoute)
        f.close()


gui=GUI()


