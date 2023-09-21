name = input("Enter your name: ")

while True:
    print("Menu:")
    print("H - Say Hello")
    print("G - Say Goodbye")
    print("Q - Quit")
    choice = input("Enter your choice (H/G/Q): ")
    if choice == 'Q':
        print("Finished.")
        break
    elif choice == 'H':
        print(f"Hello, {name}!")
    elif choice == 'G':
        print(f"Goodbye, {name}!")
    else:
        print("Invalid choice. Please choose H, G, or Q.")
