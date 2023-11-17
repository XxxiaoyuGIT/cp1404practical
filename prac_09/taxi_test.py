from taxi import Taxi

def main():
    """Test Taxi class with various operations."""
    My_taxi = Taxi("Prius 1", 100)
    My_taxi.drive(40)
    print(My_taxi)
    #Using new ticket prices to drive a car for 100 kilometers
    My_taxi.start_fare()
    My_taxi.drive(100)
    print(My_taxi)

if __name__ == '__main__':
    main()