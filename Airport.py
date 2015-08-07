class Airport:
    """This is the class for the airports. The airportcode, cityname, countryname,
    latitude and longitude are stored as attributes"""

    def __init__(self, airportcode, cityname, countryname, latitude, longitude):
        self.airportcode=airportcode
        self.ctyname=cityname
        self.countryname=countryname
        self.latitude=latitude
        self.longitude=longitude
