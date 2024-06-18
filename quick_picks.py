import random

MINIMUM = 1
MAXIMUM = 45
NUMBERS_PER_LINE = 6


def main():
    number_of_picks = int(input("How many quick picks? "))

    for _ in range(number_of_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{number:2}" for number in sorted(quick_pick)))


def generate_quick_pick():
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_LINE:
        number = random.randint(MINIMUM, MAXIMUM)
        if number not in quick_pick:
            quick_pick.append(number)
    return quick_pick


if __name__ == "__main__":
    main()
