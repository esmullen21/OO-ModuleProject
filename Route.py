import math
from Lookup import *
from itertools import permutations


class Route:
    """This class finds all the permutations of the list of airports, calculates the cost of each leg then finds the best cost for the entire journey"""

    def __init__(self, look):
        self.look=look # assigns the object look as an attribute of route

    def getAirports(self,name): #if an employee's name is selected, this function gets their visit list and then calls permutations() to fins the best route
        for anemployee in self.look.employee_info.values():
            if anemployee.name==name:
                employee=anemployee
                airports = anemployee.visitList()
        bestRoute=self.permutatuions(airports)
        return bestRoute


    def permutatuions(self, airports):
        six,seven, =[],[]


        itins = [airports[:1] + list(x) + airports[-1:] for x in permutations(airports[1:-1])]
        #Above takes the home city off the list(first and last) and gets the each permutation of the visiting cities, using the itertools module

        for c in range(len(itins)):  #This adds in the extra city
            combo=itins[c]
            for e in airports[0:4]:
                for i in range(5,0,-1):
                    newcombo=combo[:]
                    newcombo.insert(i,e)
                    itins.append(newcombo)

        while len(itins)>312: #This gets rid of all the itineraries that have two cities the same side by side (e.g. DUB, DUB). It pops them from the list. 312 is the miniumu number of itineraries there can be. Gotten trial and error
            for each in itins:
                index=0
                for c in range(len(each)-1):
                     if each[c] == each[c+1]:
                        itins.pop(itins.index(each))

        itineraries =[] #This loop makes sure there are no duplicates by adding the itineraries to a new list but before doing this, checking it's not already in there
        for each in itins:
            if each not in itineraries:
                itineraries.append(each)



        for each in itineraries[:24]: #Gets the first 24 itineries and adds them to a list (called six as there are 6 cities).
            six.append(each)
        legcost=self.legs(six) #Sends them to the function legs to get the cost for each leg

        for each in itineraries[25:]:#Gets the rest of the itineraries and adds them to a seperate list.
            seven.append(each)

        costs,itincost=self.sumCosts(six,seven, legcost)#Sends both lists six and seven, to the sumCosts function to be summed.
        bestCost=self.costCompare(costs) # compares the cost

        index=0
        for each in costs:
            if each==bestCost: # finds the entry in costs that matches the best cost returned
               i=index
            index += 1
        return (itincost[i])#uses the index of the match in costs, to find the itinerary in itincost and returns it to the function call



    def legs(self, six):
        """This calculates the cost of each leg (e.g. DUB, JFK) for all the possible city combinations and returns the list"""

        cities=[]
        leg=[]
        for each in six:
            c=0
            while c<5:
                leg=(each[c],each[c+1])
                if leg not in cities:
                    cities.append(leg)#If the leg is not already in the list, it is added
                c+=1

        #Below compiles a list of each leg and the cost
        legcost=[]
        for each in cities:
            cost=self.calcCosttLeg(each[0], each[1]) # Gets the cost of the leg
            legs=[each[0],each[1], cost] # Creates a list called leg containing the citys and the cost
            legcost.append(legs) # Appends leg to the list leg cost
        return legcost




    def calcCosttLeg(self, airport1, airport2):
        """This looks up the airports for each leg, sends them to the function that calculates the distance, it finds the
        currency for airport1, sends both to the function that calculates the cost and returns the value to the function call"""

        airports=(self.look.LookupLatandLong(airport1, airport2))
        distance=self.calDistance(airports)
        currency=self.look.findCurrency(airport1)
        cost=distance*currency
        return cost

    def calDistance(self, airports):
        """Calcualtes the distance between two airports"""

        #the latitudes are assigned to theta1 and theta 2 and the longitudes to phi1 and phi2
        theta1=float(airports[1])
        theta2=float(airports[3])
        phi1=90.0-float(airports[0])
        phi2=90.0-float(airports[2])
        rad=(2.0*(math.pi)/360.0)
        rEarth=6373
        radtheta1=(theta1*(rad))#the following 4 lines changes the lat and longs to radians
        radtheta2=(theta2*(rad))
        radphi1=(phi1*(rad))
        radphi2=(phi2*(rad))
        partA=math.sin(radphi1)*math.sin(radphi2)*math.cos(radtheta1-radtheta2)+ math.cos(radphi1)*math.cos(radphi2)#This and below computes the distance
        distance=(math.acos(partA))*rEarth
        return distance


    def sumCosts(self, six, seven,legcost):
        """Sums the cost of each leg for each itinerary and appends it to the end of each itinerary"""

        price=[]
        for each in six: #For every itinerary in the list six, this function gets each leg(or two cities)
            tot=0
            c=0
            while c<5:
                i=0
                leg=(each[c],each[c+1])
                for cities in legcost: #for each in legcost, it finds the match of leg and adds the price to tot
                    eachleg=(cities[0],cities[1])
                    if  leg== eachleg:
                        tot=tot+float(cities[2])
                c+=1
            price.append(int(tot))#Appends tot to price and at the end of each itinerary
            each.append(int(tot))


        for each in seven:#Does the same as it does for six
            tot=0
            c=0
            while c<6:
                i=0
                leg=(each[c],each[c+1])
                for cities in legcost:
                    eachleg=(cities[0],cities[1])
                    if  leg== eachleg:
                        tot=tot+float(cities[2])
                c+=1
            price.append(int(tot))
            each.append(int(tot))

        itincosts=six+seven #The lists of itineraries are added together
        return price,itincosts

    def costCompare(self, allCosts):
        """This finds the lowest cost in the list of costs and returns the lowest value"""
        best=min(i for i in allCosts)
        return best
