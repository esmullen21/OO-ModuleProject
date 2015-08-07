import unittest
from Airport import *
from Employee import *
from Lookup import *
from Route import *

class testAlice(unittest.TestCase):

    def testAlice(self):
        Alice=Employee("Alice", "DUB", "JFK","AAL", "CDG", "SYD")
        airports=Alice.visitList()
        bestRoute=route.permutatuions(airports)
        self.assertEqual(bestRoute,['DUB', 'CDG', 'AAL', 'SYD', 'JFK', 'DUB', 20431])

class testBob(unittest.TestCase):

    def testBob(self):
        Bob=Employee("Bob", "DUB", "LHR","AMS", "AAL", "CDG")
        airports=Bob.visitList()
        bestRoute=route.permutatuions(airports)
        self.assertEqual(bestRoute,['DUB', 'LHR', 'CDG', 'AMS', 'AAL', 'DUB', 2106])

class testJane(unittest.TestCase):

    def testJane(self):
        Jane=Employee("Jane", "DUB", "LHR","AMS", "ARN", "SIN")
        airports=Jane.visitList()
        bestRoute=route.permutatuions(airports)
        self.assertEqual(bestRoute,['DUB', 'LHR', 'AMS', 'ARN', 'SIN','ARN', 'DUB', 9947])

class testTom(unittest.TestCase):

    def testTom(self):
        Tom=Employee("Tom", "LHR", "AMS","SFO", "SIN", "DUB")
        airports=Tom.visitList()
        bestRoute=route.permutatuions(airports)
        self.assertEqual(bestRoute,['LHR', 'AMS', 'SIN', 'SFO', 'DUB', 'LHR', 28524])

class testAirport(unittest.TestCase):

    def testAirport(self):
        Alice=Employee("Alice", "DUB", "JFK","AAL", "CDG", "SYD")
        name="Alice"
        best=route.getAirports(name)
        self.assertEqual(best, ['DUB', 'CDG', 'AAL', 'SYD', 'JFK', 'DUB', 20431])

class testEmployeeLookup(unittest.TestCase):

    def testEmployeeLookup(self):
        try:
            look.LookupEmployee('badfile.csv')
        except FileNotFoundError:
                pass
        except Exception:
                raise Exception("Should be raising a FileNotFound error")

class testAirportLookup(unittest.TestCase):

    def testAirportLookup(self):
        try:
            look.LookupAirport('badfile.csv')
        except FileNotFoundError:
                pass
        except Exception:
                raise Exception("Should be raising a FileNotFound error")


class testCountryCurrencyLookup(unittest.TestCase):

    def testCountryCurrencyLookup(self):
        try:
            look.LookupCounrtyCurrency('badfile.csv')
        except FileNotFoundError:
                pass
        except Exception:
                raise Exception("Should be raising a FileNotFound error")


class testCurrencyRateLookup(unittest.TestCase):

    def testCurrencyRateLookup(self):
        try:
            look.LookupCurrencyRate('badfile.csv')
        except FileNotFoundError:
                pass
        except Exception:
                raise Exception("Should be raising a FileNotFound error")

class testpermutatuions(unittest.TestCase):

    def testpermutatuions(self):
        airports=["DUB", "LHR","AMS", "AAL", "CDG","DUB"]
        best=route.permutatuions(airports)
        self.assertEqual(best,['DUB', 'LHR', 'CDG', 'AMS', 'AAL', 'DUB', 2106])

class testlegs(unittest.TestCase):

    def testlegs(self):
        six=[['DUB', 'JFK', 'AAL', 'CDG', 'SYD', 'DUB'], ['DUB', 'JFK', 'AAL', 'SYD', 'CDG', 'DUB']]
        answer=route.legs(six)
        expected=[['DUB', 'JFK', 5104.628713706877], ['JFK', 'AAL', 5663.171246608263], ['AAL', 'CDG', 136.8628075502398], ['CDG', 'SYD', 16949.66161766836], ['SYD', 'DUB', 12490.15915693645], ['AAL', 'SYD', 2163.479052433552], ['SYD', 'CDG', 12293.58957129486], ['CDG', 'DUB', 785.2180721866147]]

class testcalcCosttLeg(unittest.TestCase):

    def testcalcCosttLeg(self):
        airports=("DUB", "JFK")
        answer=int(route.calcCosttLeg(airports[0], airports[1]))
        self.assertEqual(answer, 5104)

class testcalDistance(unittest.TestCase):

    def testcalDistance(self):
        airports=(53.421333,-6.270075,40.639751,-73.778925)
        answer=int(route.calDistance(airports))
        self.assertEqual(answer, 5104)

class testsumCosts(unittest.TestCase):

    def testsumCosts(self):
        six=[['DUB', 'JFK', 'AAL', 'CDG', 'SYD', 'DUB'], ['DUB', 'JFK', 'AAL', 'SYD', 'CDG', 'DUB']]
        seven=[['DUB', 'JFK', 'AAL', 'SYD','CDG', 'SYD', 'DUB'], ['DUB', 'JFK', 'CDG','AAL', 'SYD', 'CDG', 'DUB']]
        legcost=[['DUB', 'JFK', 5104.628713706877], ['JFK', 'AAL', 5663.171246608263], ['AAL', 'CDG', 136.8628075502398], ['CDG', 'SYD', 16949.66161766836], ['SYD', 'DUB', 12490.15915693645], ['AAL', 'SYD', 2163.479052433552], ['SYD', 'CDG', 12293.58957129486], ['CDG', 'DUB', 785.2180721866147]]
        answer=route.sumCosts(six, seven,legcost)
        self.assertEqual(answer,([40344, 26010, 54664, 20346], [['DUB', 'JFK', 'AAL', 'CDG', 'SYD', 'DUB', 40344], ['DUB', 'JFK', 'AAL', 'SYD', 'CDG', 'DUB', 26010], ['DUB', 'JFK', 'AAL', 'SYD', 'CDG', 'SYD', 'DUB', 54664], ['DUB', 'JFK', 'CDG', 'AAL', 'SYD', 'CDG', 'DUB', 20346]]))

class testcostCompare(unittest.TestCase):

    def testcostCompare(self):
        costs=[40344, 26010, 54664, 20346]
        answer=route.costCompare(costs)
        self.assertEqual(answer,20346)



look=Lookup()
look.LookupEmployee("employees.csv")
look.LookupAirport("airport.csv")
look.LookupCounrtyCurrency("countrycurrency.csv")
look.LookupCurrencyRate("currencyrates.csv")
route=Route(look)

if __name__ == '__main__':
    unittest.main()