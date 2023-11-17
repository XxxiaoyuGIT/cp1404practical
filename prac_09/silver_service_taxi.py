from taxi import Taxi

class silverservicetaxi(Taxi):
    flagfall = 4.50
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialize SilverServiceTaxi based on Taxi"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness
        self.price_per_km = Taxi.price_per_km * self.fanciness

    def get_fare(self):
        """Calculate the total fare including the flagfall."""
        return super().get_fare() + silverservicetaxi.flagfall

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
        """Returns a string representation of SilverServiceTaxi."""
        base_fare = Taxi.price_per_km
        actual_fare = base_fare * self.fanciness
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}, {self.current_fare_distance}km on current fare, ${actual_fare:.2f}/km plus flagfall of ${self.flagfall:.2f}"