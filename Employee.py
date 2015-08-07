class Employee:
    """This is the employee class. The employees name, home city and the cities
    they have to visit are stored as attributes"""
    def __init__(self, name, homecity, visitingcity1, visitingcity2, visitingcity3,visitingcity4):
        self.name=name
        self.homecity=homecity
        self.visitingcity1=visitingcity1
        self.visitingcity2=visitingcity2
        self.visitingcity3=visitingcity3
        self.visitingcity4=visitingcity4

    def visitList(self):
        """Returns the list airports the employee has to visit to the route class"""
        return[self.homecity,self.visitingcity1,self.visitingcity2, self.visitingcity3, self.visitingcity4, self.homecity]
