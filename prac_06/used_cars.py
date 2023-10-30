"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""


from prac_06.car import Car

def main():
    car_run = int(input("Quantity of fuel added:"))
    my_car = Car(45, "Kana")  #Define initial fuel and vehicle name
    print(my_car)

    my_car.add_fuel(car_run)
    print(f"Added {car_run} units of fuel. Fuel = {my_car.fuel}")

    drive_distance = my_car.drive(115)
    print(f"Distance driven: {drive_distance} km")
    print(my_car)

if __name__ == "__main__":
    main()



