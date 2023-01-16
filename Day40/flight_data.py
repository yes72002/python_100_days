class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, city_from, fly_from, city_to, fly_to, out_date, return_date, stop_overs=0, via_city=""):
        self.price = price
        self.city_from = city_from
        self.fly_from = fly_from
        self.city_to = city_to
        self.fly_to = fly_to
        self.out_date = out_date
        self.return_date = return_date

        self.stop_overs = stop_overs
        self.via_city = via_city