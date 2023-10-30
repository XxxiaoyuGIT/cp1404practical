class Guitar:
    current_year = 2022  # Define the current year as a class variable

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        return self.current_year - self.year  # Use the class variable for current year

    def is_vintage(self):
        return self.get_age() >= 50

# Example usage
guitar1 = Guitar("Fender Stratocaster", 1970, 1500)
guitar2 = Guitar("Gibson Les Paul", 2020, 2500)

print(guitar1)
print("Is vintage:", guitar1.is_vintage())
print(guitar2)
print("Is vintage:", guitar2.is_vintage())

