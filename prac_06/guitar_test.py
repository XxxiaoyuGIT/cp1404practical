from guitar import Guitar

def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 1299.99)  # Create sample guitars

    print("{} get_age() - Expected {}. Got {}".format(gibson.name, 100, gibson.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(another_guitar.name, 9, another_guitar.get_age()))  # Test get_age()

    print("{} is_vintage() - Expected {}. Got {}".format(gibson.name, True, gibson.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(another_guitar.name, False, another_guitar.is_vintage()))  # Test is_vintage()

    fifty_year_old_guitar = Guitar("50-year old guitar", 1972, 2000)  # Example
    print("{} is_vintage() - Expected {}. Got {}".format(fifty_year_old_guitar.name, True, fifty_year_old_guitar.is_vintage()))

if __name__ == "__main__":
    main()