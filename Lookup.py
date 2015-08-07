from Airport import *
from Employee import *
from Currency import *
from CurrencyRate import *
from Route import *
import csv

class Lookup:
    """This is the lookup class. It is used to read the csv files, create appropiate
    classes and store the information in a dictionary. It's also used to look up the
    latitude and longditute of the airports and the currency for the aiprorts. """


    def __init__(self):
        self.airport_info={}#Dictionaries of objects created when reading csv files
        self.employee_info={}
        self.currency_info={}
        self.currencyrate_info={}


    def LookupEmployee(self, filename):
        """Looks up employee csv file, creates an object for each employee and saves the object to a dictionary"""
        try:
            with open(filename, encoding ="utf8", mode='rt') as infile:
                reader=csv.reader(infile)
                for row in reader:
                    anemployee=Employee(row[0],(row[1]),row[2],row[3], row[4], row[5])
                    self.employee_info[row[0]]=anemployee

        except FileNotFoundError:
            print("The file could not be found. Please try another file")

        return self.employee_info



    def LookupAirport(self, filename):
        """Looks up airport csv file, creates an object for each Airport and saves the object to a dictionary"""
        try:
            with open(filename, encoding ="utf8", mode='rt') as infile:
              reader=csv.reader(infile)
              for row in reader:
                anairport=Airport(row[4], row[2], row[3],row[6], row[7])
                self.airport_info[row[4]]=anairport

        except FileNotFoundError:
            print("The file could not be found. Please try another file")

        return self.airport_info



    def LookupCounrtyCurrency(self, filename):
        """Looks up country currency csv file, creates an object for each country currency and saves the object to a dictionary"""
        try:
            with open(filename, encoding ="utf8", mode='rt') as infile:
                reader=csv.reader(infile)
                for row in reader:
                    acurrency=Currency(row[17],(row[14]),row[0])
                    self.currency_info[row[0]]=acurrency

        except FileNotFoundError:
            print("The file could not be found. Please try another file")





    def LookupCurrencyRate(self, filename):
        """Looks up currency rate csv file, creates an object for each currency rate and saves the object to a dictionary"""
        try:
            with open(filename, encoding ="utf8", mode='rt') as infile:
                reader=csv.reader(infile)
                for row in reader:
                    arate=CurrencyRate(row[0],(row[1]),float(row[2]))
                    self.currencyrate_info[row[1]]=arate

        except FileNotFoundError:
            print("The file could not be found. Please try another file")



    def LookupLatandLong(self, airport1, airport2):
        """Looks up the latidude and longidtude for the two airports passed to the function using the dictionary saved as an attribute"""
        airports=[]
        for anairport in self.airport_info.values():
            if anairport.airportcode==airport1:
                airports.append(anairport.latitude)
                airports.append(anairport.longitude)
        for anairport in self.airport_info.values():
            if anairport.airportcode==airport2:
                airports.append(anairport.latitude)
                airports.append(anairport.longitude)
                return (airports)

    def findCurrency(self, airport):
        """Looks up the currecny of the airport passed to the function"""
        for anairport in self.airport_info.values():
            if anairport.airportcode==airport:
                currency=anairport.countryname
                for acurrency in self.currency_info.values():
                      if acurrency.countryName==currency:
                         currency=acurrency.currencyCode
                         for arate in self.currencyrate_info.values():
                            if arate.currencyCode==currency:
                                currency=arate.rateToEuro
        return currency






