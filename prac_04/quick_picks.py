import random

# Define constants for the range of numbers, the number of quick picks, and the number of numbers to pick
MIN_NUMBER = 1
MAX_NUMBER = 45
NUM_PICKS = 6


def generate_quick_pick():
    # Generate a list of 6 unique random numbers between 1 and 45 without using random.sample
    quick_pick = []
    while len(quick_pick) < NUM_PICKS:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)
    quick_pick.sort()
    return quick_pick


def main():
    num_quick_picks = int(input("How many quick picks? "))

    for _ in range(num_quick_picks):
        quick_pick = generate_quick_pick()
        # Format and print the quick pick as a space-separated string with right alignment
        formatted_quick_pick = " ".join(map(lambda x: str(x).rjust(2), quick_pick))
        print(formatted_quick_pick)


if __name__ == "__main__":
    main()
