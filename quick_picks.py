import random

# Constants
MIN_NUM = 1
MAX_NUM = 45
NUM_PER_QUICK_PICK = 6


def generate_quick_pick():
    quick_pick = []
    while len(quick_pick) < NUM_PER_QUICK_PICK:
        num = random.randint(MIN_NUM, MAX_NUM)
        if num not in quick_pick:
            quick_pick.append(num)
    return sorted(quick_pick)


def main():
    try:
        num_quick_picks = int(input("How many quick picks? "))
        if num_quick_picks < 1:
            raise ValueError("Please enter a positive number.")

        for _ in range(num_quick_picks):
            quick_pick = generate_quick_pick()
            print(" ".join(map(str, quick_pick)))

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
