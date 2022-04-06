"""
CP-1404 Practical
Name:LIU YUHAO
"""

import random


def main():
    num_of_picks = int(input("How many quick picks? "))
    for i in range(0, num_of_picks):
        quick_picks = []
        for _ in range(0, 6):
            rand_value = random.randint(1, 45)
            while rand_value in quick_picks:
                rand_value = random.randint(1, 45)
            quick_picks.append(rand_value)
        PICK1, PICK2, PICK3, PICK4, PICK5, PICK6 = quick_picks[0], quick_picks[1], quick_picks[2], quick_picks[3], quick_picks[4], quick_picks[5]

        print(f"{PICK1} {PICK2} {PICK3} {PICK4} {PICK5} {PICK6}")


main()