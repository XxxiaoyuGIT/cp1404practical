def main():
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

    print(MENU)
    choice = input("： ").upper()
    while choice != "Q":
        if choice == "C":
            Celsius = float(input("Celsius: "))
            Fahrenheit = Celsius_to_Fahrenheit(Celsius)
            print(f"Result: {Fahrenheit:.2f} F")
        elif choice == "F":
            Fahrenheit = float(input("Fahrenheit: "))
            Celsius = Fahrenheit_to_Celsius(Fahrenheit)
            print(f"Result: {Celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you.")
def Celsius_to_Fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9.0 / 5 + 32

def Fahrenheit_to_Celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return 5 / 9 * (fahrenheit - 32)

if __name__ == "__main__":
    main()
