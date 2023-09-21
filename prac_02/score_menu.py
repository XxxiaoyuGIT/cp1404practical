def main():
    MENU = """G - Get a valid score
P - Print result
S - Show stars
Q - Quit"""

    choice = ""
    score = None

    print(MENU)
    choice = input (":  ") .upper()
    while choice != "Q":
        if choice == "G":
            score = float(input("Enter score: "))
            if score < 0 or score > 100:
                print("Invalid number")
                score = None
        elif choice == "P":
            if score is None:
                print("Please provide the correct number.")
            else:
                result = Score(score)
                print(f"Your score is {result}")
        elif choice == "S":
            if score is None:
                print("Please provide the correct number.")
            else:
                print(star(score))
        elif choice != "Q":
            print("Invalid letter")
            choice = input(": ").upper()

    print("Thank you!")

def Score(score):
    if score < 0:
        return "Invalid score"
    elif score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"

def star(score):
    return "*" * int(score)

if __name__ == "__main__":
    main()
