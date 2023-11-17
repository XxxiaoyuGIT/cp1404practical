from unreliable_car import unreliablecar

def unreliable_car_test():
    """Test function for UnreliableCar class."""
    kokomi_car = unreliablecar("Kokomi", 100, 50)
    distance_driven = kokomi_car.drive(40)
    print(f"Attempted to drive 40km; drove {distance_driven}km")
    print(kokomi_car)

    distance_driven += kokomi_car.drive(50)
    print(f"Attempted to drive another 50km; drove {distance_driven}km total")
    print(kokomi_car)

if __name__ == '__main__':
    unreliable_car_test()